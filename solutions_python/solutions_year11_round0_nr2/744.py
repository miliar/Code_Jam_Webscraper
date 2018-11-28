import sys


def solve(C, O, S):
    def combine(list):
        if len(list) < 2:
            return list
        key = list[-1]+list[-2]
        if C.has_key(key):
            list = list[:-2]
            list.append(C[key])
            return list
        key = list[-2]+list[-1]
        if C.has_key(key):
            list = list[:-2]
            list.append(C[key])
            return list
        return list
    
    def opposites(list):
        if len(list) < 1:
            return list
        last = list[-1]
        for i in range(0, len(list)-1):
            if ((last + list[i]) in O) or ((list[i] + last) in O):
                return []
        return list
    
    list = []
    for x in S:
        list.append(x)
        list = opposites(combine(list))
    return list


#some nasty IO stuff...
#the input file is assumed to end with .in
filename = sys.argv[1]
input = open(filename, 'r')
output = open(filename[:-2] + 'out', 'w')
lines = iter(input)
T = int(lines.next()) #read in the number of test cases
i = 1
for line in lines:
    temp = line.split(" ")
    
    invoke_sequence = temp.pop().strip()
    combines = {}
    opposites = []
    for x in temp:
        if not x.isdigit():
            if len(x) == 2:
                opposites.append(x)
            if len(x) == 3:
                combines[x[0]+x[1]] = x[2]
    
    solution = solve(combines, opposites, invoke_sequence)
    output.write('Case #' + str(i) + ': ' + '[' + ', '.join(solution) + ']')
    if (T!=i):
        output.write('\n')
    i = i + 1
input.close
output.close