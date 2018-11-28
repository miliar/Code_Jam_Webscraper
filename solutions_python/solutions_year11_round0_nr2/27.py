import sys

     
numcases = int(sys.stdin.readline())
for casenumber in xrange(1,numcases+1):
    line = sys.stdin.readline().rstrip("\r\n")
    line_elems = line.split(" ")

    c = int( line_elems[0] )
    line_elems = line_elems[1:]
    unparsed_combinations = line_elems[:c]
    line_elems = line_elems[c:]

    combinations = {}
    for seq in unparsed_combinations:
        a = seq[0]
        b = seq[1]
        result = seq[2]

        combinations[a+b] = result
        combinations[b+a] = result

    d = int( line_elems[0] )
    line_elems = line_elems[1:]
    unparsed_oppositions = line_elems[:d]
    line_elems = line_elems[d:]
    oppositions = {}
    for seq in unparsed_oppositions:
        a = seq[0]
        b = seq[1]
        oppositions[a+b] = 1
        oppositions[b+a] = 1

    n = int( line_elems[0] )
    line_elems = line_elems[1:]
    invocations = line_elems[:n][0]
    # line_elems = line_elems[d:] 

    elements = []
    for invocation in invocations:
#        print "before", elements
#        print "playing ", invocation

        elements.append(invocation)

        combined = True
        while len(elements) >= 2 and combined:
            a = elements[len(elements)-1]
            b = elements[len(elements)-2]
            if (a+b) in combinations:
                elements = elements[:len(elements)-2]
                elements.append(combinations[a+b])
            else:
                combined = False

        if len(elements) >= 2 and not combined:
            invocation = elements[len(elements)-1]
            for element in elements:
                if (element+invocation) in oppositions:
                    elements = []


    print "Case #%d: [%s]" % (casenumber, ", ".join(elements))

