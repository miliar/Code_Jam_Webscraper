#include <bits/stdc++.h>

using namespace std;

inline Min(int x, int y) {if(x > y) return y; else return x;}

short int dp[101][200][101][101];
bool depth[101][200][101][101];
int Hd, b, d;
int f(int H, int A, int h, int a) {
    if(A >= 200) printf("error!\n");
    if(dp[H][A][h][a]) return dp[H][A][h][a];
    if(depth[H][A][h][a]) return 10000;
    depth[H][A][h][a] = 1;
    int ans = 10000;

    if(h - A <= 0) return dp[H][A][h][a] = 1;
    else if(H - a > 0) ans = Min(ans, f(H-a, A, h-A, a) + 1);

    if(b > 0) {
        if(H - a > 0) ans = Min(ans, f(H-a, A+b, h, a) + 1);
    }

    if(Hd - a > H) ans = Min(ans, f(Hd-a, A, h, a) + 1);

    if(d > 0) {
        int na = a - d;
        if(na < 0) na = 0;
        if(H-na > 0) ans = Min(ans, f(H-na, A, h, na) + 1);
    }

    return dp[H][A][h][a] = ans;
}


int main() {
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int kase = 1; kase <= T; kase ++) {
        int H, A, h, a;
        scanf("%d%d%d%d%d%d", &H, &A, &h, &a, &b, &d);
        Hd = H;
        memset(dp, 0, sizeof(dp));
        memset(depth, 0, sizeof(depth));
        int ans = f(H, A, h, a);
        printf("Case #%d: ", kase);
        if(ans == 10000) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
    }
    return 0;
}
