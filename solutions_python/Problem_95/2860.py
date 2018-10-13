x = open('1input').readlines()

mapping = {}

for j in xrange(len(x) / 2):
    a, b = x[2 * j], x[2 * j + 1]

    for i in xrange(len(a)):
        mapping[a[i]] = b[i]

print '{'
for key, value in mapping.items():
    print '\t\'%s\': \'%s\',' % (key, value)
print '}'
