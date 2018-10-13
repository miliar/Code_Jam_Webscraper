#!/usr/local/bin/python
def main():
    for case in range(input()):
        engines = []
        queries = []
        for engine in range(input()):
            engines.append(raw_input())
        for query in range(input()):
            queries.append(raw_input());
        switch = -1
        while len(queries) > 0:
            i = 0
            for engine in engines:
                try:
                    i = max(i, queries.index(engine))
                except:
                    i = len(queries)
                    break
            switch += 1
            queries = queries[i:]
        print "Case #%d: %d" % (case+1, switch if switch >=0 else 0)
main()
