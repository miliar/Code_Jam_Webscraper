#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

const int N = 5555;
const int Inf = 1e9 + 7;

int T, cas;

int hd, ad, hk, ak, b, d, res;

void Dfs(int HD, int AD, int HK, int AK, int sta, int tot) {
//    cout << HD << ' ' << AD << ' ' << HK << ' ' << AK << ' ' << sta << ' ' << tot << ' ' << res << endl;
    if (tot > res) return;
    if (HD <= 0) return;
//    cout << "!" << endl;
    if (sta == 0) {
        Dfs(HD, AD, HK, AK, 1, tot);
        int atk = max(0, AK - d);
        if (HD - atk <= 0) {
            Dfs(hd - AK, AD, HK, AK, 0, tot + 1);
            return;
        }
        Dfs(HD - atk, AD, HK, atk, 0, tot + 1);
    } else if (sta == 1) {
        Dfs(HD, AD, HK, AK, 2, tot);
        if (HD - AK <= 0) {
            Dfs(hd - AK, AD, HK, AK, 1, tot + 1);
            return;
        }
        int atk = AD + b;
        Dfs(HD - AK, atk, HK, AK, 1, tot + 1);
    } else {
        if (HK - AD <= 0) {
            res = min(res, tot + 1);
            return;
        }
        if (HD - AK <= 0) {
            Dfs(hd - AK, AD, HK, AK, 2, tot + 1);
            return;
        }
        Dfs(HD - AK, AD, HK - AD, AK, 2, tot + 1);
    }
}

int Calc() {
//    if (ad >= hk) return 1;
//    if (Debuff(1) >= hd) return -1;
//    if (ad + ad >= hk) return 2;
//    if (ad + b >= hk) return 2;
//    if (Debuff(1) + Debuff(2) >= hd) return -1;
    res = 300;

    Dfs(hd, ad, hk, ak, 0, 0);

    if (res == 300) return -1;
    else return res;

}

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C.out", "w", stdout);
    cin >> T;
    while (T --) {
        cin >> hd >> ad >> hk >> ak >> b >> d;
        printf("Case #%d: ", ++ cas);
        int t = Calc();
        if (t == -1) puts("IMPOSSIBLE");
        else printf("%d\n", t);
    }
}
