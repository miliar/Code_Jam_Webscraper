import sys

f = open('example.in', 'r')
g = open('example.solution', 'r')

D = {}
lines1 = f.readlines()
lines2 = g.readlines()

google = lines1[1]+lines1[2]+lines1[3]
english = lines2[0][9:]+lines2[1][9:]+lines2[2][9:]

for i in range(len(google)):
    if google[i] not in D:
        D[google[i]] = english[i]

D['q'] = 'z'
D['z'] = 'q'


num_cases = int(sys.stdin.readline())

for case in range(num_cases):
    message = sys.stdin.readline()
    output = "".join(D[letter] for letter in message)
    print "Case #"+str(case+1)+":", output,
