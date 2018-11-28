def main():
    outfile = open('output.txt', 'w')
    infile = open('input.txt', 'r')

    n = int(infile.readline())
    for i in range(n):
        nums = infile.readline().split()
        C = float(nums[0])
        F = float(nums[1])
        X = float(nums[2])
        print '%.7f' % cookieTime(C, F, X)
        outfile.write('Case #' + str(i+1) + ': ' + '%.7f' % cookieTime(C, F, X) + '\n')

    infile.closed
    outfile.closed

def cookieTime(C, F, X):
    print C, F, X
    count = 0.0
    time = 0.0
    rate = 2.0
    
    while count < X:
        if ((X-count) < C): #if faster to wait
            time += (X-count)/rate
            count = X
        elif count < C: #if unable to buy a barn
            time += (C-count)/rate
            count += (C-count)
        if ((X+C-count)/(rate+F)) < ((X-count)/rate): #if faster to buy a barn
            count -= C
            rate += F
        else: #my if statements should be better...
            time += (X-count)/rate
            count = X
            
    return time

if __name__ == "__main__":
    main()
    
"""
2 cookies/sec base
+ F cookies/sec
Comsume C cookies to increment F
X cookies final number
"""
