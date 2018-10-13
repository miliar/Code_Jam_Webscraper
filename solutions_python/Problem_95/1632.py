'''
Created on 2012-4-14

@author: mzh.li
'''

if __name__ == '__main__':
    gt = '''ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc
     rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'''
    
    gt = ''.join(gt.strip().split())
    nt = '''our language is impossible to understand there are twenty six factorial possibilities 
    so it is okay if you want to just give up'''
    nt = ''.join(nt.strip().split())
    
    maps = {}
    if len(gt) != len(nt):
        print("length is not consistency")
    if len('abcdefghijklmnopqrstuvwsyz') != 26:
        print("erro letters")
    for a in 'abcdefghijklmnopqrstuvwsyz':
        if a not in nt:
            print(a, "erro letters---")
            
    for i in range(0,len(gt)):
        maps[gt[i]] = nt[i]
    
    maps['q'] = 'z'
    maps['z'] = 'q'
    
    with open('A-small-attempt1.in', 'r') as fi, open('Asmall.output','w') as fo:
        lines = int(fi.readline());
        for i in range(1,lines + 1):
            l = fi.readline();
            s = ''
            for a in l:
                if maps.get(a):
                    s += maps[a]
                else:
                    s += a
            fo.write("Case #%d: %s"%(i,s))