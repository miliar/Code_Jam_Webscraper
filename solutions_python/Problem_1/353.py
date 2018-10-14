import sys
import fileinput

fin = sys.stdin

case_count = int(fin.readline())

for case_number in range (0, case_count):
    engine_count = int(fin.readline())
    for engine_number in range (0, engine_count):
        fin.readline()

    switches = 0
    query_engines = set()

    query_count = int(fin.readline())
    for query_number in range (0, query_count):
        query = fin.readline()
        query_engines.add (query)
        if len (query_engines) >= engine_count:
            switches += 1
            query_engines.clear()
            query_engines.add (query)

    print 'Case #%d: %s' % (case_number + 1, switches)
