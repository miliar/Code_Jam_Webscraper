import sys

# https://code.google.com/codejam/contest/3264486/dashboard

def tidy_numbers(N):
    decimal = 1
    while int(N/(10*decimal)):
        # print int(N/(10*decimal))%10, int(N/decimal)%10
        if int(N/(10*decimal))%10 > int(N/decimal)%10:
            N = int(N/(10*decimal))*10*decimal - 1
        decimal *= 10
    return N

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as f:
        T = int(f.readline().strip())
        for i in range(T):
            N = int(f.readline().strip())
            print "Case #"+str(i+1)+": "+str(tidy_numbers(N))
