def StandingOvation(arr):
    psum = 0
    friends = 0
    
    for i in range(len(arr)):
        if psum + friends < i:
            friends = i - psum
        else:
            pass
        psum += arr[i]
        
    return friends

f = open("C:\Users\Owen\Documents\DEMAT\Google Code Jam\A-small-attempt0.in", "r", 0)
a = []
for line in f:
    a.append(line)
    
for i in range(int(a[0])):
    arr = []
    for j in range( int(a[i+1][0]) + 1):
        arr.append(int(a[i+1][2+j]))
    print "Case #%s: %d" %(i+1, StandingOvation(arr))