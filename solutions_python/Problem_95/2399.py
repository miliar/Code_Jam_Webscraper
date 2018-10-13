
mapper = {'\n':'',' ':' ','a' : 'y', 'c' : 'e', 'b' : 'h', 'e' : 'o', 'd' : 's', 'g' : 'v', 'f' : 'c', 'i' : 'd', 'h' : 'x', 'k' : 'i', 'j' : 'u', 'm' : 'l', 'l' : 'g', 'o' : 'k', 'n' : 'b', 'p' : 'r', 's' : 'n', 'r' : 't', 'u' : 'j', 't' : 'w', 'w' : 'f', 'v' : 'p', 'y' : 'a', 'x' : 'm','q':'z','z':'q'} # Map a google letter to a real letter

# Define a main() function
def main():
    gooLang = open("A-small-attempt1.in","r")
    lineNum = 1
    first = 1
    for gooLine in gooLang:
	if(not first):
	    print "Case #"+ str(lineNum)+": " + changeLine(gooLine)
	    lineNum= lineNum + 1
	first =0
	

def changeLine(aLine):
    transLine = ""
    for i in range(len(aLine)):
	transLine += mapper[aLine[i]]
    return transLine


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
