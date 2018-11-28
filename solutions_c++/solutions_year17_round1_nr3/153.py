#include <bits/stdc++.h>

const long long inf = 1000ll*1000*1000*1000*1000;

int Tests;
long long hd, ad, hk, ak, b, d;

long long go(long long hd, long long ad, long long hk, long long ak, long long b, long long d, long long B, long long D) {
    long long starthealth = hd;
    for (int i = 0; i < 1000; i++) {
        if (ad >= hk) {
            // we done
            return i+1;
        } else if (D && hd > ak - d) {
            ak = std::max(0ll, ak - d);
            D--;
        } else if (B && hd > ak) {
            ad += b;
            B--;
        } else if (ak >= hd) {
            // heal
            hd = starthealth;
        } else {
            // attack
            hk -= ad;
        }
        // knight attacks
        hd -= ak;
        if (hd <= 0) {
            return inf;
        }
    }
    // it's not quite working out...
    return inf;
}

int main() {
    scanf("%d", &Tests);
    for (int test = 1; test <= Tests; test++) {
        scanf("%lld%lld%lld%lld%lld%lld", &hd, &ad, &hk, &ak, &b, &d);
        long long ans = inf;
        for (int D = 0; D <= 100; D++) {
            for (int B = 0; B <= 100; B++) {
                ans = std::min(ans, go(hd, ad, hk, ak, b, d, B, D));
            }
        }
        if (ans >= inf) {
            printf("Case #%d: IMPOSSIBLE\n", test);
        } else {
            printf("Case #%d: %lld\n", test, ans);
        }
    }
}

