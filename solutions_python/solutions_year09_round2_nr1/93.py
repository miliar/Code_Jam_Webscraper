RUNNAME = "A-large"
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

def maketreenode(subtreestr):
    parts = subtreestr.strip(" ()").partition("(")
    thisnode = parts[0].strip().split(" ")
    multiplier = float(thisnode[0])
    if len(thisnode) == 1:
        return {"multiplier":multiplier}
##    print thisnode
    attribute = thisnode[1]
    subtreebits = parts[2].split(" ")
    issubtreestr = subtreebits.pop(0)
    openbrackets = 1
    # Handle a leaf node
    if issubtreestr.find(")") != -1:
        openbrackets = 0
    while openbrackets > 0:
        if subtreebits[0].find("(") != -1:
            openbrackets += 1
        if subtreebits[0].find(")") != -1:
            openbrackets -= 1
        issubtreestr += " " + subtreebits.pop(0)
    ifis = maketreenode(issubtreestr)
    ifisnt = maketreenode(" ".join(subtreebits))
    return {"multiplier":multiplier, "attr":attribute, "is":ifis,"isnt":ifisnt}

def followtree(dtree, attrs):
##    print attrs,
    if "attr" not in dtree:
        return dtree['multiplier']
##    print dtree['attr']
    if dtree['attr'] in attrs:
        return dtree['multiplier']*followtree(dtree['is'],attrs)
    else:
        return dtree['multiplier']*followtree(dtree['isnt'],attrs)

numcases = cj_getline()[0]
for caseno in range(numcases):
    casestr = "Case #"+str(caseno+1)+":\n"
    print casestr.strip()
    OUTFILE.write(casestr)
    treestr = ""
    numtreelines = cj_getline()[0]
    for treelineno in range(numtreelines):
        treestr += " " +INFILE.readline().strip()
    dtree = maketreenode(treestr)
    print dtree
    numanimals = cj_getline()[0]
    for animalno in range(numanimals):
        animal = cj_getline()
        name = animal[0]
        print name,
        attrs = animal[2:]
        # Have to do it this way, or Python gives scientific notation for
        # small values
        probcute = "%.7f" % followtree(dtree, attrs)
        print probcute
        OUTFILE.write(probcute+"\n")
INFILE.close()
OUTFILE.close()