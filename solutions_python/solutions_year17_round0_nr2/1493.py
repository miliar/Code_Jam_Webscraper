T = int(raw_input())

def notTidy(s):
    largest = 0
    for i in range(len(s)):
        if int(s[i]) < largest:
            return True
        else:
            largest = max(int(s[i]), largest)
    return False
        
for case in range(T):
    N = raw_input()
    while notTidy(N):
        largest = 0
        i = 0
        while i < len(N):
            if int(N[i]) >= largest:
                largest = max(int(N[i]), largest)
            else:
                delta = int( "1" + N[i:len(N)]) - int( ''.join(["9" for _ in range(len(N) - i)]))
                N = str( int(N) - delta)
            i = i + 1
    print "Case #" + str(case+1) + ": " + str(N)
        




