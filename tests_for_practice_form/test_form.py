from pages.form_page import FormPage


def test_practice_form():
    practice_form_page = FormPage()
    practice_form_page.open()
    practice_form_page.fill_first_name("Maxim")
    practice_form_page.fill_last_name("Titov")
    practice_form_page.fill_email("test@test.ru")
    practice_form_page.select_gender("Male")
    practice_form_page.fill_user_number("7777777777")
    practice_form_page.pick_date_of_birth("1983", "February", "19")
    practice_form_page.fill_subject("Maths")
    practice_form_page.choose_interest_sport()
    practice_form_page.choose_interest_music()
    practice_form_page.choose_interest_reading()
    practice_form_page.upload_picture("image.jpg")
    practice_form_page.fill_address("City Name, Street Name")
    practice_form_page.choose_state("NCR")
    practice_form_page.choose_city("Noida")
    practice_form_page.submit_button()

    practice_form_page.should_registered_user_with(
        "Maxim Titov",
        "test@test.ru",
        "Male",
        "7777777777",
        "19 February,1983",
        "Maths",
        "Sports, Music, Reading",
        "image.jpg",
        "City Name, Street Name",
        "NCR Noida"
    )
