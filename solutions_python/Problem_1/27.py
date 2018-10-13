#!/usr/bin/env python

import sys

class CentralSystem:
    def __init__(self):
        self.engiens = []
        self.queries = []

    def addEngine(self, engine):
        self.engiens.append(engine)

    def addQuery(self, query):
        self.queries.append(query)

    def calcMinSwitches(self):
        current_index = 0
        engine_list = []
        while current_index < len(self.queries):
            max_index = 0
            farmost_engine = ''
            for engine in self.engiens:
                index = 10000000  # more then number of queries
                if engine in self.queries[current_index:]:
                    index = self.queries[current_index:].index(engine)
                if index > max_index:
                    max_index = index
                    farmost_engine = engine
            current_index += max_index
            engine_list.append(engine)

        result = len(engine_list)
        if result > 0:
            result -= 1
        return result

def main():
    if len(sys.argv) == 1:
        f = open('test.in')
    else:
        f = open(sys.argv[1])

    count = int(f.readline())
    for i in xrange(1, count + 1):

        central_system = CentralSystem()

        search_engine_count = int(f.readline().strip())
        for se in xrange(search_engine_count):
            search_engine = f.readline().strip()
            central_system.addEngine(search_engine)

        query_count = int(f.readline().strip())
        for q in xrange(query_count):
            query = f.readline().strip()
            central_system.addQuery(query)

        min_switches = central_system.calcMinSwitches()

        print 'Case #%d: %d' % (i, min_switches)

if __name__ == '__main__':
    main()
