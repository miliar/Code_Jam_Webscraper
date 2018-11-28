INPUT_FILE = 'inputs/A-large.in'
OUTPUT_FILE = 'outputs/A-large.out'

def glueNumber(l, base):
    retVal = 0
    for elem in l:
        retVal = retVal * base + elem
    return retVal

f_in = open(INPUT_FILE, 'r')
f_out = open(OUTPUT_FILE, 'w+')

T = int(f_in.readline().strip())
for i in range(T):
    alNum = f_in.readline().strip();
    base = 0
    for ind, a in enumerate(alNum):
        if (not a in alNum[0:ind]):
            base += 1
    if base == 1:
        base += 1
            
    trNum = [0] * len(alNum)
    digits = {alNum[0]: 1}
    trNum[0] = 1
    currDigit = 0
    for ind, a in enumerate(alNum):
        if a in digits:
            trNum[ind] = digits[a]
        else:
            if (currDigit == 1):
                currDigit += 1
                
            trNum[ind] = currDigit;
            digits[a] = currDigit;
            
            currDigit += 1;
            
    num = glueNumber(trNum, base)
    print("Case #" + str(i + 1) + ": " + str(num))
    f_out.write("Case #" + str(i + 1) + ": " + str(num) + "\n")

f_in.close()
f_out.close()
