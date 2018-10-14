#! /usr/bin/env python

def countSwitches(ifs):
    num_engines = int(ifs.readline())
    for i in range(num_engines):
        ifs.readline()
    num_queries = int(ifs.readline())
    queries = []
    switches = 0
    for i in range(num_queries):
        query = ifs.readline().strip()
        if query not in queries:
            if len(queries) + 1 == num_engines:
                switches += 1
                queries = [query]
            else:
                queries.append(query)
    return switches

def main():
    ifs = open("A-large.in")
    ofs = open("out-a.txt", "w")
    num_cases = int(ifs.readline())
    for i in range(num_cases):
        ofs.write("Case #%d: %d\n" % (i + 1, countSwitches(ifs)))

if __name__ == "__main__":
    main()
