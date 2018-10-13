def getmapping(instr, outstr, mapping):
    for i in range(len(instr)):
        mapping[instr[i]] = outstr[i]
    return mapping

if __name__=='__main__':
    mapping = {}
    mapping['y'] = 'a'
    mapping['e'] = 'o'
    mapping['q'] = 'z'
    mapping['z'] = 'q'
    instr = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
    outstr = 'our language is impossible to understand'
    mapping = getmapping(instr, outstr, mapping)
    instr = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
    outstr = 'there are twenty six factorial possibilities'
    mapping = getmapping(instr, outstr, mapping)
    instr = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'
    outstr = 'so it is okay if you want to just give up'
    mapping = getmapping(instr, outstr, mapping)
    if len(mapping.keys()) != 27 :
        print "***************Incomplete**********"

    fin = open("g:\\input.txt", 'r')
    fout = open("g:\\output", 'w')

    inpno = int(fin.readline())

    for i in range(inpno):
        inpline = fin.readline()
        outline = ''
        for element in inpline:
            if element <> '\n':
                outline += mapping[element]

        fout.write("Case #%d: %s\n"%(i+1, outline))
    fout.close()
    fin.close()
