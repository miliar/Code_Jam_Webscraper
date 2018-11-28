#include <algorithm>
#include <cstdio>
#include <map>
using namespace std;

typedef long long ll;

int main() {
    int t;
    ll k, n;
    scanf("%d", &t);
    for (int tt = 1; tt <= t; tt++) {
        scanf("%lld %lld", &n, &k);
        map<ll, ll> mapa;
        mapa[n]++;
        ll ans;
        while (k > 0) {
            auto x = mapa.rbegin();
            ll xst = x->first, xnd = x->second;
            ans = xst;
            k -= xnd;
            mapa[xst/2] += xnd;
            mapa[(xst-1)/2] += xnd;
            mapa.erase(ans);
        }
        printf("Case #%d: %lld %lld\n", tt, ans/2, (ans-1)/2);
    }
    return 0;
}
