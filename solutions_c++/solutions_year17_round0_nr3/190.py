#include <bits/stdc++.h>
#define SZ(x) ((int) (x).size())
using namespace std;

typedef long long i64;

void solve() {
    int64_t n, k;
    cin >> n >> k;

    map<int64_t, int64_t> cnt;
    cnt[n]++;
    int64_t total = 0;
    int64_t ans1 = 0, ans2 = 0;
    while (total < k) {
        auto it = cnt.end();
        --it;
        int64_t value = it->first, freq = it->second;
        cnt.erase(value);
        int64_t v1 = (value - 1) / 2;
        int64_t v2 = value / 2;
        cnt[v1] += freq;
        cnt[v2] += freq;
        ans1 = v2;
        ans2 = v1;
        total += freq;
    }
    cout << ans1 << ' ' << ans2 << '\n';
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

    for (int i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }
}
