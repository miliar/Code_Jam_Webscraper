'''
Created on Apr 14, 2012

@author: shelajev
'''



def make_dict(texts):
    d = {}
    b = {}
    for k, v in texts.items():
        for i in range(len(k)):
            d[k[i]] = v[i]
            b[v[i]] = k[i]
    return d, b


def solve(d, line):
    l = [0] * len(line)
    for i in range(len(line)):
        l[i] = d[line[i]]
    return ''.join(l)


if __name__ == '__main__':
    d,b = make_dict({'ejp mysljylc kd kxveddknmc re jsicpdrysi':'our language is impossible to understand',
                   'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd':'there are twenty six factorial possibilities',
                   'de kr kd eoya kw aej tysr re ujdr lkgc jv':'so it is okay if you want to just give up'})
    
    d['q'] = 'z'
    d['z'] = 'q'
    first = True
    i = 1
    for line in file('A-small-attempt0.in').readlines():
        if first:
            first = False
            continue
        print 'Case #%s: %s' % (i, solve(d, line.rstrip()))
        i+=1
    
    
            
        

    