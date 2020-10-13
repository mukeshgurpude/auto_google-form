from selenium import webdriver
import sys
import random
import time


def submit(browser, classes):
    buttons = browser.find_elements_by_class_name(classes["button"])
    buttons[-1].click()


def fill_form(url):
    cont = ["Color", "Electronics", "Container", "LCD", "Design"]
    bugs = ["Doesn't count correctly, if objects are at high speed",
            "Doesn't always count correctly, if the objects are at high speed",
            "sometimes, Display is blurry",
            "Unable to count objects",
            "low accuracy in dim light"]
    feedbacks = ["It's a good product.. I've not faced any issue till now",
                 "High accuracy",
                 "I haven't been confronted with any issues until now",
                 "This is indeed a fantastic product. I've not faced any problem till now",
                 "Well done, but there are some bugs, that should be fixed",
                 "Better you people design it properly",
                 "I suggest that you should use some better quality sensor and display"]
    features = ["A handle or some type of stand should be there for proper placing",
                "Need power backup in case of power failure",
                "For proper positioning, a handle or some sort of stand should be there.",
                "A handle or some kind of stand should be in place for proper placement.",
                "Need a reserve of power in the event of electricity loss.",
                "For proper placing, a handle or some kind of stand should be there."]
    questions = ["What to do, if the case is damaged, when bought?",
                 "How to clean the lcd?",
                 "How to submit a bug report?",
                 "How can I request for a feature?",
                 "What is the warranty for this counter?",
                 "What to do if display broke?"]
    classes = {"input": "quantumWizTextinputPaperinputInput",
               "radio": "docssharedWizToggleLabeledLabelWrapper",
               "textarea": "quantumWizTextinputPapertextareaInput",
               "button": "appsMaterialWizButtonPaperbuttonContent"}
    options = webdriver.ChromeOptions()
    options.add_argument("-incognito")
    options.add_argument("--headless")
    browser = webdriver.Chrome(executable_path=r"C:\Users\Asus\Downloads\WebDriver\chromedriver.exe",
                               options=options)
    browser.get(url)
    time.sleep(2)

    # First Page
    input_boxes = browser.find_elements_by_class_name(classes["input"])
    name_box = input_boxes[0]
    email_box = input_boxes[1]
    text_boxes = browser.find_elements_by_class_name(classes["textarea"])
    feedback_box = text_boxes[0]
    improve = text_boxes[1]
    # name_box.send_keys("testing")
    feedback_box.send_keys(random.choice(feedbacks))
    choice = random.choice(range(5))
    if choice != 4:
        browser.find_elements_by_class_name(classes["radio"])[choice].click()
    submit(browser, classes)
    time.sleep(2)
    if not choice: return

    # Second Page
    print(f"Choice: {choice}")
    if choice == 0:
        comment = browser.find_elements_by_class_name(classes["textarea"])[0]
        comment.send_keys(random.choice(feedbacks))
    elif choice == 1:
        ques = browser.find_elements_by_class_name(classes["textarea"])
        for i in range(random.choice(range(3))):
            ques[i].send_keys(random.choice(questions))
    elif choice == 2:
        radios = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupRadioButtonContainer")
        radios[random.choice(range(5))].click()
        browser.find_elements_by_class_name(classes["textarea"])[0].send_keys(random.choice(bugs))
    elif choice == 3:
        rad = random.choice(range(3))
        if rad == 2:
            browser.find_elements_by_class_name("quantumWizTextinputSimpleinputInput")[0].send_keys(random.choice(cont))
        else:
            browser.find_elements_by_class_name("docssharedWizToggleLabeledContent")[rad].click()
        browser.find_elements_by_class_name(classes["textarea"])[0].send_keys(random.choice(features))
    submit(browser, classes)


if __name__ == '__main__':
    try:
        link = sys.argv[1]
    except Exception as e:                  # List index out of range
        link = input("Enter the form url: ")
    for i in range(15):
        print(i+1)
        try:
            fill_form(link)
            print(f"{i+1} Done")
        except Exception as e:
            print(f"{i+1}: {e}")
            continue
