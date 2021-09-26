from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("-headless")
driver = webdriver.Chrome(options=options)

search_string = input("What would you like to generate an essay on?\n")
frmtd_search = search_string.replace(" ", "_")
driver.get(f"https://en.wikipedia.org/wiki/{frmtd_search}")

output = open (fr"{frmtd_search}_essay.txt", "w+")

if "Wikipedia does not have an article with this exact name." in driver.page_source:
    print("Sorry, we couldn't find a Wikipedia page that refers to the topic.")
else:
    body = driver.find_element_by_id("bodyContent")
    p_tags = body.find_elements_by_tag_name("p")
    for p_tag in p_tags:
        output.write(f"\t{p_tag.text}\n\n")
    print("Found a Wikipedia page referring to topic.")
    print(f"Your essay has been generated in {frmtd_search}_essay.txt!")

output.close()