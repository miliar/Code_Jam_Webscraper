'''
Created on Mar 20, 2012

@author: Wen
'''
if __name__ == '__main__':
    s1 ={ 0: "ejp mysljylc kd kxveddknmc re jsicpdrysi",
          1:"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
          2:"de kr kd eoya kw aej tysr re ujdr lkgc jv",
     }
    s2= { 0:"our language is impossible to understand",
          1:"there are twenty six factorial possibilities",
          2:"so it is okay if you want to just give up"
     }

    d={}
    for i in range(0,3):
        x = s1[i]
        e = s2[i]
        for i in range(0,len(x)):
            d[x[i]]=e[i]
    d['z']='q'
    d['q']='z'
    d['\n']='\n'
    
    fi = open ( 'C:/Users/Wen/Desktop/codejam/1/q1.in' , 'r' )
    fo = open ( 'C:/Users/Wen/Desktop/codejam/1/q1.out' , 'w' )
    size = int( fi.readline() ) 
    
    for j in range(0,size):
        e = []
        x = fi.readline()
        e = [ d[k] for k in x ]
        fo.write( "Case #"+str(j+1)+': ') 
        fo.write( "".join(e) )            
    
    print("Done")
    
    
