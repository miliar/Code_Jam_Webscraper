def read_input_file(fileName_in):
    fo = open(fileName, "r")
    content = fo.read().strip()
    fo.close()
    
    lines = content.split("\n")
    tc = lines[0]
    lines = lines[1:]
    
    return(tc, lines)

#fileName = "Tidy_Test.txt"
#fileName = "TN_small.in"
fileName = "TN_large.in"

(tc, lines) = read_input_file(fileName)

outFile = list()
case = 0
for l in lines:    
    num = list(int(t) for t in l.strip())
    i = 0
    if len(num) > 1:
        while(i < (len(num) - 1)):
            n1 = num[i]
            n2 = num[i+1]
            if n1 > n2:                
                j = i+1                
                while ( j < len(num)):
                    num[j] = 9
                    j += 1
                n1 -= 1
                num[i] = n1
                if i > 0:
                    i -= 1
            else:
                i += 1
    
    num = "".join(str(t) for t in num)
    num = num.replace("0", "")
    if len(num) == 0:
        num = "0"    
    case += 1
    ofs = ("Case #" + str(case) + ": " + num)
    #print(ofs)
    outFile.append(ofs) 

fo = open(fileName + ".out.txt", "w")
fo.write("\n".join(outFile))
fo.close()
