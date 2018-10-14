from string import maketrans
someFile = open("A-small-attempt3.in")
numOfLines=int(someFile.readline())
hugeAssDict={'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}
someString="" #too lazy to replace these to fix my mistake
otherString=""
for x,y in hugeAssDict.iteritems():
    someString=someString+x
    otherString=otherString+y
num=1
someLine=""
trantab=maketrans(someString,otherString)
for line in someFile:
    line=line.replace('\n','')
    print "Case #"+str(num)+": "+line.translate(trantab)
    num+=1