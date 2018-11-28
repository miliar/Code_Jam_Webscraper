
import sys

def loadinput():

    fn = sys.argv[1]

    f = open(fn,"r")

    l1 = f.readline()

    l,d,n = [int(x) for x in l1.split()]

#    print "param: "
#    print l,d,n
#    print ""

    dict = [f.readline()[:-1] for i in range(d)]

#    print "dictionary: "
#    print dict
#    print ""

    solve = [f.readline()[:-1] for i in range(n)]

#    print "solve: "
#    print solve
#    print ""

    return l,d,n,dict,solve

# naive solution

def parsechar(word):
    if word[0] == '(':
	i = word.index(')')
	return word[1:i],word[i+1:]
    else:
	return word[0],word[1:]

# Optimize by building grouped word tables?
def indict_count(dict,word):
    subdict = dict[:]   # Full copy
    i = 0
# Parse the characters in the word one at a time
    while word != "":
	set,word = parsechar(word)
	newdict = []	    # Add words to newdict as they are found to match
	for dw in subdict:
	    if dw[i] in set:
		newdict.append(dw)
	subdict = newdict
		
	i +=1
    return len(newdict)

def naivesolve():
    l,d,n,dict,solve = loadinput()

    for i in range(n):
	word = solve[i]
	nm = indict_count(dict,word)
	print "Case #%d: %d"%(i+1,nm)

naivesolve()
