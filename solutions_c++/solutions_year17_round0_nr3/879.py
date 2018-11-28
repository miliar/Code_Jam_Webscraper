#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define debug printf
typedef long long ll;
typedef pair<ll, ll> pll;

ll rec2(ll q, ll a, ll na, ll nb) {
    /* printf("rec2 %lld %lld %lld %lld\n", q, a, na, nb); */
    if (q < na) {
        return a;
    } else if (q < na + nb) {
        return a-1;
    } else {
        if (a % 2 == 0)
            return rec2(q-na-nb, a/2, na, na+2*nb);
        else
            return rec2(q-na-nb, a/2, 2*na+nb, nb);
    }
}

void solve(int T) {
    ll n, k; scanf("%lld%lld", &n, &k);
    ll sol = rec2(k-1, n, 1, 0);
    printf("Case #%d: %lld %lld\n", T, sol/2, max(0LL, (sol-1)/2));
}

int main() {
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; t++)
        solve(t);
    return 0;
}
