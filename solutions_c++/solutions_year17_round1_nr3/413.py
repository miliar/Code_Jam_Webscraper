#include <bits/stdc++.h>
using namespace std;

int dp[101][101][101][101];
int B, D;
constexpr int inf = 100000;
int fullB;

int dfs(int Hd, int Ad, int Hk, int Ak) {
    if (Hk <= 0) return 0;
    if (Hd <= 0) return inf;
    if (Ad >= Hk) return 1;

    /*
    assert(Ad >= 0 and Ak >= 0);
    assert(Hd >= 0 and Hd <= 100);
    assert(Hk >= 0 and Hk <= 100);
    assert(Ad <= 200 and Ak <= 100);
    */
    int &ans = dp[Hd][Ad][Hk][Ak];
    if (ans != -1) return ans;
    ans = inf;

    ans = min(ans, dfs(Hd - Ak, Ad, Hk - Ad, Ak) + 1);
    if (B > 0) ans = min(ans, dfs(Hd - Ak, Ad + B, Hk, Ak) + 1);
    ans = min(ans, dfs(fullB - Ak, Ad, Hk, Ak) + 1);
    if (D > 0) ans = min(ans, dfs(Hd - Ak, Ad, Hk, max(Ak - D, 0)) + 1);
    ans = min(ans, inf);
    return ans;
}

int main(void) {
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++ t) {
        memset(dp, -1, sizeof(dp));

        cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
        fullB = Hd;

        int ans = dfs(Hd, Ad, Hk, Ak);

        if (ans < inf)
            cout << "Case #" << t << ": " << ans << endl;
        else
            cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
    }

    return 0;
}
