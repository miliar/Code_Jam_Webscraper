
__author__="eugen"
__date__ ="$Sep 3, 2009 8:39:23 AM$"


allchars = {} #map to store which chars are at what position
currentwords = set([])

def solve2(prefix, rest):
    global allwords, currentwords, allchars
    if rest == "":
        currentwords.add(prefix)
        return
    else:
        #
        pre, klammerauf, post = rest.partition("(")
        if klammerauf == "":
            solve(prefix+pre, "")
            return
        options, klammerzu, postklzu = post.partition(")")
        if len(options) == 0:
            return
        for c in range(0,len(options)):
            if options[c] in allchars[(len(prefix)+ len(pre))]:
                solve(prefix + pre + options[c], postklzu)
        return

def solve(word, matches):
    if len(matches) == 0:
        return 0
    if word == "":
        return len(matches)
    else:
        head = word[0]
        if word[0] != "(":
            #what words have the current char at the current position
            newmatches = filter(lambda opt: opt[0] ==  head, matches)
            return solve(word[1:], map(lambda no: no[1:], newmatches))
        else:
            # we have options
            options, klammerzu, post = word[1:].partition(")")
            newmatches = filter(lambda m: m[0] in options, matches)
            return solve(post, map(lambda no: no[1:], newmatches))

def purgeword(word, position):
    global allchars
    #return filter(lambda wrd: wrd in allchars, word)
    if word == "":
        return ""
    if word[0] == "(":
        options, klzu, rest = word[1:].partition(")")
        validoptions = ""
        for o in range(0,len(options)):
            if options[o] in allchars[position]:
                validoptions += options[o]

        return "(" + validoptions + ")" + purgeword(rest,position+1)
    else:
       return word[0] + purgeword(word[1:], position+1)

if __name__ == "__main__":
    with open("A-large.in") as f:
        lines = f.readlines()
        head = lines.pop(0).split()
        l,d,n = int(head[0]),int(head[1]),int(head[2])
        #print l,d,n
        #store all words
        allwords = map(lambda l:l[:-1], lines[:d])
        cases = map(lambda l:l[:-1], lines[d:])
        #store all characters
        w1 = allwords[0]
        for c1 in range(0, len(w1)):
            allchars[c1] = set([w1[c1]])
        for w in allwords[1:]:
            for c in range(0, len(w)):
                allchars[c].add(w[c])
        #print cases
        #print allchars
        awset = set(allwords)
        for case in range(1,n+1):
            currentwords.clear()
            print "Case #{0}:".format(case),
            word = cases.pop(0)
            purgedword = word#purgeword(word,0)
            #print purgedword,
            r = solve(purgedword, awset)
            print r;