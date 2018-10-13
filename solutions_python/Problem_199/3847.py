lines = [line.rstrip('\n') for line in open('A-large.in')]

f = open("A-large.out","w+")

for a in range(1,(len(lines))):
    data = lines[a].split(" ")

    li = list(data[0])
    k = int(data[1])
    l = len(li)
    i = 0
    j = 0
    m = 0
    count = 0

    for i in range(0,l):
        if li[i] == '-':
            count  = count + 1
            for j in range(0,k):
                if (m != 1):
                    try:
                        if li[i] == '-':
                            li[i] = '+'
                        else:
                            li[i] = '-'
                        i = i + 1

                    except:
                        #print("Case #", a, ": IMPOSSIBLE")
                        f.write("Case #%d: IMPOSSIBLE\r\n" % a)
                        m = 1

    if (m != 1):
        #print(li)
        #print(k)
        #print("Case #",a, ": ",count)
        f.write("Case #%d: %d\r\n" % (int(a), int(count)))

f.close()
