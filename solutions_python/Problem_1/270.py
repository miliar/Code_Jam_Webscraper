
def search_case(S, Q):
    count = 0
    map = {}
    open = len(S)
    current = None
    for s in S:
        map[s] = True
    Q.reverse()
    for query in Q:
        print query
        if(map[query] == True):
            open = open - 1
            map[query] = False
            print "Invalidate", query, map
        if open == 0 and current != query:
            print "Served next query with", query
            current = query
            open = len(S) - 1
            count = count + 1
            for s in S:
                map[s] = True
            map[query] = False
    return count

input_file = open("input.txt")
output_file = open("output.txt", "w")
case_count = int(input_file.readline())
for i in range(1, case_count + 1):
    search_count = int(input_file.readline())
    S = []
    for j in range(search_count):
        S.append(input_file.readline().strip())
    query_count = int(input_file.readline())
    Q = []
    for j in range(query_count):
        Q.append(input_file.readline().strip())
    
    output = search_case(S, Q)
    print "=>", S
    print Q
    print "Result", output
    output_line = "Case #%s: %s\n" % (i, output)
    output_file.writelines([output_line])
    print output_line
    