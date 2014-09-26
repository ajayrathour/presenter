import csv
import os
import operator
from math import ceil


root_path = os.path.realpath(os.path.dirname(__file__))
path_to_csv = os.path.join(root_path, 'data/input.csv')
default_session_numbers = 3

"""
This method is for reading csv and returns sorted list in descending order ,based on hours
"""
def csv_reader():
    fp =  open(path_to_csv,"rb")
    csv_reader = csv.reader(fp)
    csv_reader.next()
    get_sorted_list = sorted(csv_reader,key=operator.itemgetter(1),reverse=True)
    return get_sorted_list


def get_presentation_time(tot_time):
    total_tot_time = tot_time
    each_session_hour = ceil(float(tot_time) / float(default_session_numbers))
    time_slot_list = []
    session = 0
    while session < default_session_numbers:
        if session < default_session_numbers - 1:
            if each_session_hour > total_tot_time / 2:
                each_session_hour = each_session_hour - 1
        else:
            each_session_hour = tot_time
        tot_time = tot_time - each_session_hour
        time_slot_list.append(each_session_hour)
        session +=1
    return time_slot_list


def process_output(total_hours):
    time_slot_list = get_presentation_time(total_hours)
    print "Total hours\t"+ str(total_hours)
    print "slot1\t" +str(time_slot_list[0])
    print "slot2\t" +str(time_slot_list[1])
    print "slot3\t" +str(time_slot_list[2])
    sorted_list = csv_reader()

    session_info = {}
    for i, val in enumerate(time_slot_list):
        session_info["session%s" % i] = {"hours": val,
                                             "presenters": []}
    while total_hours > 0:
        for i, session in enumerate(time_slot_list):
            if session != 0 and len(sorted_list) > 0:
                presenter = sorted_list.pop()
                if session - int(presenter[1]) >= 0:
                    time_slot_list[i] = session - int(presenter[1])
                    key_str = "session%s" % i
                    session_info[key_str]["presenters"].append(presenter)
                else:
                    sorted_list.append(presenter)
                total_hours = total_hours - int(presenter[1])
            else:
                total_hours = 0
                if len(sorted_list) <= 0:
                    print_msg = "Not enough presenters"
                    print print_msg
                    break
    print session_info

if __name__ == "__main__":
    
    total_hours = 12
    process_output(total_hours)
