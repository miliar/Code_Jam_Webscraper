from sys import stdin

samples = [('ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand'),
           ('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities'),
           ('de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up')]

googlerese = {'y':'a', 'e':'o', 'q':'z', '\n':''}
normal = {'a':'y','o':'e', 'z':'q'}

for sample in samples:
    for i in range(len(sample[0])):
        googlerese[sample[0][i]] = sample[1][i]
        normal[sample[1][i]] = sample[0][i]

##print len('abcdefghijklmnopqrstuvwxyz')
##for letter in 'abcdefghijklmnopqrstuvwxyz':
##    if not googlerese.has_key(letter):
##        print 'NOT IN GOOGLERESE ',letter
##    if not normal.has_key(letter):
##        print 'NOT IN NORMAL',letter

googlerese['z'] = 'q'    

num_cases = int(stdin.readline())
for case_index in xrange(1, num_cases+1):
    encoded = stdin.readline().strip()
    decoded = ''
    for i in range(len(encoded)):
        decoded+=googlerese[encoded[i]]
    print "Case #" + str(case_index) + ": " + decoded
