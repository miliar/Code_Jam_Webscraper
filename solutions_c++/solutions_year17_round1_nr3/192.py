#pragma GCC optimize(2)
#include <bits/stdc++.h>
#define LL long long
#define INF 0x3f3f3f3f
using namespace std;

template<class T> inline
void read(T& x) {
    int f = 1; x = 0;
    char ch = getchar();
    while (ch < '0' || ch > '9')   {if (ch == '-') f = -1; ch = getchar();}
    while (ch >= '0' && ch <= '9') {x = x * 10 + ch - '0'; ch = getchar();}
    x *= f;
}

/*============ Header Template ============*/

int gcd(int a, int b) {return b == 0 ? a : gcd(b, a % b);}

int hd, ad, hk, ak, B, D;

int main() {
    int T, kas = 0;
    read(T);
    while (T--) {
        read(hd), read(ad), read(hk), read(ak), read(B), read(D);
        int nak = ak, nhd = hd, nct = 0, ans = INF;
        for (int i = 0; i <= ((D == 0) ? 0 : (ak / D + 1)); ++ i) {
            int W = nhd, nad = ad, nnct = nct;
            for (int j = 0; j <= ((B == 0) ? 0 : (hk - ad / B + 1)); ++ j) {
                int WF = W, nhk = hk, nnnct = nnct;
                while (1) {
                    if (nhk - nad <= 0) {ans = min(ans, nnnct + 1); break;}
                    if (WF <= nak) {WF = hd; WF -= nak; nnnct++;}
                    if (WF <= 0) break;
                    nhk -= nad; WF -= nak; nnnct++;
                    if (WF <= 0) break;
                }
                if (W <= nak) {W = hd; W -= nak; nnct++;}
                if (W <= 0) break;
                nad += B; W -= nak; nnct++;
                if (W <= 0) break;
            }
            if (nhd <= nak - D) {nhd = hd; nhd -= nak; nct++;}
            if (nhd <= 0) break;
            nak -= D; nhd -= nak; nct++;
            if (nhd <= 0) break;
        }
        printf("Case #%d: ", ++kas);
        if (ans == INF) puts("IMPOSSIBLE");
        else printf("%d\n", ans);
    }
    return 0;
}