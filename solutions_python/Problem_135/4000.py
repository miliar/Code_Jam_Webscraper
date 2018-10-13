def solve(q,g):
    qtotal = int(q.readline())
    for case in range(1,qtotal+1):
        ans = []
        c1 = int(q.readline())
        for i in range(1,5):
            l1 = q.readline()
            if i==c1:
                t1 = l1.split(" ")
        c2 = int(q.readline())
        for j in range(1,5):
            l2 = q.readline()
            if j==c2:
                t2 = l2.split(" ")
        for i in t1:
            for j in t2:
                if int(i)==int(j):
                    ans.append(int(i))
        if len(ans)==1:
            g.write("Case #{0}: {1}\n".format(case,ans[0]))
        elif len(ans)==0:
            g.write("Case #{0}: Volunteer cheated!\n".format(case))
        else:
            g.write("Case #{0}: Bad magician!\n".format(case))

f = open('A-small-attempt4.in', 'r')
g = open('A-small-attempt4.out', 'w+')
solve(f,g)
    
    
