import os
import time
from selene import browser, have, be, by


def test_fill_submit_form(setup_browser):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element(by.text('Practice Form')).should(be.visible)  # Ждем заголовок

# Заполняем основные данные
    browser.element('#firstName').type('Alex')
    browser.element('#lastName').type('Bagel')
    browser.element('#userEmail').type('alexbagel@mail.ru')
    browser.element(by.text('Male')).click()
    browser.element('#userNumber').type('9021778990')

# Заполняем дату рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker').should(be.visible)
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select option[value="5"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select option[value="1990"]').click()
    browser.element('.react-datepicker__day--019:not(.react-datepicker__day--outside-month)').click()
    browser.element('#dateOfBirthInput').should(have.value('19 Jun 1990'))

# Выбираем предмет
    browser.element('#subjectsInput').type('English')
    browser.element('.subjects-auto-complete__menu').with_(timeout=5).should(be.visible)
    browser.all('.subjects-auto-complete__option').first.click()

# Выбираем хобби
    browser.element(by.text('Sports')).click()
    browser.element(by.text('Music')).click()

# Загружаем файл
    browser.element('#uploadPicture').send_keys(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'mount.jpg'))

# Заполняем адрес
    browser.element('#currentAddress').type('Lomonosov str. 8')

    browser.element('#state').click()
    browser.element('.css-26l3qy-menu').with_(timeout=5).should(be.visible)
    browser.element('#react-select-3-option-2').click()

    browser.element('#city').click()
    browser.element('.css-26l3qy-menu').with_(timeout=5).should(be.visible)
    browser.element('#react-select-4-option-1').click()

# Отправляем форму
    browser.element('#submit').click()

# Проверяем успешную отправку формы
    assert browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    time.sleep(10)