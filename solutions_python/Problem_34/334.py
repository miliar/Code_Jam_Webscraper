test = """3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc"""

test = file( "A-small-attempt0.in" ).read()

v = test.split( "\n" )
L, D, N = map( int, v[0].split( " " ) )

samples = []
for i in range( D ):
    samples.append( v[i + 1] )

rules = []
import re
for i in range( N ):
    rules.append( re.compile( v[i + D + 1].replace( "(", "[" ).replace( ")", "]" ) ) )

for k in range( len( rules ) ):
    r = rules[k]
    total = 0
    for i in samples:
        if r.match( i ):
            total += 1

    print "Case #%s: %s" % ( k + 1, total )

#rules = []
#for i in range( N ):
#    offset = 0
#    pure_rule = v[i + 1 + D]
#    rule = []
#    for j in range( L ):
#        if pure_rule[j + offset] == '(':
#            right = pure_rule.index( ")", j + offset )
##            print j, offset, right, pure_rule, rule
#            rule.append( pure_rule[j + offset + 1:right] )
#            offset = right - j
#        else:
#            rule.append( pure_rule[j + offset] )
#
#
#    rules.append( rule )
#
#print samples, rules
#
#root = {}
#childs = [root]
## build rule trees
#for r in rules:
#    for k in range( L ):
#        for s in r[k]:
#            for c in childs:
#                if childs[]


