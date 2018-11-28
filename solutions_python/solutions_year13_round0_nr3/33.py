from itertools import count

MX = 60

a = [1,2,3]

def go(x, rest):
    s = str(x)
    if len(s)*2 > MX:
        return
    a.append(int(s + s[::-1]))
    if len(s)*2+1 <= MX:
        for i in count(0):
            if i*i > rest:
                break
            a.append(int(s + str(i) + s[::-1]))
    for i in count(0):
        if i*i*2 > rest:
            break
        go(x*10+i, rest - 2*i*i)

for i in count(1):
    if i*i*2 > 9:
        break
    go(i, 9-2*i*i)

print(len(a))
with open("pal1.in","w") as f:
    for i in sorted(a):
        f.write(str(i*i)+"\n")
b = sorted(i*i for i in a)

FN = "c-large-2"
with open(FN+".in","r") as fi, open(FN+".out","w") as fo:
    tests = int(fi.readline().strip())
    for test in range(1,tests+1):
        print('*',end='')
        x,y = map(int,fi.readline().strip().split())
        res = sum(1 for i in b if x <= i and i <= y)
        fo.write("Case #{}: {}\n".format(test,res))
