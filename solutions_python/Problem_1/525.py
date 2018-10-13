
def find_switches((s_engines, queries)):
    switches = 0
    while queries:
        try:
            max_index = max((queries.index(e) for e in s_engines))
        except ValueError:
            break
        else:
            queries = queries[max_index:] 
            switches += 1 
    return switches

def read_case(file):
    S = int(file.readline().strip())
    sengines = [file.readline().strip() for i in range(S)]
    Q = int(file.readline().strip())
    queries = [file.readline().strip() for i in range(Q)]
    return sengines, queries

if __name__ == '__main__':
    import sys
    input_file = open(sys.argv[1])
    N = int(input_file.readline().strip())
    for i in range(1, N+1):
        print "Case #%d: %d" % (i, find_switches(read_case(input_file)))

