#include <bits/stdc++.h>
using namespace std;

int calc(int nb, int nd, int hd, int ad, int hk, int ak, int b, int d, int cure) {
    int ret = 0;
    int con = 0;
    for (int i = 0; i < nd; i++) {
        if (hd > ak - d) {
            ak = max(0, ak - d);
            hd -= ak;
            con = 0;
        } else {
            if (con == 1) return INT_MAX;
            con = 1;
            hd = cure;
            hd -= ak;
            if (hd <= 0) return INT_MAX;
            i--;
        }
        ret++;
    }
    con = 0;
    for (int i = 0; i < nb; i++) {
        if (hd > ak) {
            ad += b;
            hd -= ak;
            con = 0;
        } else {
            if (con == 1) return INT_MAX;
            con = 1;
            hd = cure;
            hd -= ak;
            if (hd <= 0) return INT_MAX;
            i--;
        }
        ret ++;
    }
    con = 0;
    while (1) {
        ret ++;
        if (hk <= ad || hd > ak) {
            hk -= ad;
            if (hk <= 0) break;
            con = 0;
        } else {
            if (con == 1) return INT_MAX;
            con = 1;
            hd = cure;
        }
        hd -= ak;
        if (hd <= 0) return INT_MAX;
    }
    return ret;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int CAS, hd, ad, hk, ak, b, d;
    cin >> CAS;
    for (int cas = 1; cas <= CAS; cas++) {
        scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &b, &d);
        int ans = INT_MAX;
        for (int nd = 0; nd <= 100; nd++) {
            for (int nb = 0; nb <= 100; nb++) {
                ans = min(ans, calc(nb, nd, hd, ad, hk, ak, b, d, hd));
            }
        }
        printf("Case #%d: ", cas);
        if (ans == INT_MAX) {
            puts("IMPOSSIBLE");
        } else {
            printf("%d\n", ans);
        }
    }
}
