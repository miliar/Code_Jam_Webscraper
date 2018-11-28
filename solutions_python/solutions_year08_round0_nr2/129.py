#!/usr/bin/python

def convert_to_minute(s):
    fields = s.split(":")
    h = int(fields[0])
    m = int(fields[1])
    return h * 60 + m

def parse(f):
    lines = f.readlines()
    index = 0
    case = []
    line = lines[0].strip()
    N = int(line)
    index = 1
    cases = []
    for i in range(N):
        line = lines[index].strip()
        T = int(line)
        index += 1
        line = lines[index].strip()
        fields = line.split(" ")
        NA = int(fields[0])
        NB = int(fields[1])
        NA_TIME = []
        for j in range(NA):
            index += 1 
            line = lines[index].strip()
            time_fields = line.split()
            depart = convert_to_minute(time_fields[0])
            arrive = convert_to_minute(time_fields[1])
            NA_TIME.append((depart,arrive))
        NB_TIME = []
        for k in range(NB):
            index += 1 
            line = lines[index].strip()
            time_fields = line.split()
            depart = convert_to_minute(time_fields[0])
            arrive = convert_to_minute(time_fields[1])
            NB_TIME.append((depart,arrive))
        d = {}
        d['T'] = T
        d['NA_TIME'] = NA_TIME
        d['NB_TIME'] = NB_TIME
        cases.append(d)
        index += 1
    return cases


def helper(T,NA_TIME,NB_TIME):
    a_ready = []
    for i in NB_TIME:
        arrive = i[1]
        a_ready.append(arrive + T)
    a_ready.sort(reverse=True)
    a_must = 0
    print "ready:", a_ready
    for i in NA_TIME:
        depart = i[0]
        ready = False
        for j in a_ready:
            if j <= depart:
                ready = True
                a_ready.remove(j)
                break
        if not ready:
            a_must += 1
    print "must:", a_must    
    return a_must


def solve(case):
    T = case['T']
    NA_TIME = case['NA_TIME']
    NB_TIME = case['NB_TIME']
    a_must = helper(T,NA_TIME,NB_TIME)
    b_must = helper(T,NB_TIME,NA_TIME)
    return (a_must, b_must)

f = open('input.txt','r')
cases = parse(f)

o = open('output.txt','w')
case_number = 1
for case in cases:
    result = solve(case)
    o.write('Case #%s: %s %s\n' % (case_number, result[0], result[1]))
    case_number += 1
