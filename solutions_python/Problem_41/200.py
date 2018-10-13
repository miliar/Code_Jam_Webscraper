def getNextNo(startingNo):
    case_digits=getDigits(startingNo)
    if case_digits[0]!=0:
        case_digits.insert(0,0)
    else:
        while case_digits[0]!=0:
          case_digits.pop()
        case_digits.insert(0,0)    
    while True:
        startingNo+=1
        no_digits=getDigits(startingNo)
        if no_digits==case_digits[1:]:
            return startingNo
        elif no_digits==case_digits:
            return startingNo
            

def getDigits(Number,sorted=True):
    
    digits=[]
    while Number!=0L:
        digits.append(int(Number%10))
        Number=Number/10L
    if sorted:
        digits.sort()
        return digits
    else:            
        return digits[::-1]    
file_in=open("B-small-attempt1.in")
no_cases=int(file_in.readline().strip())
cases=[]
lines=file_in.readlines()
file_in.close()
cases=[]
for line in lines:
    cases.append(long(line.strip()))
print cases
file_out=open("out.txt","w")
i=1
for case in cases:
    output_str="Case #%d: %s"%(i,getNextNo(case))
    file_out.write(output_str+"\n")
    print output_str
    i+=1
file_out.close()    
    