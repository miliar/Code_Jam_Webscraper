from  math import pi

f = open('ans.txt', 'w')

c = int(input())
for i in range(1,c+1):
    n, k = map(int, input().split())
    u = float(input())
    s = [float(j) for j in input().split()]
    s.sort()
    count  = 1
    t = [s[0]]
    if len(s)> 1:
        while (sum(t)+u)/count > s[count]:
            t.append(s[count])
            count+=1
            if count == len(s):
                break
    m = ((sum(t)+u)/count)**count
    for j in s[count:]:
        m*=j
    m = min(m, 1)

    f.write(f"Case #{i}: {m}\n")
f.close()