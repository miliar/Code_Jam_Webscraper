#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long ll;
ll n, k;

void solve()
{
    scanf("%lld%lld", &n, &k);
    ll i = floor(log(k) / log(2));
    ll t = 1 << (i + 1);
    ll delta = 1 << i;
    ll l = (n - k) / t;
    ll r = (n - k + delta) / t;
    printf("%lld %lld\n", r, l);
}

int main()
{
    int t;
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