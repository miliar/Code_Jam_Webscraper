
__author__="eugen"
__date__ ="$Sep 3, 2009 1:40:35 PM$"

def positions(c):
    if c == "w":
        return [0]
    elif c == "e":
        return [1,6,14]
    elif c == "l":
        return [2]
    elif c == "c":
        return [3,11]
    elif c == "o":
        return [4,9,12]
    elif c == "m":
        return [5,18]
    elif c == " ":
        return [7,10,15]
    elif c == "t":
        return [8]
    elif c == "d":
        return [13]
    elif c == "j":
        return [16]
    elif c == "a":
        return [17]
    else:
        return []

def solve2(line):
    #init map
    wordcount = {}
    for i in range(0,19):
        wordcount[i]=0
    #print wordcount
    for p in range(0,len(line)):
        currentchar = line[p]
        currentpos = positions(currentchar)
        #print currentchar, currentpos
        for pos in currentpos:
            if pos == 0:
                wordcount[0] += 1
            else:
                wordcount[pos] += wordcount[pos-1]
                #print pos," increased by ",wordcount[pos-1]
    #print wordcount
    return wordcount[18] % 10000

def solve(line, phrase):
    if len(line) < len(phrase):
        return 0
    elif phrase == "":
        return 1
    else:
        count = 0;
        pc1 = phrase[0]
        for c in range(0, len(line)-len(phrase)+1):
            if line[c] == pc1:
                count += solve(line[c:], phrase[1:])
                count = count % 10000
        return count

def mitnullen(zahl):
    prefix = ""
    if zahl < 10:
        return "000"+str(zahl)
    if zahl < 100:
        return "00"+str(zahl)
    if zahl < 1000:
        return "0"+str(zahl)
    else:
        return str(zahl)

if __name__ == "__main__":
    with open("C-large.in") as f:
        lines = f.readlines()
        head = lines.pop(0)
        cases = int(head)
        for case in range(1,cases+1):
            print "Case #{0}:".format(case),
            line = lines.pop(0)[:-1]
            #print line
            result = solve2(line)
            print mitnullen(result);