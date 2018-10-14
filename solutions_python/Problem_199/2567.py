def flipper(x):
    if x=='+':
        return '-'
    else:
        return '+'
        
def check(string):
    for i in xrange(len(string)):
        if string[i]=='-':
            return False
    return True
def pancake(string, k):
    counter=0
    for i in xrange(len(string)-k+1):
        if string[i]=='-':
            tmp=''
            for j in xrange(k):
                tmp+=flipper(string[i+j])
            string = string[:i]+tmp+string[i+k:]
#            print string
            counter+=1

    if check(string):
        return counter
    else:
        return 'IMPOSSIBLE'
            
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    string, k = [s for s in raw_input().split(" ")]
    
    print "Case #{}: {}".format(i, pancake(string, int(k)))
    # check out .format's specification for more formatting options