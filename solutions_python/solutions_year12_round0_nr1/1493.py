__author__ = 'JJ'


# a -> y
# o -> e
# z -> q
# a zoo -> y qee

i = ['ejp mysljylc kd kxveddknmc re jsicpdrysi',
     'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
     'de kr kd eoya kw aej tysr re ujdr lkgc jv']

j = ['our language is impossible to understand',
     'there are twenty six factorial possibilities',
     'so it is okay if you want to just give up']

transdict=[]
for num in range(3):
    transdict.append(dict(
        [(i[num][x], j[num][x]) for x in range(len(i[num]))]
        ))

final = transdict[0]
final.update(transdict[1])
final.update(transdict[2])
final.update({'q':'z', 'z':'q'})
#transdict=final

#transdict = dict((v,k) for k,v in transdict.iteritems())

## read in file
with open(r'C:\GCJ\in.txt', 'r') as thefile:
    temp = thefile.readlines()

def trans(a):
    return final[a]

temp.pop(0)

output = []
for line in temp:
    output.append(''.join(map(trans, line.strip())))

# out
with open('C:\GCJ\out.txt', 'w') as outputfile:
    outputfile.write('\n'.join(["Case #%s: %s" % (index + 1, content) \
                                for index, content in \
                                enumerate(output)]))
