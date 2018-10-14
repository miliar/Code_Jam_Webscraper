'''
Created on Apr 14, 2012

@author: diego
'''
alphabet=dict()

def train(pairs):
    for (x,y) in pairs:
        for i in range(len(x)):
            alphabet[x[i]]=y[i]
    alphabet['z']='q'
    alphabet['q']='z'

def translate(line):
    output=""
    for i in range(len(line)):
        output=output+alphabet[line[i]]
        
    return output
'''a' -> 'y', 'o' -> 'e', and 'z' -> 'q'.'''
if __name__ == '__main__':
    pairs=[("ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand"),
("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","there are twenty six factorial possibilities"),
("de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up")]
    alphabet=dict()
    train(pairs)
    file=open('input.txt')
    i=1
    lines=file.readlines()
    lines=lines[1:]
    for line in lines:
        line=line.strip('\n')
        output=translate(line)
        print "Case #" + str(i) + ": " + output
        i+=1
    pass