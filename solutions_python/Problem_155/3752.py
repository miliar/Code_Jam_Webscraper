import operator
from functools import reduce

class Case:
    def __init__(self, s_max, case_number):
        self.s_max = s_max;
        self.audience = []
        self.friends = []
        self.case_number = case_number

    def calculate_friends(self):
        people_standing = int(self.audience[0])
        for s_k in range(1, len(self.audience)):
            num_people = int(self.audience[s_k])
            if num_people == 0 or people_standing >= s_k:
                self.friends.append(0)
                people_standing += num_people
            else:
                self.friends.append(s_k - people_standing)
                people_standing += num_people + s_k - people_standing
                
            #print(self.friends)
        
    def __repr__(self):
        #return str(self.s_max) + " " + str(self.audience)
        self.calculate_friends()
        if(len(self.friends) == 0):
            num_friends = 0
        else:
            num_friends = reduce(operator.add, map(int, list(self.friends)))
        return "Case #" + str(self.case_number) + ": " + str(num_friends)
        
f = open('A-small-attempt1.in','rt')
num_cases = int(f.readline())
cases = []

case_number = 0
for line in f:
    s_max = int(line[0])
    case_number += 1

    case = Case(s_max, case_number)
    for pos in range(2, 3 + s_max):
        case.audience.append(line[pos])

    cases.append(case)
    
for case in cases:
    print(case)
