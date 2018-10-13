def flip(begin, k):
    for i in range(k):
        l[begin+i] = l[begin+i] == '-' and '+' or '-'

t = int(input())
for i in range(1, t + 1):
    s, k = [p for p in input().split(" ")]
    l = list(s)
    k = int(k)

    count = 0
    for j in range(len(l)-k+1):
        if l[j] == '-':
            if len(l)-k < j:
                count = 'IMPOSSIBLE'
                break
            else:
                count += 1
                flip(j, k)
        if j == len(l) - k:
            for e in l[j:]:
                if e == '-':
                    count = 'IMPOSSIBLE'
    print("Case #{}: {}".format(i, count))
 
