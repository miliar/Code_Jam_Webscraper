total = 10**7
res = []
for i in range(1, total+1):
    if str(i) == str(i)[::-1]:
        if str(i**2) == str(i**2)[::-1]:
            res.append(i**2)

with open("c.in","r") as in_file:
    i=0
    for row in in_file:
        if len(row.split()) > 1:
            ans=0
            i=i+1
            a, b = row.split()
            for t in res:
                if t>=int(a) and int(b)>=t:
                    ans=ans+1
            print "Case #%d: %d"%(i, ans)
