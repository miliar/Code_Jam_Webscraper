def solve():
    n = int( input() )
    for i in range(n):
        _t = 2
        c,f,x = map(float, input().split())
        curr = x/_t
        fut, ans = x/(f+_t) + c/_t, 0
        while fut < curr :
            ans += c/_t
            _t += f
            curr = x/_t;
            fut = x/(f + _t) + c/_t
        ans += curr
        print ("Case #{}: {}".format(i+1,ans))

if __name__ == '__main__':
    solve()

