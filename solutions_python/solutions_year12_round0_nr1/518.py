import io
inFileName = 'small'
outFileName = 'smallout'
dict = {} 
s = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
s1 ="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
i = 0
for c in s:
    dict[c] = s1[i]
    i = i + 1
dict['y'] = 'a'
dict['e'] = 'o'
dict['q'] = 'z'
dict['z'] = 'q'
dict['\n'] = '\n'


fin = open(inFileName, 'r')
fout = open(outFileName, 'w')

j = 0
for line in fin:
    if (j > 0):
        eng = ''    
        for c in str(line):
            eng = eng + dict[c]         
        fout.write('Case #' + str(j) + ': ' + eng)        
    j = j + 1
fin.close()    
fout.close()     
    		
