import sys

from utils import test_cases
from utils import print_test_case

def find_minimum_friends(attendees_by_shyness):
    total_people_standing = 0
    minimum_friends = 0
    for req_people, attendees in enumerate(attendees_by_shyness):
        attendees = int(attendees)
        if (total_people_standing + minimum_friends) < req_people:
            minimum_friends += req_people - (total_people_standing + minimum_friends)

        total_people_standing += attendees
    return minimum_friends

if __name__ == "__main__":
    assert len(sys.argv) > 1
    for i, test_case in test_cases(sys.argv[1]):
        shynesses = list(test_case.split(' ')[1])
        print_test_case(i, find_minimum_friends(shynesses))
