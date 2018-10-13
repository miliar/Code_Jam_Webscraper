import sys

w = "welcome to code jam"
l = len(w)

def main(argv):
    ifilename = argv[1]
    ofilename = argv[2]
    ifile = open(ifilename, 'r')
    numlines = ifile.readline()
    ofile = open(ofilename, 'w')
    numlines = numlines.strip();
    num = int(numlines)
    
    for i in range(num):
        a = ifile.readline().strip()
        count = findNumber(a, 0, 0)
        s = '%04d' % count
        ofile.write("Case #"+str(i+1)+": "+s+"\n")
    
    ifile.close()
    ofile.close()
    
def findNumber(string, i, count):
    if i == l:
        #print "================================="
        return count+1
    else:
        #print "-----"
        #print "letter: "+str(i)+" - "+w[i]
        end = len(string) - (l-i) + 1
        #print "string: "+string
        #print "end: "+str(end)
        nexti = string.find(w[i], 0, end)
        while nexti != -1 and count < 9999:
            count = findNumber(string[nexti+1:], i+1, count)
            nexti = string.find(w[i], nexti+1, end)
        return count
    
if __name__ == '__main__':
    main(sys.argv)