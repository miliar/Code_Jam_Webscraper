import sys

lines = sys.stdin.readlines()

firstline = lines[0].split()
L = int(firstline[0])
D = int(firstline[1])
N = int(firstline[2])

i = 1
known_data = []
input_cases = []

for x in xrange(D):
    known_data.append(lines[i+x].rstrip())

#print known_data
i += D
for x in xrange(N):
    input_cases.append(lines[i+x].rstrip())

#print input_cases
case = 1
for each in input_cases:
    ind = 0
    success = 0
    tokens = []
    while ind<len(each):
        if each[ind] == '(':
            temp_str = []
            while each[ind] != ')':
                ind += 1
                temp_str.append(each[ind])
            temp_str = temp_str[:-1]
            tokens.append("".join(temp_str))
        else:
            tokens.append(each[ind])
        ind += 1
    #print tokens
    for check in known_data: 
        match = 0
        counter = 0
        while counter<L:
            if len(tokens[counter]) > 1:
                for letter in tokens[counter]:
                    if letter == check[counter]:
                        match += 1
                        break
            else:
                if tokens[counter] == check[counter]: match += 1
            counter += 1
        if match == L: success += 1
    print "Case #"+str(case)+": "+str(success)
    case += 1
