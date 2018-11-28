#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=a;i<b;i++)




typedef long long ll;
#define INF 1LL<<60
int B, D, Hd;
ll memo[101][101][101][101];
int vis[101][101][101][101];
ll rec(int hd, int Ad, int Hk, int Ak) {
    if (0 < memo[hd][Ad][Hk][Ak]) return memo[hd][Ad][Hk][Ak];
    if (vis[hd][Ad][Hk][Ak]) return INF;
    vis[hd][Ad][Hk][Ak] = 1;

    //fprintf(stderr, "[%d %d %d %d]\n", hd, Ad, Hk, Ak);

    auto &dp = memo[hd][Ad][Hk][Ak];

    ll ret = INF;

    // Can Win
    if (Hk <= Ad) ret = 1;
    else {
        // Attack
        if (Ak < hd) ret = min(ret, rec(hd - Ak, Ad, Hk - Ad, Ak) + 1);

        // Buff
        if (Ak < hd) {
            if(Ad + B <= 100) ret = min(ret, rec(hd - Ak, Ad + B, Hk, Ak) + 1);
            else ret = min(ret, 2LL);
        }

        // Cure
        if (Ak < Hd) ret = min(ret, rec(Hd - Ak, Ad, Hk, Ak) + 1);

        // Debuff
        if (max(0, Ak - D) < hd) ret = min(ret, rec(hd - max(0, Ak - D), Ad, Hk, max(0, Ak - D)) + 1);
    }

    //printf("[%d %d %d %d] = %d\n", hd, Ad, Hk, Ak, ret);

    return dp = ret;
}
ll sol() {
    int Ad, Hk, Ak;
    cin >> Hd >> Ad >> Hk >> Ak >> B >> D;

    rep(a, 0, 101) rep(b, 0, 101) rep(c, 0, 101) rep(d, 0, 101) vis[a][b][c][d] = memo[a][b][c][d] = 0;
    return rec(Hd, Ad, Hk, Ak);
}
//-----------------------------------------------------------------------------------
int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int T; cin >> T;
    rep(t, 1, T + 1) {
        ll ans = sol();
        if(ans == INF) printf("Case #%d: IMPOSSIBLE\n", t);
        else printf("Case #%d: %lld\n", t, ans);
        fprintf(stderr, "Finish : %d\n", t);
    }
}