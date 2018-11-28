import sys

convert = {'a':'y', 'o':'e', 'z':'q'}
revconvert = {'y':'a', 'e':'o', 'q':'z'}


line1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
line2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
line3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"

ans1 = "our language is impossible to understand"
ans2 = "there are twenty six factorial possibilities"
ans3 = "so it is okay if you want to just give up"


for i in range( len(line1) ):
    convert[ line1[i] ] = ans1[i]

for i in range( len(line2) ):
    convert[ line2[i] ] = ans2[i]

for i in range( len(line3) ):
    convert[ line3[i] ] = ans3[i]

convert['q'] = 'z'

#print len(convert)

#for k,v in sorted(convert.iteritems()):
#    print "%s: %s" % (k,v)

#sys.stdout.write('a')
#sys.stdout.write('a')

file_name = ""

if (len(sys.argv) > 1):
    file_name = sys.argv[1]
else:
    file_name = "input.txt"

input = open(file_name, 'r')
output = open('output.txt', 'w')
cases = int(input.readline().strip())

for case in range(cases):
    line = input.readline().strip()
    sys.stdout.write( "Case #%s: " % str(case+1) )
    output.write( "Case #%s: " % str(case+1) )

    for x in line:
        sys.stdout.write( convert[x] )
        output.write( convert[x] )
    print ""
    output.write( "\n" )


input.close()
output.close()
