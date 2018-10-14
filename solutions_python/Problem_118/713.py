limit = 10000001
numbers = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804,
            44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401,
            121242121, 123454321, 125686521, 400080004, 404090404, 10000200001,
            10221412201, 12102420121, 12345654321, 40000800004, 1000002000001,
            1002003002001, 1004006004001, 1020304030201, 1022325232201,
            1024348434201, 1210024200121, 1212225222121, 1214428244121,
            1232346432321, 1234567654321, 4000008000004, 4004009004004}

def palindrome(a):
    reverse = ""
    for j in range(0, len(a)):
        reverse += a[len(a) - j - 1]
    return a == reverse

def calc():
    for i in range(1, limit):
        if palindrome(str(i)) and palindrome(str(i * i)):
            fair[i * i] = True

def main():
    t = int(raw_input())
    for i in xrange(t):
        cnt = 0
        input = raw_input()
        line = input.split(" ")
        a = int(line[0])
        b = int(line[1])
        for j in numbers:
            if j >= a and j <= b:
                cnt += 1
        print "Case #%s: %s" % (i + 1, cnt)
    
main()
