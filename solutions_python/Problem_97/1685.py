'''
Created on Apr 14, 2012

@author: jpsantos
'''



def roll(string):
    ll = list(string)
    lll = []
    lll.append(ll[-1])
    for c in ll[0:-1]:
        lll.append(c)
    return ''.join(str(n)for n in lll)


def process(small, big):
    first = small
    map = {}
    count = 0;
    while first <= big:
        s_first = str(first)
        tam = len(s_first)
        for i in range(tam):
            rolled = roll(s_first)
            i_rolled = int(rolled)
            if(i_rolled>first and i_rolled<=big and rolled[0] !='0'):
                key = '(%s,%s)' %(first,rolled)
                if(key not in map):
                    count=count+1
                    #print key
                    map[key] = True
                #else:
                    #print "Fuck! %s" % key 
            s_first = rolled
        first=first+1
    return count 

input = open("smallC.txt","r")
output = open("out_small_c.txt","w")

tests = int(input.readline())
for t in range(tests):
    line = input.readline()
    numbers = line.split()
    found = process(int(numbers[0]), int(numbers[1]))
    out = "Case #%d: %d\n" %(t+1,found)
    output.write(out)
output.close()       