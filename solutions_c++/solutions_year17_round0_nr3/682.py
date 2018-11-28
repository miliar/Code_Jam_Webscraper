#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

pair<ll, ll> f(ll l, ll r, ll q)
{
    if (q == 0) return {0,0};

    ll mid = l + ((r - l) / 2);
    if (q == 1) return {min(mid - l, r - mid), max(mid - l, r - mid)};

    q--;

    if (q % 2 == 0) {
        return f(l, mid - 1, q/2);
    } else {
        return f(mid + 1, r, (q+1) / 2);
    }
}

int main()
{
    int t;
    cin >> t;
    int tc = 1;

    while (t--) {
        ll n, k;
        cin >> n >> k;
        pair<ll, ll> ans = f(1, n, k);
        printf("Case #%d: %lld %lld\n", tc++, ans.second, ans.first);
    }

    return 0;
}
