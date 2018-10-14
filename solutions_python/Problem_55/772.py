f = open('2.in', 'r')
o = open('2.out', 'w')

t = int(f.readline().strip())

for i in range(t):
    r, k, n = map(int, f.readline().strip().split(' '))
    q = map(int, f.readline().strip().split(' '))
    
    money = 0
    for j in range(r):
        tmp = []
        sum = 0
        while len(q)>0 and sum+q[0]<=k:
            tmp.append(q[0])
            sum+=q[0]
            q=q[1:]
        money+=sum
        q = q+tmp
    
    s = "Case #" + str(i+1) + ": " + str(money) + "\n"
    o.write(s)
    