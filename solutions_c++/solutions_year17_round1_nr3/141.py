#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

using ll = long long;

int T;
int f[2][128][128][128];
int Hd, Ad, Hk, Ak, B, D, ans;

void upd(int &x, int y) {
    x = max(x, y);
}

int main() {
    scanf("%d", &T);
    for (int test = 1; test <= T; ++test) {
        printf("Case #%d: ", test);
        scanf("%d%d%d%d%d%d", &Hd, &Ad, &Hk, &Ak, &B, &D);
        ans = 256;
        memset(f, -1, sizeof(f));
        f[0][Hd][Hk][Ak] = Ad;
        for (int i = 0; i < 210; ++i) {
            int I = i & 1;
            int NI = I ^ 1;
            memset(f[NI], -1, sizeof(f[NI]));
            bool alive = false;
            for (int hd = 1; hd <= Hd; ++hd)
                for (int hk = 1; hk <= Hk; ++hk)
                    for (int ak = 0; ak <= Ak; ++ak) {
                        int ad = f[I][hd][hk][ak];
                        alive = true;
                        if (f[I][hd][hk][ak] > 0) {
                            if (ad >= hk)
                                ans = min(ans, i + 1);
                            if (hd > ak && hk > ad)
                                upd(f[NI][hd - ak][hk - ad][ak], f[I][hd][hk][ak]);
                            if (hd > ak)
                                upd(f[NI][hd - ak][hk][ak], f[I][hd][hk][ak] + B);
                            if (Hd > ak)
                                upd(f[NI][Hd - ak][hk][ak], f[I][hd][hk][ak]);
                            int nak = max(0, ak - D);
                            if (hd > nak)
                                upd(f[NI][hd - nak][hk][nak], f[I][hd][hk][ak]);
                        }
                    }
            if (!alive)
                break;
        }
        if (ans > 210)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", ans);
    }
    return 0;
}