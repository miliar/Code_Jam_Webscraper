#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>

using namespace std;

int T;
long long N, K;

int main() {
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%lld %lld", &N, &K);
        map<long long, long long> s;
        s[N] = 1;

        long long remaining = K, a, b;
        while (remaining > 0) {
            map<long long, long long>::reverse_iterator end = s.rbegin();
            long long width = end->first;
            long long freq = end->second;
            s.erase(width);

            a = (width - 1) / 2;
            b = width - 1 - a;
            if (s.find(a) == s.end()) {
                s[a] = freq;
            } else {
                s[a] += freq;
            }
            if (s.find(b) == s.end()) {
                s[b] = freq;
            } else {
                s[b] += freq;
            }

            remaining -= freq;

        }
        printf("Case #%d: %lld %lld\n", t, max(a, b), min(a, b));
    }

    return 0;
}
