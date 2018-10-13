#!/usr/bin/python
import sys

def cal_seconds(sequence):
    location = {'O' : 1, 'B' : 1}
    time = {'O' : 0, 'B' : 0, 'L' : 0}
    for step in sequence:
        finish_time = max(time[step[0]]+abs(step[1]-location[step[0]])+1,
                                                                time['L']+1)
        time[step[0]] = finish_time
        time['L'] = finish_time
        location[step[0]] = step[1]
    return time['L']

if __name__ == "__main__":
    num_cases = int(sys.stdin.readline().rstrip('\n'))
    for case_no in xrange(1, num_cases+1):
        case = sys.stdin.readline().split()
        sequence = []
        for i in xrange(1, len(case), 2):
            sequence.append((case[i], int(case[i+1])))
        finish_time = cal_seconds(sequence)
        print "Case #%d: %d" % (case_no, finish_time)
