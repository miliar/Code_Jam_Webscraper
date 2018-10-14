#! /usr/bin/env python

FILE_NAME = 'A-small'

def get_array(in_file):
    ans = int(in_file.readline())
    arr = []
    for i in range(4):
        t = in_file.readline().rstrip()
        if i + 1 == ans:
            arr = t.split(' ')
    return arr


def run_once(in_file):
    ret = set(get_array(in_file)).intersection(set(get_array(in_file)))
    if len(ret) == 0:
        return 'Volunteer cheated!'
    elif len(ret) == 1:
        return list(ret)[0]
    else:
        return 'Bad magician!'
    
in_file = open(FILE_NAME + '-attempt1.in', 'r')
out_file = open(FILE_NAME + '.out', 'w')

num = int(in_file.readline())
for i in range(num):
    out_file.write('Case #' + str(i + 1) + ': ' + run_once(in_file) + '\n')
