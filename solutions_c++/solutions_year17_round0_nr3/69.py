#include <map>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

using ll = long long;

int T;
ll n, k;
map<ll, ll> h;

int main() {
    scanf("%d", &T);
    for (int test = 1; test <= T; ++test) {
        h.clear();
        scanf("%lld%lld", &n, &k);
        h[n] = 1;
        ll al, ar;
        while (k > 0) {
            auto it = h.end();
            --it;
            ll len = it->first;
            ll count = it->second;
            if (count >= k) {
                al = len / 2;
                ar = (len - 1) / 2;
                break;
            } else {
                h.erase(it);
                ll tl, tr;
                tl = len / 2;
                tr = (len - 1) / 2;
                k -= count;
                h[tl] += count;
                h[tr] += count;
            }
        }
        printf("Case #%d: %lld %lld\n", test, al, ar);
    }
    return 0;
}
