def calculate(servers, queries):
    table = [(i, 0) for i in servers]
    table = dict(table)
    count = 0
    cursor=0
    while(cursor < len(queries)):
        a = table[queries[cursor]]
        table[queries[cursor]] += 1
        if (a == 0):
            count += 1
        if (count == len(servers)):
            return 1+calculate(servers, queries[cursor:])
        cursor += 1
    return 0

input = open("input.txt").readlines()
output = open("output.txt", "w")
for i in range(len(input)):
    if input[i][-1] == '\n':
        input[i] = input[i][:-1]

nOfCases = int(input[0])
cursor = 1

for count in range(nOfCases):
    nOfServers = int(input[cursor])
    servers = input[cursor+1:cursor+nOfServers+1]
    
    cursor = cursor + nOfServers + 1
    nOfQuries = int(input[cursor])
    queries = input[cursor+1:cursor+nOfQuries+1]
    result = calculate(servers, queries)
    cursor = cursor + nOfQuries + 1
    print >> output , "Case #" + str(count+1) + ": "+ str(result)
    print "case #" + str(count+1) + ": "+ str(result)


