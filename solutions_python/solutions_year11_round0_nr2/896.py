import sys
import re
sys.stdin.readline()
case = 0
while 1:
    line = sys.stdin.readline()
    if not line:
        break
    parts = line.split( ' ' )
    invoke = parts[-1]
    c = 1
 
    combines = {}
    opposed = {}
    for i in range( 1, int(parts[0])+1 ):
        combines[re.compile(parts[i][0:2]+'$')] = parts[i][-1]
        combines[re.compile(parts[i][1:2]+parts[i][0:1]+'$')]= parts[i][-1]
        c+=1
    for i in range( c+1, c+1+int(parts[c]) ):
        opposed[re.compile("^.*" + parts[i][0:1] + ".*?" + parts[i][1:2] + "$")]= ""
        opposed[re.compile("^.*" + parts[i][1:2] + ".*?" + parts[i][0:1] + "$")]= ""

    elements = ""
    for i in range(0,len(invoke)-1):
        # check for combine
        elements += invoke[i]
        for ( k, v ) in combines.iteritems():
            elements = k.sub(v,elements)
        for ( k, v ) in opposed.iteritems():
            elements = k.sub(v,elements)
    case += 1
    print "Case #%d: [%s]" % ( case, ', '.join(list(elements)))
