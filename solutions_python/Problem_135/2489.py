N = input()
for n in range(1, N+1):
    c = input()
    for i in range(c-1): raw_input()
    r1 = raw_input().split()
    for i in range(4-c): raw_input()
    
    
    c = input()
    for i in range(c-1): raw_input()
    r2 = raw_input().split()
    for i in range(4-c): raw_input()
    
    c = 0; s = 0
    for i in range(4):
        if r2.count(r1[i]):
            s += 1
            c = r1[i]
    
    st = c
    if not s:
        st = "Volunteer cheated!"
    elif s>1:
        st = "Bad magician!"
    
    print "Case #%d: "%(n)+st