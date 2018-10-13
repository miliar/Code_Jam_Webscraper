samples = {
'ejp mysljylc kd kxveddknmc re jsicpdrysi': 'our language is impossible to understand',
'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd': 'there are twenty six factorial possibilities',
'de kr kd eoya kw aej tysr re ujdr lkgc jv': 'so it is okay if you want to just give up'
}
words = {}
for i in samples.items():
    for j in range(len(i[0])):
        original = i[0][j]
        other = i[1][j]
        words[original] = other
words['z'] = 'q'
words['q'] = 'z'

N = input()

for i in range(1, N+1):
    e = raw_input()
    f = ''.join(words[j] for j in e)
    print 'Case #' + str(i) + ': ' + f
    
