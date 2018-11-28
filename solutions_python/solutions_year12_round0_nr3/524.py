def count(num, a, b):
    global flag
    st = str(num)
    s = 0
    for i in range(len(st)-1):
        n = int(st[i+1:] + st[:i+1])
        if n in flag:
            return 0
        if n >= a and n <= b and n > num:
            tmp = int(str(num)+str(n)) 
            if not tmp in flag:
                s += 1
                flag[tmp] = True
    return s

    
def main(filename):
    global flag
    f = open(filename)
    ouf = open("3output.txt", "w")
    num_of_tests = int(f.readline())
    for test_i in range(num_of_tests):
        line = f.readline().split(" ")
        a = int(line[0])
        b = int(line[1])
        ans = 0
        flag = dict()
        for i in range(a, b+1):
            ans += count(i, a, b)
        print test_i + 1
        ouf.write("Case #%d: %d\n" % (test_i + 1, ans))

if __name__ == "__main__":
    main("C-large.in.txt")
                
        
    