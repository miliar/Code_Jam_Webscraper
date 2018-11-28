#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define N 20
typedef long long ll;
int f[N][10];
int num[N];

int dp(int i, int s, bool zero, bool e)
{
    if (i < 0)
        return 1;
    if (!e && ~f[i][s])
        return f[i][s];
    int ans = 0;
    int u = e ? num[i] : 9;
    for (int d = 0; d <= u; ++d)
        if (zero)
            ans += dp(i - 1, d, zero && d == 0, e && d == u);
        else if (d >= s)
            ans += dp(i - 1, d, 0, e && d == u);
    return e ? ans : f[i][s] = ans;
}

int count(ll n)
{
    int len = 0;
    for (; n; n /= 10)
        num[len++] = n % 10;
    return dp(len - 1, 0, 1, 1);
}

void solve()
{
    ll n;
    scanf("%lld", &n);
    int target = count(n);
    ll l = 1, r = n;
    while (l < r)
    {
        ll mid = (l + r) >> 1;
        if (count(mid) < target)
            l = mid + 1;
        else
            r = mid;
    }
    printf("%lld\n", r);
}

int main()
{
    int t;
    memset(f, -1 ,sizeof(f));
    freopen("1.txt", "r", stdin);
    freopen("2.txt", "w", stdout);
    scanf("%d", &t);
    for (int tt = 1; tt <= t; ++tt)
    {
        printf("Case #%d: ", tt);
        solve();
    }
    return 0;
}