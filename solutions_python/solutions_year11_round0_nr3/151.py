
def tobinary(n):
    if n == 0:
        return 0
    result = ""
    while n > 0:
        result = str(n % 2) + result
        n = n / 2
    return int(result)

#add 2 binary numbers to resulting binary number by Patrick
def Paddition(a, b):
    a = str(a)
    b = str(b)
    la = len(a)
    lb = len(b)
    if la > lb:
        d = la - lb
        for i in range(d):
            b = "0" + b
    elif lb > la:
        d = lb - la
        for i in range(d):
            a = "0" + a
    #print a
    #print b
    result = ""
    for j in range(len(a)):
        if (a[j] == "0" and b[j] == "0") or (a[j] == "1" and b[j] == "1"):
            result += "0"
        if (a[j] == "1" and b[j] == "0") or (a[j] == "0" and b[j] == "1"):
            result += "1"
    return int(result)
    

def lstadd(a):
    al = len(a)
    ar = 0
    if al == 1:
        ar = a[0]
    elif al > 0:
        i = 1
        prev = a[0]
        while i < al:
            ar = Paddition(a[i], prev)
            prev = ar
            i += 1
    return ar

def main():
    inpfile = open("C-large.in", 'r')
    outfile = open('outfile', 'w')
    casenum = int(inpfile.readline().strip())
    for case in range(1, casenum + 1):
        line1 = inpfile.readline().strip()
        line2 = inpfile.readline().strip().split()
        numcandy = int(line1)
        candylst = line2
        x = 0
        while x < numcandy:
            candylst[x] = int(line2[x])
            x += 1
        #print numcandy
        #print candylst
        x = 0
        binarylst = candylst[:]
        while x < len(candylst):
            binarylst[x] = tobinary(candylst[x])
            x += 1
        Sum = lstadd(binarylst)
        #print binarylst
        #print candylst
        #print Sum
            
        if Sum == 0:
            candylst.sort()
            out = str(sum(candylst) - candylst[0])
        else:
            out = "NO"
        
        result = "Case #" + str(case) + ": " + out + "\n"
        outfile.write(result)
    inpfile.close()
    outfile.close()

    
if __name__ == "__main__":
    main()
    
