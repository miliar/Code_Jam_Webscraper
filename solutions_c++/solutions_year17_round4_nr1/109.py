#include <bits/stdc++.h>
#define SZ(x) ((int) (x).size())
using namespace std;

void solve() {
    int n, p;
    cin >> n >> p;
    vector<int> cnt(p, 0);
    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        cnt[x % p]++;
    }
    int ans = 0;
    if (p == 2) {
        ans = cnt[0];
        ans += (cnt[1] + p - 1) / p;
    } else if (p == 3) {
        ans = cnt[0];
        int x = min(cnt[1], cnt[2]);
        ans += x;
        cnt[1] -= x;
        cnt[2] -= x;
        ans += (cnt[1] + p - 1) / p;
        ans += (cnt[2] + p - 1) / p;
    } else if (p == 4) {
        ans = cnt[0];
        ans += cnt[2] / 2;
        cnt[2] %= 2;
        int x = min(cnt[1], cnt[3]);
        ans += x;
        cnt[1] -= x;
        cnt[3] -= x;
        if (cnt[2] == 0) {
            ans += (cnt[1] + cnt[3] + p - 1) / p;
        } else {
            if (cnt[1] + cnt[3] >= 2) {
                if (cnt[1] >= 2) {
                    cnt[1] -= 2;
                } else {
                    cnt[3] -= 2;
                }
                cnt[2] = 0;
                ans++;
            }
            ans += (cnt[1] + cnt[3] + p - 1) / p;
        }
    }
    cout << ans << '\n';
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
