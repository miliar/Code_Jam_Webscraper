f = open("test.txt")
o = open("final.txt", 'w')
t = int(f.readline())

for i in range(t):
    n = int(f.readline())
    while n>0:

        if int(''.join(sorted(list(str(n))))) == n:
            o.write("Case #{}: {}\n".format(i+1,n))
            break
        else:
            n -= 1
