a=int(input())
b=a
f = open('out_bath.txt', 'w')

def split(n):
    if n % 2 == 0:
        return int(n / 2) , (int(n / 2) - 1)
    else:
        return  int(n / 2), int(n / 2)


while a>0:
    a-=1
    n, k = input().split()
    n, k = [int(n), int(k)]
    q = []
    min, max = 0, 0
    q.append(n)
    for j in range(k):
        current = q[0]
        q = q[1:]
        max, min= split(current)
        q.append(max)
        q.append(min)
        q.sort(reverse=True)
    f.write('Case #' + str(b - a) + ': ' + str(max)+' '+str(min) + '\n')

f.close()
