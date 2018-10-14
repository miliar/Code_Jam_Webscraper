def test(n):
    for i in range(len(n) - 1):
        if n[i] < n[i+1]:
            return False
    return True

def check_tidy(n):
    N = [int(x) for x in str(n)][::-1]
    if len(n) == 1:
        return n
    while True:
        for i in range(len(N) - 1):
            current = N[i]
            next = N[i + 1]
            # print N, current, next
            if current < next:
                for x in range(i + 1):
                    N[x] = 9
                N[i + 1] -= 1
        if test(N):
            return int("".join([str(x) for x in N[::-1]]))
        
    
            
    
f = open("B-large.in", "r").readlines()
T = f.pop(0).strip()
x = 1
output = open("tidy.txt", "w")
for line in f:
    N = line.strip()
    y = check_tidy(N)
    print "Case #%s: %s" % (x, y)
    
    output.write("Case #%s: %s\n" % (x, y))
    x += 1
output.close()
    