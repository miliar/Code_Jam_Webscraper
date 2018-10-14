import time

debug = False

def substr(string):
    j=1
    a=set()
    while True:
        for i in xrange(len(string)-j+1):
            a.add(string[i:i+j])
        if j==len(string):
            break
        j+=1
        #string=string[1:]
    return a

def cgroups(iterable,minlen):
    s = tuple(iterable)
    for size in range(1, len(s)+1):
        for index in range(len(s)+1-size):
            str = iterable[index:index+size]
            if len(str) >= minlen:
                    yield str
                    
vowels = ['a','e','i','o','u']

tStart = time.time()

fname = "A-small-attempt0"

fin = open(fname+".in","r")
flines = fin.readlines()
fin.close()

fout = open(fname+".out","w")

numcases = int(flines[0])

for icase in range(1,numcases+1):
   
    line = flines[icase].split()
    word = line[0]
    slen = int(line[1])

    word2 = [0 if i in vowels else 1 for i in word]
    result = 0
    for item in cgroups(word2,slen):
        #print item
        cons = 0
        for x in item:
            if x == 1:
                cons += 1
                if cons == slen:
                    result += 1
                    break
            else:
                cons = 0

    outstr = "Case #%d: %d" % (icase,result)
    print outstr
    fout.write("%s\n" % (outstr))
    
fout.close()

tEnd = time.time()

print "run time = %s" % (str((tEnd - tStart)))

    

            
