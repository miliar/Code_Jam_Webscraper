f = open('input.txt', 'r')
out = open('output.txt', 'w') 
n = int(f.readline())



def solve(n):
    res = ''
    last = 10
    while n > 0:
        next = n%10
        if next <= last:
            res = str(next) + res
            last = next
        else:
            res = len(res)*'9'
            res = str(next-1) + res
            last = next - 1
        n /= 10

    return int(res)


def check(n):
    last = 10
    while n > 0:
        next = n%10
        if next > last:
            return False
        n /=  10
        last = next

    return True
        
for i in xrange(n):
    n = int(f.readline())
    ans = solve(n)
    out.write("Case #%d: %s\n" % (i+1, ans))



    
