
#decoder
a1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
b1 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
c1 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"

a2 = "our language is impossible to understand"
b2 = "there are twenty six factorial possibilities"
c2 = "so it is okay if you want to just give up"

rosetta = {}
for (encrypted,unencrypted) in [(a1,a2),(b1,b2),(c1,c2)]:
    print (encrypted, unencrypted)
    for i in range( 0, len(encrypted) ):
        if encrypted[i] in rosetta and rosetta[encrypted[i]] != unencrypted[i]:                        
            print "ERRROR!"
            print encrypted[i] + ": "  + unencrypted[i]        
        rosetta[encrypted[i]] = unencrypted[i]
        #print encrypted[i] + ": "  + unencrypted[i]

rosetta['y'] = 'a'
rosetta['e'] = 'o'
rosetta['q'] = 'z'
rosetta['z'] = 'q'

rosetta[' ']=' '
rosetta['\n']=''

for k in rosetta:
    print k + " : " + rosetta[k]

def solve(f):
    line = f.readline()
    res = ""
    for char in line:
        res += rosetta[char]
    return res

def main():
    with open('A-small-attempt1.in','r') as f:        
        numCases = int(f.readline())
        for i in range(1, numCases+1):
            output = solve(f)
            print "Case #%d:"  % i, output
            
main()