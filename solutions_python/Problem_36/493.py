# Usage:
# python script.py input_file output_file
# If output_file is not specified, it simply
# writes the result to console
# Lines between #---v and #---^ are part of
# the template and should not be edited.

#----------v
import sys
#----------^

def check(index1, index2):
    if index2 is len(string):
        return 1
    else:
        r = 0
        for i in range(index1, len(cases[n])):
            if cases[n][i] == string[index2]:
                r += check(i+1, index2+1)
        return r


#----------v
output = None
if len(sys.argv) == 3:
    output = open(sys.argv[2], 'w')
input = open(sys.argv[1])
#----------^

string = "welcome to code jam"
n = int(input.readline().split("\n")[0])
cases = []
for a in range(n):
    cases.append([ch for ch in input.readline().split("\n")[0]])
    for i in range(len(cases[-1])-1, -1, -1):
        if cases[-1][i] not in string:
            cases[-1].pop(i)

#----------v
for n in range(len(cases)):
#----------^

    result = 0
    result = str(check(0, 0))[-4:]
    while len(result) < 4:
        result = "0" + result

#----------v
    print("Case #"+str(n+1)+": "+result)
    if len(sys.argv) == 3:
        output.write("Case #"+str(n+1)+": "+result+"\n")
if len(sys.argv) == 3:
    output.close()
#----------^










