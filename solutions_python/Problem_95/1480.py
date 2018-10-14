mapping = {' ': ' ', 'y': 'a', 'e': 'o', 'q': 'z'}
mapping['z'] = 'q' # found by bijective property
for j in xrange(3):
    x = raw_input(""); # encoded
    y = raw_input(""); # decoded
    for i in xrange(len(x)):
        mapping[x[i]] = y[i];
    
print repr(mapping)

for x in "abcdefghijqlmnopqrstuvwxyz":
    print "%s -> %s" % (x, mapping.get(x, '?'))
    
for x in "abcdefghijklmnopqrstuvwxyz":
    if not x in mapping.values():
        print x, 'missing'
