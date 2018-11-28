#include<cstdio>
#include<algorithm>
using namespace std;
int hdx, adx, hkx, akx, b, d;
static inline int test(int bt, int dt) {
    int bc = 0, dc = 0;
    int hd = hdx, ad = adx, hk = hkx, ak = akx;
    bool jc = false;
    int turn = 0;
    while (dc < dt) {
        turn++;
        int akn = max(0, ak-d);
        if (hd-akn <= 0) {
            if (jc || hdx-ak <= 0) {
                return -1;
            }
            hd = hdx-ak;
            jc = true;
        } else {
            ak = akn;
            hd -= ak;
            jc = false;
            dc++;
        }
    }
    while (bc < bt) {
        turn++;
        if (hd-ak <= 0) {
            if (jc || hdx-ak <= 0) {
                return -1;
            }
            hd = hdx-ak;
            jc = true;
        } else {
            ad += b;
            hd -= ak;
            jc = false;
            bc++;
        }
    }
    while (hk > 0) {
        turn++;
        if (hk-ad > 0 && hd-ak <= 0) {
            if (jc || hdx-ak <= 0) {
                return -1;
            }
            hd = hdx-ak;
            jc = true;
        } else {
            hk -= ad;
            if (hk > 0) {
                hd -= ak;
            }
            jc = false;
        }
    }
    return turn;
}
int main() {
    int ttt;
    int am, bm, dm, best;
    bool possible;
    scanf("%d", &ttt);
    for (int tt = 1; tt <= ttt; tt++) {
        scanf("%d", &hdx);
        scanf("%d", &adx);
        scanf("%d", &hkx);
        scanf("%d", &akx);
        scanf("%d", &b);
        scanf("%d", &d);
        possible = false;
        best = -1;
        if (b == 0) {
            bm = 0;
        } else {
            bm = 400;//(hkx-adx+b-1)/b;
        }
        if (d == 0) {
            dm = 0;
        } else {
            dm = 400;//(akx+d-1)/d;
        }
        for (int bi = 0; bi <= bm; bi++) {
            for (int di = 0; di <= dm; di++) {
                int result = test(bi, di);
                if (result > -1) {
                    if (!possible) {
                        possible = true;
                        best = result;
                    } else {
                        best = min(best, result);
                    }
                }
            }
        }
        if (possible) {
            printf("Case #%d: %d\n", tt, best);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", tt);
        }
    }
    return 0;
}
