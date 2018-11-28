fin = open("input", "r")
fout = open("output", "r+")

n = int(fin.readline())

found = {}
listfound = []
setfound = set([])

for i in range(n):
    count = 0
    line = fin.readline().split()
    output = "Case #"+str(i+1)+": "
    low = int(line[0])
    high = int(line[1])

    for i in range(int(low), int(high)+1):
        n = str(i)
        for j in range(1, len(n)+1):
            m = n[-j:] + n[:-j]
            if int(m) <= high and int(m) >= low and int(m) > int(n) and int(n) >= low and int(n) <= high:
                count += 1
                listfound.append( (n, m) )
                setfound.add( (n, m) )

    for i in setfound:
        try:
            listfound.remove(i)
        except ValueError:
            #print(str(i) + "not found in listfound")
            continue

    count = count - len(listfound)

    output += str(count)
    fout.write(output + "\n")

fin.close()
fout.close()
