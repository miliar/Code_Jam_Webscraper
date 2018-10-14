def solve(in_num):
    sl = in_num.split()
    n = int(sl[0])
    S = int(sl[1])
    p = int(sl[2])
    out = 0
    for i in range (n):
         num = int(sl[i+3])
         if num >= p:
           if num >= 3*(p-1)+1:
             out=out+1
           elif num >= 3*(p-2)+2 and S > 0:
             out=out+1
             S=S-1
    return str(out)

f = open('input', 'r')
t = int(f.readline())
for n in range(t):
    inp = f.readline()
    print('Case #'+str(n+1)+': '+solve(inp[:-1]))
f.close();
