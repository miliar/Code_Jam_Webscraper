#include <iostream>
#include <cstdio>
#include <string>

#define LL long long

using namespace std;

void work0(LL x, LL y)
{
    LL small = x;
    LL smallcnt = 1;
    LL bigcnt = 0;
    while ((smallcnt + bigcnt) * 2 - 1 < y)
    {
        LL s, b;
        if (small & 1)
        {
            s = smallcnt + smallcnt + bigcnt;
            b = bigcnt;
        }
        else
        {
            s = smallcnt;
            b = smallcnt + bigcnt + bigcnt;
        }
        smallcnt = s;
        bigcnt = b;
        small = (small - 1) / 2;
    }
    y -= smallcnt + bigcnt - 1;
    LL ans;
    if (y <= bigcnt) ans = small + 1; else ans = small;
    cout << ans / 2 << " " << (ans - 1) / 2 << endl;
}

void work(int n)
{
    for (int _ = 1; _ <= n; ++_)
    {
        printf("Case #%d: ", _);
        LL x, y;
        cin >> x >> y;
        work0(x, y);
    }
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n;
    cin >> n;
    work(n);
    return 0;
}
