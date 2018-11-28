#include <map>
#include <cstdio>
#include <algorithm>
using namespace std;

long long n, k;

void read() {
    scanf ("%lld%lld", &n, &k);
}

void solve() {
    map<long long, long long> m1, m2;

    m1[n] = 1;

    while (1) {
        for (map<long long, long long>::reverse_iterator kv = m1.rbegin(); kv != m1.rend(); kv++) {
            //printf ("%lld %lld\n", kv->first, kv->second);
            long long l = (kv->first - 1) / 2;
            long long r = l + (kv->first - 1) % 2;

            if (k <= kv->second) {
                printf ("%lld %lld\n", r, l);
                return ;
            }
            k -= kv->second;
            m2[l] += kv->second;
            m2[r] += kv->second;
        }
        m1 = m2;
        m2.clear();
    }

}

int main() {
    int i, cases;

    scanf("%d", &cases);
    for (i = 1; i <= cases; i++) {
        read();
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}

