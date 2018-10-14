import sys, math

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def count_fair_squares(a,b):
    low = int(math.ceil(math.sqrt(a)))
    high = int(math.floor(math.sqrt(b))) + 1
    count = 0
    i = low
    while i < high:
        if is_palindrome(i) and is_palindrome(i**2):
            count += 1
        i += 1
    return count

def main():
    file = open(sys.argv[1],'r')
    T = int(file.readline().strip())
    for i in range(T):
        params = file.readline().strip().split(' ')
        A = int(params[0])
        B = int(params[1])
        print "Case #%d: %d" % (i+1, count_fair_squares(A,B))
    file.close()

if __name__ == '__main__':
    main()