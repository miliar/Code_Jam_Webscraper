fname='A-small-attempt0.in'
fixed_mapping = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
lines=[]
f=open(fname)
N=int(f.readline())
for line in range(N):
    lines.append(f.readline().strip())
lines = [x.lower() for x in lines]
##mapping= {}
##mapping['z'] = 'q'
##mapping['q'] = 'z'
##output_given = ["our language is impossible to understand", \
##"there are twenty six factorial possibilities",\
##"so it is okay if you want to just give up"]
##for li in range(len(lines)):
##    for i in range(0, len(lines[li])):
##        mapping[lines[li][i]] = output_given[li][i]
##print N, lines
##print
##print len(mapping), mapping
##for k, v in sorted(mapping.iteritems()):
##    print k,v,ord(k), ord(v),-ord(k)+ ord(v)
f.close()
o=open(fname +'out.txt', "w")
for li in range(len(lines)):
    str=''
    for i in range(0, len(lines[li])):
        str = str + fixed_mapping[lines[li][i]]
    o.write( 'Case #{0}: {1}\n'.format(li+1, str))
o.close()
