fhr = open("input.txt",'r')
fhw = open("output.txt",'w')

f = fhr.readlines()
fhr.close()
Cases = int(f[0].strip())

for i in range(0,Cases):
    raw = (f[i+1].strip()).split()
    Smax = int(raw[0])
    People = raw[1]
    Friends = 0
    Total = 0
    j = 0
    while j <= Smax:
        if (People[j] != "0"):
            if (Total < j):
                Friends += j - Total
                Total = j + int(People[j])
            else:
                Total += int(People[j])
        else:
            pass
        j += 1
    fhw.write("Case #" + str(i+1) + ": " + str(Friends) + "\n")
fhw.close()
