import sys

inputfile = sys.argv[1]
sys.stdin = open(inputfile,"r")

T = int(raw_input())

for i in xrange(T):
    inputline = raw_input().split()

    combos = {}
    opposed = []

    curIndex = 0
    C = int(inputline[curIndex])
    curIndex += 1

    for j in xrange(curIndex,C+curIndex):
        combos[inputline[j][:2]] = inputline[j][2]
        combos[inputline[j][:2][::-1]] = inputline[j][2]

    curIndex += C
    D = int(inputline[curIndex])
    curIndex += 1

    for j in xrange(curIndex,D+curIndex):
        opposed.append(inputline[j])
        opposed.append(inputline[j][::-1])

   # print "combos",combos
    #print "opposed",opposed

    curIndex += D
    cmds = list(inputline[curIndex+1])

    elements = []
    for j in cmds:
        elements.append(j)
#        print "before:",elements
        if len(elements) >= 2:
            suffix = ''.join(elements[-2:])
            if suffix in combos:
 #               print "new combo!"
                new = combos[suffix]
                del elements[-2:]
                elements.append(new)
            for s in opposed:
                if s[0] in elements and s[1] in elements:
  #                  print "opposed with %s" % s
                    elements = []
                    break

#        print "after:",elements
    sys.stdout.write("Case #"+str(i+1)+": [")
    for e in xrange(len(elements)):
        el = elements[e]
        if e > 0:
            sys.stdout.write(", "+el)
        else:
            sys.stdout.write(el)
    print "]"
