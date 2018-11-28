#include <cstdio>
#include <map>
#include <tuple>
#define repeat(i,n) for (int i = 0; (i) < int(n); ++(i))
using ll = long long;
using namespace std;

pair<ll, ll> solve(ll n, ll k) {
    map<ll, ll> que;
    que.emplace(n, 1);
    while (true) {
        ll len, cnt; tie(len, cnt) = *que.rbegin(); que.erase(len);
        ll l = (len - 1) / 2;
        ll r = (len - 1 + 1) / 2;
        que[l] += cnt;
        que[r] += cnt;
        k -= cnt;
        if (k <= 0) {
            return make_pair(r, l);
        }
    }
}
int main() {
    int t; scanf("%d", &t);
    repeat (x,t) {
        ll n, k; scanf("%lld%lld", &n, &k);
        ll y, z; tie(y, z) = solve(n, k);
        printf("Case #%d: %lld %lld\n", x+1, y, z);
    }
    return 0;
}
