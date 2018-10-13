import copy
RUNNAME = "B-large"
INFILE = open(RUNNAME+".in","r")
OUTFILE = open(RUNNAME+".out","w")

# Turn a number as a string into a number
def magic(inthing):
    if inthing.isdigit():
        return int(inthing)
    try:
        return float(inthing)
    except ValueError:
        return inthing
    
# Get the data on the next line of the input file
def cj_getline():
    line = INFILE.readline().strip()
    lineparts = line.split(" ")
    parts = [magic(linepart) for linepart in lineparts]
    return parts

numcases = cj_getline()[0]
for caseno in range(numcases):
    casestr = "Case #"+str(caseno+1)+": "
    print casestr.strip(),
    OUTFILE.write(casestr)
    prevno = INFILE.readline().strip()
    orderix = -1
    chars = []
    for ix in range(len(prevno)-1):
        chars.append(int(prevno[ix]))
        if chars[-1] < int(prevno[ix+1]):
            orderix = ix
            oldkeyno = chars[-1]
    chars.append(int(prevno[-1]))
    print orderix, prevno,
    if orderix == -1:
        # Numbers all in maxed order--add a zero
        chars.sort()
        zeros = 1
        while chars[0] == 0:
            chars.pop(0)
            zeros += 1
        chars[1:1] = [0]*zeros
        newno = ""
        for char in chars:
            newno += str(char)
    else:
        fixedpart = chars[:orderix] 
        mutablepart = chars[orderix:]
        keynopool = []
        for char in mutablepart:
            if char > oldkeyno:
                keynopool.append(char)
        newkeyno = min(keynopool)
        mutablepart.remove(newkeyno)
        mutablepart.sort()
        newno = ""
        for char in fixedpart:
            newno += str(char)
        newno += str(newkeyno)
        for char in mutablepart:
            newno += str(char)
            
    oldnodigs = {}
    for char in prevno:
        if char in oldnodigs:
            oldnodigs[char] += 1
        else:
            oldnodigs[char] = 1
    newnodigs = {}
    for char in newno:
        if char in newnodigs:
            newnodigs[char] += 1
        else:
            newnodigs[char] = 1
    for dig, count in oldnodigs.items():
        if dig == "0":
            print "--",count, newnodigs[dig]
        else:
            if count != newnodigs[dig]:
                print "!!!", dig, count, newnodigs[dig] 
    print newno
    OUTFILE.write(newno+"\n")
INFILE.close()
OUTFILE.close()