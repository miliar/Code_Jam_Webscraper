#Google Code Jam 2012
#Qualification Round
#Problem A


def file2gen(name):
    f=open(name,'r')
    text=f.read()
    f.close()
    return (line for line in text.splitlines())

#In the three example sentences, we have translations for most English letters
#We miss q and z. The text says z->q. Only remaining unaccounted is z->q.
#We use this to build a Googlerese to English translation table.

table=str.maketrans('''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jvqz''',
                    '''our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give upzq''')

def output(gen,out):
    f=open(out,'w')
    cases=int(next(gen))
    for i in range(cases):
        english=next(gen).translate(table)
        f.write('Case #'+str(i+1)+': '+english+'\n')
    f.close()

def run(infile,outfile): output(file2gen(infile),outfile)

if __name__=='__main__': run('A-small-attempt0.in', 'outA.txt')
        
