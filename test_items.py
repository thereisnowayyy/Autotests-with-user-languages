link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-ta-work_207/'

def test_addtobasket_button_visible_on_page(browser):
    browser.get(link)
    browser.find_element_by_css_selector("button.btn-add-to-basket")
    button = len(browser.find_elements_by_css_selector("button.btn-add-to-basket"))
    assert button > 0, 'Не отображается кнопка добавления в корзину'
