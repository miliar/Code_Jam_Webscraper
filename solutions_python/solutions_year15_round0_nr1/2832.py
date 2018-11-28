fo = open("A-large.in", "r")
fi = open("A-large-output.txt", "w")
line = fo.readline()
t = int(line)
for i in range(t):
    line = fo.readline()
    s,arr = line.split()
    s = int(s)
    summ = 0
    j = 0
    r = 0
    #print(s,arr)
    while j <= s:
        summ = summ + int(arr[j])
        j = j + 1
        if j > summ:
            r = r + j - summ
            summ = j
    fi.write("Case #%d: %d\n"%(i+1,r))
fo.close()
fi.close()
