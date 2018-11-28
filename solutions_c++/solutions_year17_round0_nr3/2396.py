#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long ll;

ll solve(ll n, ll k)
{
    if (k == 1) return n;
    ll cnt, sum = n, a = 2 * n + 1, b = 2 * n + 1;
    for (ll i = 1; i <= k; i *= 2) {
        sum -= i / 2;
        cnt = i;
        
        if (b % 2 == 0) swap(a, b);
        ll t = a - 1;
        a = t - t / 2;
        b = t / 2;
    }
    ll x, y;
    if (a == b) x = cnt, y = 0;
    else {
        y = (a * cnt - sum) / (a - b);
        x = cnt - y;
    }
    k -= (cnt - 1);
    if (k <= x) return a;
    return b;
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int tc = 1; tc <= T; tc++) {
        ll n, k;
        scanf("%lld%lld", &n, &k);
        ll c = solve(n, k) - 1;
        printf("Case #%d: %lld %lld\n", tc, c - c / 2, c / 2);
    }
    return 0;
}
