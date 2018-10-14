import math

def getOutput(line):
    s_max = int(line[0])
    k_array = line[2:]
    ppl = 0
    min = 0
    for i in range(len(k_array)):
        if int(k_array[i]) == 0:
            if ppl > i:
                pass
            else:
                min = min + 1
                ppl = ppl + 1
        elif int(k_array[i]) > 0:
            if ppl >= i:
                ppl = ppl + int(k_array[i])
            else:
                min = min + 1
                ppl = ppl + 1
    return min

f = open('A-small-attempt3.in', 'r')
T = int(f.readline())

outputString = ""
for i in range(T):
    start = i+1
    line = f.readline().strip()
    outputString+= "Case #%i: %i" % (start, getOutput(line)) + "\n"
    
ff = open('output.out', 'w')
ff.write(outputString)
ff.close()

    
