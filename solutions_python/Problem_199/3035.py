file_object  = open('A-large.in', 'r')
t = (file_object.readlines())
st = int(t[0].split()[0])
file_object.close()
file = open('testfile1_1.txt', 'w')
for i in range(1, st + 1):
    a, b = [s for s in t[i].split()]
    n = int(b)
    m = list(a)
    step = 0
    flag = 0
    for j in range(len(m)):
        l=j+n
        if m[j]=='-':
            if l<=len(m):
                for k in range(n):
                    if m[j+k]=="-":
                        m[j+k] = "+"
                    else:
                        m[j+k] = "-"
                step+=1
            else:
                file.write("Case #{}: {}\n".format(i, "IMPOSSIBLE"))
                flag = 1
                break
    if flag!=1:       
        file.write("Case #{}: {}\n".format(i, step))
file.close()

