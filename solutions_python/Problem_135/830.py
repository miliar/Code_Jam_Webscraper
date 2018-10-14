#!/usr/bin/env python


def read_array(fd, lines):
    temp = [fd.readline().strip().split(' ') for i in range(lines)]
    return temp


f = open('a-small.txt')
TEST_COUNT = int(f.readline())
print TEST_COUNT

fout = open('a-small.out', 'w')
for test in range(TEST_COUNT):
    start_row = int(f.readline())

    start = read_array(f, 4)
    start_eligibles = set(start[start_row - 1])
    #print start_eligibles

    second_row = int(f.readline())
    second = read_array(f, 4)
    second_eligibles = set(second[second_row - 1])
    #print second_eligibles

    eligibles = start_eligibles.intersection(second_eligibles)
    #print 'Overall', eligibles

    if len(eligibles) == 0:
    	verdict = 'Volunteer cheated!'
    elif len(eligibles) == 1:
    	verdict = list(eligibles)[0]
    else:
    	verdict = 'Bad magician!'
    print 'Case #%d: %s' % (test + 1, verdict)
    fout.write('Case #%d: %s\n' % (test + 1, verdict))

fout.close()
