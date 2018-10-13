import sys
import string

if __name__=='__main__':
    mapping = {}
    refInputString = "ejp mysljylc kd kxveddknmc re jsicpdrysi" + \
        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" + \
        "de kr kd eoya kw aej tysr re ujdr lkgc jv"
    refOutputString = "our language is impossible to understand" +\
        "there are twenty six factorial possibilities" +\
        "so it is okay if you want to just give up"
    for i in range(len(refInputString)):
        mapping[refInputString[i]] = refOutputString[i]
    mapping['z'] = 'q'
    keys = string.lowercase
    vals = string.lowercase
    for k in mapping.keys():
        keys = keys.replace(k, '')
        vals = vals.replace(mapping[k], '')
    mapping[keys] = vals
    infile = open(sys.argv[1])
    lines = []
    output = []
    infile.readline()
    for line in infile:
        lines.append(line.rstrip())
    caseNum = 1
    for line in lines:
        output.append("Case #" + str(caseNum) + ": " + 
                      ''.join(mapping[s] for s in line))
        caseNum += 1
    out = open('out.out', 'w')
    for line in output:
        out.write(line + '\n')
