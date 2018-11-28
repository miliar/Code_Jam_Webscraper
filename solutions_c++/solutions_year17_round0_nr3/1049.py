#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

int main() {
//    freopen("C-small-2-attempt0.in", "r", stdin);
//    freopen("C-small-2-attempt0.out", "w", stdout);
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    int T;
    LL N, K;

    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        scanf("%lld %lld", &N, &K);
        map<LL, LL> mp;
        mp[N] = 1;
        while (K > 0) {
            auto p = *mp.rbegin();
            if (K <= p.second) break;
            K -= p.second;
            mp.erase(p.first);
            mp[(p.first - 1) / 2] += p.second;
            mp[p.first / 2] += p.second;
        }
        LL w = mp.rbegin()->first;
        printf("Case #%d: %lld %lld\n", t, w / 2, (w - 1) / 2);
    }

    return 0;
}

