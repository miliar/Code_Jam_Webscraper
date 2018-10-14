

f = open("p1.in","r")
g = open("p1.out","w")

num_lines = int(f.readline().strip())

for test in range(1,num_lines + 1):
    d = {}
    aux = f.readline().strip()
    a = int(aux.split()[0])
    b = int(aux.split()[1])
    total = 0
    for i in range(a,b + 1):
        if i in d:
            continue
        curd = {}
        j = i
        num_dig = len(str(i)) - 1
        num = 0
        while(j not in curd):
            d[j] = 1
            curd[j] = 1
            if j >= a and j <= b:
                num += 1
            j = (j % 10) * 10 ** num_dig + (j / 10)
        total += num * (num - 1) / 2
    g.write("Case #" + str(test) + ": "+ str(total) + "\n")

    


