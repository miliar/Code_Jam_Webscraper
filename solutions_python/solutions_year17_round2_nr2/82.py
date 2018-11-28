import sys



def run():
    n, r, o, y, g, b, v = map(int, raw_input().split())
    #print n, r, o, y, g, b, v
    colors = [(r, 'R'), (y, 'Y'), (b, 'B')]
    colors.sort(key= lambda s: s[0])
    #print colors
    ans =  [0] * n
    pos = 0
    for i in range(colors[2][0]):
        if pos >= n:
            print 'IMPOSSIBLE'
            return
        ans[pos] = colors[2][1]
        pos += 2
        
    pos = n - 1
    for i in range(colors[1][0]):
        while pos >= 0 and ans[pos] != 0:
            pos -= 1
        if pos < 0:
            print 'IMPOSSIBLE'
            return
        ans[pos] = colors[1][1]
        pos -= 2
        
    for i in range(n):
        if ans[i] == 0:
            ans[i] = colors[0][1]
            
    if ans[0] == ans[-1]:
        print 'IMPOSSIBLE'
        return
    
    for i in range(1, n):
        if ans[i] == ans[i-1]:
            print 'IMPOSSIBLE'
            return
    print ''.join(ans)

def main():
    T = input()
    for cas in range(1, T+1):
        print "Case #%d:" % (cas),
        run()

if __name__ == '__main__':
    sys.stdin = open("B-small-attempt1.in", "r")
    sys.stdout = open ("bout.txt", "w")
    main()
