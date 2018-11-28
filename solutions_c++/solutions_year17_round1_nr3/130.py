#include <cstdint>
#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

int64_t Hd, Ad, Hk, Ak, B, D;
int64_t ans;

void check(int64_t d, int64_t b) {
    int64_t hd = Hd;
    int64_t ad = Ad;
    int64_t hk = Hk;
    int64_t ak = Ak;

    int64_t step = 0;
    for (int64_t i = 0; i < d; i++) {
        if (hd <= ak - D) {
            step++;
            hd = Hd - ak;
            if (hd <= ak) return;
        }
        ak -= D;
        hd -= ak;
        step++;
    }

    for (int64_t i = 0; i < b; i++) {
        if (hd <= ak) {
            step++;
            hd = Hd - ak;
            if (hd <= ak) return;
        }
        ad += B;
        hd -= ak;
        step++;
    }

    if (ad == 0) return;
    while (true) {
        step++;
        if (hk <= ad) break;
        if (hd <= ak) {
            hd = Hd - ak;
            if (hd <= ak) return;
        } else {
            hk -= ad;
            hd -= ak;
        }
    }

    if (ans < 0 || step < ans) ans = step;
}

void solve() {
    cin >> Hd >> Ad >> Hk >> Ak >> B >> D;

    int64_t Dmax = 0;
    if (D > 0) Dmax = Ak / D + 1;
    int64_t Bmax = 0;
    if (B > 0) Bmax = Hk / B + 1;

    ans = -1;
    for (int64_t d = 0; d <= Dmax; d++)
    {
        for (int64_t b = 0; b <= Bmax; b++)
        {
            check(d, b);
        }
    }

    if (ans < 0) {
        cout << "IMPOSSIBLE" << endl;
    } else {
        cout << ans << endl;
    }
}

int main() {
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; testcase++) {
        cout << "Case #" << testcase << ": ";
        solve();
    }
    return 0;
}
