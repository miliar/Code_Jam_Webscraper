def check(temp):
    s = 'aeiou';
    for i in temp:
        if i in s:
            return False
    return True
def main():
    fin = open("A-small-attempt1.in", "r")
    fout = open("a.out", "w")
    T = int(fin.readline())
    for i in range(T):
        s = fin.readline().split()
        st = str(s[0])
        n = int(s[1])
        length = len(st)
        ans = 0
        last = 0
        for j in range(n-1, length):
            temp = st[j-n+1:j+1]
            if check(temp):
                left = j-n+2
                left -= last;
                
                right = length - j
                ans += left * right
                last = j-n+2
        fout.write("Case #%d: %d\n" % (i+1, ans))
        
if __name__ == '__main__':
    main()
