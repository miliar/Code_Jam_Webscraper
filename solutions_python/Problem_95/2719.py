import string

table = string.maketrans( 'ynficwlbkuomxsevzpdrjgthaq ',  
                          'abcdefghijklmnopqrstuvwxyz ' )
#print 'ejp mysljylc kd kxveddknmc re jsicpdrysi'.translate(table)
#print 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'.translate(table)
#print 'de kr kd eoya kw aej tysr re ujdr lkgc jv'.translate(table)
p = input()
count = 1
while count <= p:
  line = raw_input()
  print "Case #{0}: {1}".format(count, line.translate(table))
  count += 1
