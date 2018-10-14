import sys

rtlA = 0
rtlB = 1
lA = 3
lB = 4

def read_time(s):
    spl = s.split(':')
    return int(spl[0])*60 + int(spl[1])

def do_test(input):
    T = int(input.readline())
    line = input.readline().split(' ')
    NA = int(line[0])
    NB = int(line[1])
    events = []
    for i in range(NA+NB):
        line = input.readline().split(' ')
        dep = read_time(line[0])
        arr = read_time(line[1])
        if i<NA:
            events.append([dep, lA])
            events.append([arr+T, rtlB])
        else:
            events.append([dep, lB])
            events.append([arr+T, rtlA])
    events.sort()
    necA = 0
    necB = 0
    curA = 0
    curB = 0
    for ev in events:
        if ev[1]==lA:
            if curA>0:
                curA -= 1
            else:
                necA += 1
        elif ev[1]==lB:
            if curB>0:
                curB -= 1
            else:
                necB += 1
        elif ev[1]==rtlA:
            curA += 1
        elif ev[1]==rtlB:
            curB += 1
        else:
            pass
    return [necA, necB]

input = sys.stdin

N = int(input.readline())

for test in range(N):
    answer = do_test(input)
    print 'Case #%(case)d: %(answer1)d %(answer2)d' % \
        {'case': test+1, 'answer1': answer[0], 'answer2': answer[1]}
