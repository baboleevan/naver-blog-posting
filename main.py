import pyperclip
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys

LOGIN_URL = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'

blog_id = 'BLOG_ID_HERE'
login_id = 'LOGIN_ID_HERE'
password = 'PASSWORD_HERE'

driver = webdriver.Edge(executable_path='./msedgedriver', capabilities={})
driver.implicitly_wait(3)


def main():
    try:
        login(login_id, password)
        post_article(blog_id, 'title', 'content', ['블챌', '오늘일기'])
    finally:
        time.sleep(3)
        driver.close()


def login(login_id, password):
    driver.get(url=LOGIN_URL)

    clipboard_input('//*[@id="id"]', login_id)
    clipboard_input('//*[@id="pw"]', password)
    driver.find_element_by_xpath('//*[@id="log.login"]').click()

    time.sleep(1)


def post_article(blog_id, title, content, tags):
    driver.get(url=get_blog_post_url(blog_id))
    driver.switch_to.frame('mainFrame')

    close_popup()
    write_title(title)
    write_content(content)
    attach_tags(tags)
    complete_post()


def clipboard_input(user_xpath, user_input):
    temp_user_input = pyperclip.paste()
    pyperclip.copy(user_input)
    driver.find_element_by_xpath(user_xpath).click()
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()

    pyperclip.copy(temp_user_input)
    time.sleep(0.3)


def get_blog_post_url(blog_id):
    return 'https://blog.naver.com/' + blog_id + '?Redirect=Write'


def close_popup():
    close_writing_article()
    close_help_panel()


def close_writing_article():
    try:
        writing_cancel_button = driver.find_element_by_css_selector('.se-popup-button.se-popup-button-cancel')
        writing_cancel_button.click()
    except:
        pass


def close_help_panel():
    try:
        close_help_button = driver.find_element_by_css_selector('.se-help-panel-close-button')
        close_help_button.click()
    except:
        pass


def write_title(title):
    title_field = driver.find_element_by_css_selector('.se-placeholder.__se_placeholder.se-ff-nanumgothic.se-fs32')
    action = ActionChains(driver)
    (
        action.move_to_element(title_field)
            .pause(1)
            .click()
            .send_keys(title)
            .perform()
    )
    action.reset_actions()


def write_content(content):
    content_field = driver.find_element_by_css_selector('.se-component.se-text.se-l-default')
    content_field.click()

    action = ActionChains(driver)
    (
        action.move_to_element(content_field)
            .pause(1)
            .click()
            .send_keys(content)
            .perform()
    )
    action.reset_actions()


def attach_tags(tags):
    for tag in tags:
        action = ActionChains(driver)
        action.send_keys(Keys.ENTER).send_keys('#' + tag).perform()
        action.reset_actions()


def complete_post():
    post_button = driver.find_element_by_css_selector('.btn_publish__1tn-5')
    post_button.click()

    confirm_button = driver.find_element_by_css_selector('.btn_confirm__14fnr')
    confirm_button.click()


if __name__ == "__main__":
    main()
