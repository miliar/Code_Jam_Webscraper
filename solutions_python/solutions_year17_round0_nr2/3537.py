
def seq(n):

    r = str(n)
    t = r[1:len(str(n))] + '9'
    print(r,t)
    for x in zip(r,t):
        print(x)
    return all([ int(a)<=int(b) for (a,b) in zip(r,t)])

def fun(n):
    while n >=0:
        if seq(n):
            return n
        n = n-1

v = open('B-small-attempt0.in', 'r')
t = open('out1.txt', 'w')
r = int(v.readline())

l = [int(v.readline()) for x in range(r)]

for i,x in enumerate(l):
    t.writelines('Case #{0}: {1}\n'.format(i+1, fun(x)))

t.close()
v.close()
# print(fun(113214234))
n = 139
print(seq(n))
# print(fun(n))