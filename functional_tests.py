from selenium import webdriver
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
    self.fail('Finish the test!')

    # Edith is invited to enter to-do item right away
    # Edith types "Buy peacock feathers" into a textbox
    # After hitting enter, page updates, page lists
    # '1: Buy peacock feathers' as an item in to-do list
    # A textbox invites her to add another item
    # Edith types "Use peacock feathers to make a fly"
    # Page updates again
    # Now shows both items on her list
    # Edith wonders whether the site will remember her list
    # Then she sees the site has generated a unique URL for her
    # Explainitory text to that effect
    # Edith visits that URL, her list is still there
    # Edith goes back to sleep


if __name__ == '__main__':
  unittest.main(warnings='ignore')


