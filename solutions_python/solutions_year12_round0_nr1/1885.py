import ast,sys
w = {}
k = '''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv'''
v = '''our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up'''
i = ''.join(k.split())
a = ''.join(v.split())

for l, m  in zip(i , a) :
    if l not in w :
        w[l] = m

#spaces q/z additional work too

t = int(raw_input(''))
for h in range(t) : 
    s = raw_input('')
    print('Case #{0}: '.format(h+1)),
    for pi in s :
        if pi in w : 
            sys.stdout.write(w[pi])
        else :
            print pi,
    print
print
    
    

