'''
Created on Apr 10, 2015

@author: RaquelAraujo
'''
def extrapeople(T,numpeople):
    stand=0
    extra = 0
    for i,n in enumerate(numpeople):
        if int(n)>0 and stand<i:
            extra += i-stand
            stand += i-stand
        stand += int(n)   
            
    return extra

f = open("A-small-attempt1.in")
for n, line in enumerate(f):
    if n>0:
        info = line.split()
        print("Case #%d: "+str(extrapeople(info[0],info[1]))) %(n)   
