from fractions import gcd
outfile = open("outputC.txt", "w")
linenum = 0
case = 1
stat = "jeff"
for line in open("C-small-attempt0.in", "rU"):
    if linenum != 0:
        if stat == "jeff":
            listy = line.strip().split(" ")
            lower = int(listy[1])
            upper = int(listy[2])
            stat = "freq"
        elif stat == "freq":
            freqlist = line.strip().split(" ")
            numlist = []
            for number in freqlist:
                numlist.append(int(number))
            n = lower
            while True:
                for item in numlist:
                    if gcd(item, n) != min(item, n):
                        break
                else:
                    answer = n
                    break
                n += 1
                if n > upper:
                    answer = "NO"
                    break
            outfile.write("Case #" + str(case) + ": " + str(answer) + "\n")
            case += 1
            stat = "jeff"
    linenum += 1
outfile.close()

    
