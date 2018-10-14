def gettable():

    example = [("ejp mysljylc kd kxveddknmc re jsicpdrysi",  "our language is impossible to understand"),
               ("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities"),
               ("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up")]

    table = dict()

    for crypt, ori in example:
        for i in xrange(len(ori)):
            table[crypt[i]] = ori[i]

    table['z'] = 'q'
    table['q'] = 'z'

    return table

def main():
    table = gettable()
    
    inp  = open("A-small-attempt1.in","r");
    outp = open("output.txt","w");

    for t in xrange(int(inp.readline())):
        outp.write("Case #%d: %s\n" % (t+1, "".join(map(lambda x: table[x],inp.readline()[:-1]))))
    

if __name__ == "__main__":
    main()
