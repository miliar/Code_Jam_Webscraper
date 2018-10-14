#Google Code Jam
#############################

inFile = open("C:/Users/Alex/Desktop/codejam2/cjinput.txt",'r')
outFile = open("C:/Users/Alex/Desktop/codejam2/cjoutput.txt",'w')
lines = []

for line in inFile:
    lines.append(line)

#############################

params = lines[0].split(' ')

T = int(params[0])

##!!!!!!
endpt = 1000000

def permutations(str):
    if len(str) <= 1:
        yield str
    else:
        for perm in permutations(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

def stripZeros(list):
    if list[0][0] != "0":
        return list
    else:
        for c in range(0,len(list)-1):
            if(list[c][0] == "0"):
                list.pop(0)
            else:
                break
        return stripZeros(list)

for l in range(1,T+1):
    N = origN = int(lines[l].strip())
    solutionFound = False
    while not solutionFound:
        operatinglist = list(set(stripZeros(sorted(permutations(str(N))))))
        for i in sorted(operatinglist):
            if int(i) > origN:
                outFile.write( "Case #" + str(l) + ": " + str(i) + "\n")
                solutionFound = True
                break
        if not solutionFound:
            N = N * 10
    if not solutionFound:
        print ("Case #" + str(l) + ": " + str(N) + "\n")
        outFile.write( "Case #" + str(l) + ": " + str(N) + "\n") 

#############################
inFile.close()
outFile.close()
