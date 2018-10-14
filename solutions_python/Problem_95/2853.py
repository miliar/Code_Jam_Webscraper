'''
Created on 15 Apr 2012

@author: firman
'''

if __name__ == '__main__':
    filename = "A-small-attempt0"
    N = 0
    
    string = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y e q z\n';
    answer = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a o z q\n';
    
    d = {}
    
    for key,value in enumerate(string):
        d[value] = answer[key]
        
    #out = "".join([d[a] for a in string ])
    
    f = open(filename+".in","r")
    fout = open(filename+".out","w")
    
    N = int(f.readline())
    for n in range (N):
        i = f.readline()
        o = "".join([d[a] for a in i ]) 
        fout.write("Case #%i: %s"%(n+1,o))
    
    f.close()
    fout.close()