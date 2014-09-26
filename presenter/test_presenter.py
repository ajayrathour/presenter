import unittest
import csv
import os
import operator
from math import ceil
from presenters import get_presentation_time, process_output
PROGRAM_PATH = os.path.realpath(os.path.dirname(__file__))
CSV_PATH = os.path.join(PROGRAM_PATH, '/Users/Bigdata/Desktop/presenter/data/input.csv')

default_session_numbers = 3

class TestConference(unittest.TestCase):

    def setUp(self):
        with open(CSV_PATH) as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_reader.next()
            sortedlist = sorted(csv_reader,
                key=operator.itemgetter(1),
                reverse=True)  # sorted by descending number of hours
        self.sortedlist = sortedlist
        

    def test_01_check_session_length(self):
        
        """
        None of the session should have length greater than NUM_HOURS/2 
        """
        
        NUM_HOURS = 8
        session_list = get_presentation_time(NUM_HOURS)
        self.assertLessEqual(session_list[0], NUM_HOURS/2, 
                             "Time duration for first session if greater than half of total allocated hours")

#     def test_02_check_filled_sessions(self):
#         
#         """
#         All of the sessions must be filled: else display "Not enough presenters" 
#         """
#         
#         NUM_HOURS = 44 
#         # if number of hours per session gets increased, it means many 
#         # presenters will completed before time.
#         session_list = divide_presentation_hours(NUM_HOURS)
#         session_dict, return_msg = process_output(NUM_HOURS)
#         self.assertEqual(return_msg, "Not enough presenters",
#                              "Failed test for not enough presenters")

if __name__ == '__main__':
    unittest.main()