import re

def solve():
    global case, f, f2
    
    [N, K] = re.findall(r'\d+', f.readline());
    N = int(N)
    K = int(K)
    
    m = (pow(2,N))
    
    if (K % m) == (m-1):
        S = "ON"
    else:
        S = "OFF"
    
    f2.write("Case #" + str(case) + ": " + S + "\n")


# BEGIN APP

file = 'A-large.in'

f = open(file, 'r');
f2 = open("A.out", "w");

cases = int(f.readline());

for case in range(1,cases+1):
    solve()


f.close()
f2.close()
