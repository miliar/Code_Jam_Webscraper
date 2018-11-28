#include <bits/stdc++.h>
#define SZ(x) ((int) (x).size())
using namespace std;

void solve() {
    int n, c, m;
    cin >> n >> c >> m;

    vector<vector<int>> poss(c + 1);
    vector<int> cnt(n + 1, 0);
    for (int i = 1; i <= m; ++i) {
        int pos, b;
        cin >> pos >> b;
        poss[b].push_back(pos);
        cnt[pos]++;
    }
    int ans = 0;
    for (int i = 1; i <= c; ++i) {
        ans = max(ans, SZ(poss[i]));
    }
    for (int i = 1; i <= n; ++i) {
        cnt[i] += cnt[i - 1];
        while (ans * i < cnt[i]) {
            ans++;
        }
    }
    int ans2 = 0;
    for (int i = 1; i <= n; ++i) {
        int x = cnt[i] - cnt[i - 1];
        ans2 += max(0, x - ans);
    }
    cout << ans << ' ' << ans2 << '\n';
    
}

int main() {
    #ifdef LOCAL_RUN
    freopen("task.in", "r", stdin);
    freopen("task.out", "w", stdout);
    //freopen("task.err", "w", stderr);
    #endif // ONLINE_JUDGE
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        solve();
    }
}
