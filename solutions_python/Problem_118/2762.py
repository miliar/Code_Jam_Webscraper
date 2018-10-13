def palindromeCheck(num):
    num = str(num)
    if(num[len(num)-1] == '0') and (num[len(num)-2] == '.'):
        num = num.strip('0')
        num = num.strip('.')
    reverse = num[::-1]
    if (num == reverse):
        return True
    return False


Infile = open('C-small-attempt0.in','r')
Outfile = open('output.txt','w')
CaseNo = int(Infile.readline())
casecount = 0
while (casecount<CaseNo):
    FScount = 0
    limits = (Infile.readline()).split()
    upper = int(limits[1])
    lower = int(limits[0])
    for num in range(lower,upper+1):
        if (palindromeCheck(num) == True):
            root = num**0.5
            if (palindromeCheck(root) == True):
                FScount = FScount+1
    output = 'Case #%d: %d \n' %(casecount+1,FScount)
    print output
    Outfile.write(output)
    casecount = casecount+1
Infile.close()
Outfile.close()
