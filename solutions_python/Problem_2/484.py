#!/usr/bin/env python2.5

"""
train.py
Google Code Jam 208
Solution for the "Train Timetable" problem.
rbp@isnomore.net

Usage: train.py input_file output_file
"""

import sys
from datetime import datetime, timedelta

def read_input():
    in_file = file(sys.argv[1])

    in_text = in_file.readlines()
    n_cases = int(in_text.pop(0))
    cases = []
    for i in range(n_cases):
        turnaround = int(in_text.pop(0))
        na, nb = [int(j) for j in in_text.pop(0).split()]
        cases.append({'turnaround': turnaround, 'na': na, 'nb': nb})
        cases[-1].update({'a2b': [in_text.pop(0).strip()
                                  for j in range(na)]})
        cases[-1].update({'b2a': [in_text.pop(0).strip()
                                  for j in range(nb)]})

    in_file.close()
    return cases

def add_time(t, mins):
    i, j = [int(k.lstrip('0') or '0') for k in t.split(':')]
    dt = datetime(1970, 1, 1, hour=i, minute=j)
    return (dt + timedelta(minutes=mins)).strftime('%H:%M')

def sort_times(a, b):
    return cmp(a['time'], b['time'])

def departures_arrivals(c):
    table = {'departures': [],
         'arrivals': []}
    for times, w in [(c['a2b'], 'A B'), (c['b2a'], 'B A')]:
        w_from, w_to = w.split()
        for t in times:
            dep, arr = t.split()
            table['departures'].append({'where': w_from, 'time': dep})
            table['arrivals'].append({'where': w_to,
                                      'time': add_time(arr, c['turnaround'])})
    table['departures'].sort(cmp=sort_times)
    table['arrivals'].sort(cmp=sort_times)
    return table

def next_time(table):
    try:
        d = table['departures'][0]['time']
    except IndexError:
        d = '24:00'
    try:
        a = table['arrivals'][0]['time']
    except IndexError:
        a = '24:00'
    return min(d, a)

def solve_case(c):
    station = {'A': 0, 'B': 0}
    initial = {'A': 0, 'B': 0}
    table = departures_arrivals(c)
    
    next = next_time(table)
    while next != '24:00':
        d = table['departures']
        a = table['arrivals']

        # New arrivals?
        while a and a[0]['time'] == next:
            where = a[0]['where']
            station[a[0]['where']] += 1
            table['arrivals'].pop(0)

        # New departures?
        while d and d[0]['time'] == next:
            where = d[0]['where']
            if station[where] == 0:
                initial[where] += 1
                station[where] += 1
            station[where] -= 1
            table['departures'].pop(0)
        next = next_time(table)

    return (initial['A'], initial['B'])


if __name__ == '__main__':
    cases = read_input()
    out_file = file(sys.argv[2], "w")
    output = "".join(['Case #%d: %d %d\n' % (i+1, a, b)
                        for i, (a, b) in enumerate([solve_case(c)
                                               for c in cases])])
    out_file.write(output)
    out_file.close()
