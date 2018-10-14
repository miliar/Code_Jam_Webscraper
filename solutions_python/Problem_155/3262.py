import re
import os.path
import glob   



fnr=os.getcwd()+'\\Input.txt'
fnw=os.getcwd()+'\\Output.txt'

if (os.path.isfile(fnr)):
        
        fp = open(fnr, 'r')
        fw = open(fnw, 'w')
        line = fp.readline()
        n=int(line)
        result=[]
        for i in range(0, n):
                line = fp.readline()
                token = line.split()
                nn=int(token[0])
                nos=list(token[1])
                inv=0                
                p=int(nos[0])
                for j in range(1, nn+1):
                        s=int(nos[j])
                        if((p+inv)<j):
                                if(s > 0):
                                        inv=inv+(j-(p+inv))
                                
                        p=p+s
                result.append(inv)
        print result
        l=len(result)
        for k in range(0, l):
                v=k+1
                fw.write('Case #%s:'%v)
                fw.write(' %s\n'%result[k])
                
        
        fp.close()
        fw.close()
