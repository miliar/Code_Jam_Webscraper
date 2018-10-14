#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Scott Patterson
# asp742@gmail.com
#

import sys

def num_switch(engine_set, query_list):
    nengine = len(engine_set)
    pool = set()
    nswitch = 0
    for q in query_list:
        pool.add(q)
        if len(pool) >= nengine:
            pool = set([q])
            nswitch += 1

    return nswitch

def main():
    file = sys.argv[1]
    data = (lines.strip() for lines in open(file))
    ncase = int(data.next())
    for case in range(ncase):
        nengine = int(data.next())
        engine_set = set(data.next() for x in range(nengine))
        nquery = int(data.next())
        query_list = [data.next() for x in range(nquery)]

        print 'Case #%d: %d' % (case+1, num_switch(engine_set, query_list))

if __name__ == '__main__':
    main()
