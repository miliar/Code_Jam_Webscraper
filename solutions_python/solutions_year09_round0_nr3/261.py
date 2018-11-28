welcome = "welcome to code jam"

infile = open("C-small-attempt0.in","r")
outfile = open("C-small.out","w")
numcases = int(infile.readline().strip())

def findoccsin(welcome,text):
    if welcome == "":
        return 1
    else:
        occs = 0
        start = 0
        ix = text.find(welcome[0])
        while ix != -1:
            start = ix + 1
            occs += findoccsin(welcome[1:],text[start:])
            ix = text.find(welcome[0],start)
        return occs 
        
for case in range(numcases):
    text = infile.readline().strip()
    occurences = findoccsin(welcome, text)
    foccs = str(occurences)
    if len(foccs) < 4:
        foccs = ((4-len(foccs))*"0") + foccs
    elif len(foccs) > 4:
        foccs = foccs[-4:]
    out = "Case #" + str(case+1) + ": " + foccs + "\n"
    print out
    outfile.write(out)

infile.close()
outfile.close()
