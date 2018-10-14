import queue
n = int(input())
l = [input().split() for i in range(n)]

def min_max (stalls, people):
    if stalls == people:
        return (0,0)
    q = []
    q.append((stalls,0))
    m1 = stalls
    m2 = stalls
    for i in range(people):
        q.sort(key=(lambda x: (-x[0],x[1])))
        (a,b) = q.pop(0)
        if a%2==0:
            if a!=0:
                q.append((int(a/2),int(a/2)+b))
            if int((a/2)-1) != 0:
                q.append((int((a/2)-1), b))
            m1 = int(a/2)
            m2 = m1-1
        else:
            if a!= 0:
                q.append((int(a / 2), b))
                q.append((int(a / 2), int(a / 2) + b + 1))
                m1 = int(a / 2)
                m2 = m1
    return (max(m1,m2),min(m1,m2))

for j in range(n):
    (a,b) = min_max(int(l[j][0]),int(l[j][1]))
    print("Case #{}: {} {}".format(j+1,a,b))