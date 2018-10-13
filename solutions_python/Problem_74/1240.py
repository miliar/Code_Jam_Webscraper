import sys
import os

def run_test_case(test_case):
    time = {'O': 0, 'B': 0}
    pos = {'O': 1, 'B': 1}

    for button in test_case:
        current_robot = button[0]
        other_robot = 'B' if current_robot == 'O' else 'O'
        button_pos = button[1]

        time[current_robot] += abs(button_pos - pos[current_robot]) + 1
        #print "time['O']: %d" % time['O']
        if time[current_robot] <= (time[other_robot]):
            time[current_robot] = time[other_robot] + 1
        pos[current_robot] = button_pos

    return max(time['O'], time['B'])

def main():
    test_cases = int(raw_input()) 
    for i in xrange(test_cases):
        test_case = raw_input()
        test_case_list = test_case.split(" ")
        buttons = int(test_case_list.pop(0))
        test_case_list_tuples = []
        for j in xrange(buttons):
            test_case_list_tuples.append((test_case_list[j*2], int(test_case_list[j*2+1])))
        
        print "Case #%d: %d" % (i + 1, run_test_case(test_case_list_tuples))

if __name__ == '__main__':
    sys.exit(main())

