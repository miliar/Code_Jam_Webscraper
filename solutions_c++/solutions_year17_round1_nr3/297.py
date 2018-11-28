#include <bits/stdc++.h>
#define REP(i, a, b) for (int i = a, i##__end__ = b; i <= i##__end__;++i)
#define PER(i, a, b) for (int i = a, i##__end__ = b; i >= i##__end__; --i)
#define RVC(i, S) for (int i = 0; i < S.size();++i)
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define debug(...) fprintf(stderr, __VA_ARGS__)
using namespace std;

typedef pair<int, int> pii;
typedef vector<int> VI;
typedef long long LL;

inline int read(){
    int x = 0, ch = getchar(), f = 1;
    while (!isdigit(ch)){if (ch == '-') f = -1; ch = getchar();}
    while (isdigit(ch)) x = x * 10 + ch - '0', ch = getchar();
    return x * f;
}

const int INF = 1000000000;

void solve(){
    int hd, ad, hk, ak, B, D;
    hd = read(), ad = read(), hk = read();
    ak = read(), B = read(), D = read();
    
    int ak1 = ak, hd1 = hd, ct1 = 0, ans = INF;
    REP(i, 0, (D ? (ak / D + 1) : 0)){
        int hd2 = hd1, ad1 = ad, ct2 = ct1;
        REP(j, 0, (B ? (hk - ad / B + 1) : 0)){
            int hd3 = hd2, nhk = hk, ct3 = ct2;
            while (1){
                if (nhk - ad1 <= 0) {ans = min(ans, ct3 + 1); break;}
                if (hd3 <= ak1){
                    ct3++;
                    hd3 = hd;
                    hd3 -= ak1;
                }
                if (hd3 <= 0) break;
                ct3++;
                nhk -= ad1;
                hd3 -= ak1;
                if (hd3 <= 0) break;
            }

            if (hd2 <= ak1){
                hd2 = hd;
                hd2 -= ak1;
                ct2++;
            }
            if (hd2 <= 0) break;
            ad1 += B;
            hd2 -= ak1;
            ct2++;
            if (hd2 <= 0) break;
        }

        if (hd1 <= ak1 - D){
            hd1 = hd;
            hd1 -= ak1;
            ct1++;
        }
        if (hd1 <= 0) break;
        ak1 -= D;
        hd1 -= ak1;
        ct1++;
        if (hd1 <= 0) break;
    }
    if (ans == INF) cout << "IMPOSSIBLE\n";
    else cout << ans << endl;
}

int main(){
    int T = read();
    REP(kas, 1, T){
        printf("Case #%d: ", kas);
        solve();
    }
}