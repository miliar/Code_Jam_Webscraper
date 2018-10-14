import math
f = open ('C-small-1-attempt0.in', 'r');

cases = int(f.readline());
case = 0;
output = "";
while case < cases:
    case += 1;
    N, K = f.readline().split()
    N = [int(N)]
    for i in range(int(K)):
        sect = max(N)-1
        mn = int(sect/2)
        mx = int(sect/2) + sect%2
        N.remove(sect+1)
        if mx: N.append(mx)
        if mn: N.append(mn)
    result = str(mx) + " " + str(mn)
    output += "Case #" + str(case) + ": " + str(result) + "\n"

with open('C-small-1.out', 'w') as o:
    o.write(output)
