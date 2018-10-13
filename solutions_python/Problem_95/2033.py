'''
Created on Apr 13, 2012

@author: mchesley
'''

D = {};

D['y'] = 'a'
D['e'] = 'o'
D['q'] = 'z'

G = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv"
S = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup"

for i in range(len(G)):
    D[G[i]] = S[i]

s = ""

handle = open("cj.in", "r")
cases = handle.readline()
for case in range(int(cases)):
    line = handle.readline()
    s += "Case #" + str(case+1) + ": "
    for c in line:
        print c
        if c == ' ': s += ' '
        elif c == '\n': s += '\n'
        elif not D.has_key(c): s += '*'
        else: s += D[c]
    case += 1
    
handle.close()

print s

handle = open("cj.out","w")
handle.write(s)
handle.close()