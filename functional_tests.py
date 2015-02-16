from selenium import webdriver
import unittest
class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	def tearDown(self):
		self.browser.quit()
	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith has heard about a cool new online to-do app. She goes
		# to check out its homepage
		self.browser.get('http://localhost:8000')
		# She notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title) #
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)


		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'enter a to-do item'
		)

		inputbox.send_keys(Keys.Enter)
		table = self.browser.find_element_by_id('id_list_table')
		rows = self.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text =='1: Buy cigarettes' for row in rows)
		)
		
		self.fail('Finish the test!') #
		# She is invited to enter a to-do item straight away

if __name__ == '__main__': #
	unittest.main(warnings='ignore')
