import sys

fairs = set() 

def palindrome(s):
    l = 0
    r = len(s)-1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

def check(s, add):
    v = long(s)
    v = v*v
    if palindrome(str(v)):
        global fairs
        fairs.add(v)
        add.append(s)

def gen(length):
    global fairs
    fairs.add(1L)
    fairs.add(4L)
    fairs.add(9L)
    ls = ["", "0", "1", "2"]

    for i in xrange(2, length):
        print i, " ", len(ls)
        add = []
        if i*2-1 > length:
            break
        for x in ls:
            if (i-len(x))%2 == 1:
                continue
            t = (i-len(x))/2
            for j in xrange(1, t+1):
                s = "1"*j + "0"*(t-j) + x + "0"*(t-j) + "1"*j
                check(s, add)
            s = "2" + "0"*(t-1) + x + "0"*(t-1) + "2"
            check(s, add)

        ls = ls + add

def gen_fairs():
    gen(100)

    ls = map(lambda x: str(x), sorted(list(fairs)))
    print len(fairs)
    f = open("fairs.txt", "w")
    f.write("\n".join(ls))
    f.write("\n")
    f.close()

def solve(fairs, input_file, testcase):
    A, B = map(lambda x: long(x), input_file.readline().split())
    t = filter(lambda x: x >= A and x <= B, fairs)
    print "Case #%s: %s" % (testcase, len(t))

def main():
    fairs = map(lambda x: long(x), open("fairs.txt").readlines())
    
    input_file = open(sys.argv[1])
    T = int(input_file.readline())
    for i in xrange(1, T+1):
        solve(fairs, input_file, i)

if __name__ == "__main__":
    #gen_fairs()
    main()
