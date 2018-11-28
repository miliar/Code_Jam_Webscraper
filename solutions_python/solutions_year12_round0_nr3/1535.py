'''
Created on Apr 13, 2012

@author: mchesley
'''

def recycled(m,n):
    pairs = []
    
    for x in range(m, n+1):
        s = str(x)
        possible = s[1:] + s[0]
        while possible != s:
            if int(possible) >= m and int(possible) <= n and int(possible) != x:
                pair = [x, int(possible)]
                pair.sort()
                pairs.append(pair)
            possible = possible[1:] + possible[0]
    print pairs
    
    final = []
    for pair in pairs:
        if pair not in final:
            final.append(pair)
    
    print final
    answer = len(final)
    return answer

handle = open("cj.in", "r")
cases = handle.readline()

s = ""

for case in range(int(cases)):
    s += "Case #" + str(case+1) + ": "
    line = handle.readline()
    nums = line.split()
    answer = recycled(int(nums[0]), int(nums[1]))
    s += str(answer) + '\n'

print s

handle = open("cj.out","w")
handle.write(s)
handle.close()