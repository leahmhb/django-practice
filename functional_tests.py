from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(3)

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    # Edith has heard about a new to-do app, checks out homepage
    self.browser.get('http://127.0.0.1:8000/')

    # Edit notices page title and header mention to-do lists
    self.assertIn('To-Do', self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('To-Do', header_text)

    # Edith is invited to enter to-do item right away
    inputbox = self.browser.find_element_by_id('id_new_item')
    self.assertEqual(
      inputbox.get_attribute('placeholder'),
      'Enter a to-do item'
      )
    # Edith types "Buy peacock feathers" into a textbox
    inputbox.send_keys('Buy peacock feathers')

    # After hitting enter, page updates, page lists
    # '1: Buy peacock feathers' as an item in to-do list
    inputbox.send_keys(Keys.enter)

    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertTrue(
      any(row.test == '1: Buy peacock feathers' for row in rows)
      )
    # A textbox invites her to add another item
    # Edith types "Use peacock feathers to make a fly"
    self.fail('Finish the test!')
    # Page updates again
    # Now shows both items on her list
    # Edith wonders whether the site will remember her list
    # Then she sees the site has generated a unique URL for her
    # Explainitory text to that effect
    # Edith visits that URL, her list is still there
    # Edith goes back to sleep


if __name__ == '__main__':
  unittest.main(warnings='ignore')


