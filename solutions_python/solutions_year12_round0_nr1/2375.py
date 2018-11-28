# problem a

translation_tips = [('ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand'),
    ('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities'),
    ('de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up')]

dictionary = {'y': 'a', 'e': 'o', 'q':'z', 'z': 'q'}

for tip in translation_tips:
    g = tip[0]
    t = tip[1]
    
    for i in range(len(g)):
        if g[i] == ' ':
            continue
        dictionary[g[i]] = t[i]

keys = dictionary.keys()
keys.sort()
keys = set(keys)
missing = set('abcdefghijklmnopqrstuvwxyz') - keys
#print 'Missing:', missing
missing_2 = set('abcdefghijklmnopqrstuvwxyz') - set(dictionary.values())
#print 'Missing2', missing_2
#print 'Looks like our basic dictionary is ', keys

def translate(g):
    n = ''
    for c in g:
        if c == ' ':
            n += ' '
        else:
            n += dictionary[c]
    return n

if __name__ == '__main__':
    n_tests = int(raw_input())

    for i in range(1, n_tests+1):
        string_g = raw_input()
        
        print 'Case #%d: %s' % (i, translate(string_g))