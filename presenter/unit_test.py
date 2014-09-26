from presenters import process_output
import unittest
import os

total_hours = 12
root_path = os.path.realpath(os.path.dirname(__file__))
path_to_csv = os.path.join(root_path, 'data/input.csv')
default_session_numbers = 3

class TestResults(unittest.TestCase):
    def setUp(self):
        self.return_max = process_output(total_hours)
        self.result_correct = None
        self.result_incorrect = ''
    
    def test_equality(self):
        self.assertEqual(self.return_max, self.result_correct)
    
    def test_inequality(self):
        self.assertNotEqual(self.return_max, self.result_incorrect)
    if __name__ == '__main__':
        unittest.main()