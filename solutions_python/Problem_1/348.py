#!/usr/bin/python

import sys


def find_optimal(engines, requests, n = 0):

    if len(requests) == 0: return 0

    max_queue_length = 0
    while max_queue_length != len(requests):
        for engine in engines:
            queue_length = 0
            for request in requests:
                if request == engine:
                    break
                queue_length += 1
            max_queue_length = max(max_queue_length, queue_length)
        if max_queue_length != len(requests):
            requests = requests[max_queue_length:]
            n = n + 1
            max_queue_length = 0
        else:
            return n
    return n


if __name__ == '__main__':
    f = open(sys.argv[1])
    n_cases = int(f.readline())
    for case in range(n_cases):
        n_engines = int(f.readline())
        engines = []
        for j in range(n_engines):
            engines.append(f.readline().strip('\r\n'))
        n_requests = int(f.readline())
        requests = []
        for j in range(n_requests):
            requests.append(f.readline().strip('\r\n'))

        #print '%d eng, %d req' % (n_engines, n_requests)

        #print ','.join(engines)

        n_switches = find_optimal(engines, requests)
        print 'Case #%d: %d' % (case + 1, n_switches)

