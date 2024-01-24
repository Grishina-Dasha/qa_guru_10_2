from selene import have, browser


def test_search_1():
    browser.element('[name="q"]').type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_search_2():
    browser.element('[name="q"]').type('fghfghdjkghkdujh').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
