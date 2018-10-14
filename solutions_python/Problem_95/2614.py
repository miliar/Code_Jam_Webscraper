'''
Created on Apr 13, 2012

@author: gmaztak
'''
def createDict():

    l = "qzaejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
    t = "zqyour language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
    
    d = {}
    for i in range(l.__len__()):
        d[l[i]] = t[i]
    keys = d.keys()
    keys.sort()
    for k in keys:
        print "key: " + k + " = " + d[k]
    return d

def translateLine(d,line):
    retString = ""
    for c in line:
        if c == '\n': continue
        retString += d[c]
    return retString
def crunch(file1, file2, d):
    f = open(file1, 'r')
    f2 = open(file2, 'w')
    i =0
    lines = f.readlines()
    for line in lines:
        if i == 0:
            i =1
            continue
        s = translateLine(d, line)
        f2.write("Case #%d: %s\n"%(i,s))
        #print "Case #%d: %s"%(i,s)
        i+=1
def main():
    d = createDict()
    crunch('GoogleReese.txt', 'GoogleReeseOutput.txt', d)
    
if __name__ == "__main__": main()