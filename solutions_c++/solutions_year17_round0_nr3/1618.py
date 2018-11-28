#include <cstdio>
#include <cstring>
#include <map>
using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        long long n, k;

        scanf("%lld %lld", &n, &k);
        map<long long, long long> m;
        m[n] = 1;
        long long S = 1;
        while (k > S) {
            // printf("SZ=%u\n", m.size());
            k -= S;
            map<long long, long long> ne;
            S = 0;
            for (map<long long, long long>::iterator it = m.begin(); it != m.end(); ++it) {
                // printf("%lld %lld\n", it->first, it->second);
                ne[it->first / 2] += it->second;
                if (it->first / 2 > 0) {
                    S += it->second;
                }
                ne[(it->first - 1) / 2] += it->second;
                if ((it->first - 1) / 2 > 0) {
                    S += it->second;
                }
            }
            m = ne;
        }
        for (map<long long, long long>::reverse_iterator it = m.rbegin(); it != m.rend(); ++it) {
            if (k > it->second) {
                k -= it->second;
                continue;
            }
            printf("Case #%d: ", t);
            printf("%lld %lld\n", it->first / 2, (it->first - 1) / 2);
            break;
        }
    }
    return 0;
}
