import sys
input = sys.stdin.read()

ar = input.split("\n")
cases = ar[0];
ar=ar[1:]

for i in range(len(ar)):
    [max,strr] = ar[i].split(" ")
    added=0
    standing=0
    char = list(strr)
    for j in range(len(char)):
        if standing<j:
            added +=j-standing
            standing +=j-standing
        standing +=int(char[j])
    print "Case #"+str(i+1)+": "+str(added)
    
