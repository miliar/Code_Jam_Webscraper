#include <cstdio>
#include <map>

using namespace std;

typedef long long ll;

int TC, tc;
ll N, K;

map<ll, ll> m;

int main() {
    freopen("i.in", "r", stdin);
    freopen("o.out", "w", stdout);
    scanf("%d", &TC);
    while(TC--) {
        m.clear();
        scanf("%lld%lld", &N, &K);
        m[-N]++;
        ll n, v = 0;
        while(n = m.begin()->first, v += m[n], v < K) {
            m[n / 2] += m[n];
            m[(n+1) / 2] += m[n];
            m.erase(m.begin());
        }
        printf("Case #%d: %lld %lld\n", ++tc, -n/2, (-n-1)/2);
    }
}
