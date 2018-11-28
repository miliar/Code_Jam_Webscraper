#include <bits/stdc++.h>

int T;
long long n, k;

int main() {
    scanf("%d", &T);
    for (int test = 1; test <= T; test++) {
        scanf("%lld%lld", &n, &k);
        std::map<long long, long long> m;
        std::set<long long> s;
        s.insert(n);
        m[n] = 1;
        while (true) {
            long long i = *s.rbegin();
            s.erase(--s.end());
            if (k <= m[i]) {
                printf("Case #%d: %lld %lld\n", test, i/2, (i-1)/2);
                break;
            }
            k -= m[i];
            m[i/2] += m[i];
            m[(i-1)/2] += m[i];
            s.insert(i/2);
            s.insert((i-1)/2);
        }
    }
}

