#include <bits/stdc++.h>

using namespace std;

typedef long long LL;


int main() {
    int T;
    scanf("%d", &T);
    for (int _ = 1; _ <= T; _++) {
        LL n, k;
        scanf("%lld%lld", &n, &k);
        map<LL, LL> mp;
        mp[n] = 1;
        LL mn, mx;
        while (1) {
            LL len = mp.rbegin()->first;
            LL cnt = mp.rbegin()->second;
            mp.erase(len);
            LL l = (len - 1) / 2, r = len / 2;
            if (cnt >= k) {
                mn = l;
                mx = r;
                break;
            }
            mp[l] += cnt;
            mp[r] += cnt;
            k -= cnt;
        }
        printf("Case #%d: %lld %lld\n", _, mx, mn);
    }
    return 0;
}
