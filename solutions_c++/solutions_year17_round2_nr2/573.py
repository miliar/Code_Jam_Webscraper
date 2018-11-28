#include <bits/stdc++.h>

using std::cin;
using std::cout;
using std::cerr;
using std::ios_base;
using std::fixed;
using std::endl;

using std::pair;
using std::make_pair;
using std::swap;

using std::string;
using std::vector;
using std::map;
using std::set;

using std::sort;
using std::reverse;

#define pb push_back
#define mp make_pair
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define sqr(x) ((x) * (x))

const int MAXN = 1005;
const int INF = 1e9;
const int MOD = 1e9+7;
const long long L_INF = 4e18;
const long double EPS = 1e-10;

int T;
int n, cnt[6];
char col[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(10);
    cout << fixed;
    srand(566);

    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        cin >> n;
        int mx = 0;
        for (int i = 0; i < 6; i++) {
            cin >> cnt[i];
            mx = std::max(mx, cnt[i]);
        }
        string ans = "";
        bool ok = true;
        for (int i = 0; i < n; i++) {
            pair<int, int> best(-1, -1);
            for (int j = 0; j < 6; j++) {
                if (!ans.empty() && col[j] == ans[i - 1])
                    continue;
                best = std::max(best, make_pair(cnt[j], j));
            }
            ok &= best.first > 0;
            if (!ok) break;

            ans += col[best.second];
            cnt[best.second]--;
        }
        if (ok && ans[0] == ans[n - 1]) {
            for (int i = n - 1; i > 1; i--) {
                swap(ans[i], ans[i - 1]);
                if (ans[i - 1] != ans[i - 2] && ans[i - 1] != ans[i])
                    break;
            }
        }
        for (int i = 0; i < n; i++) {
            int j = (i + 1) % n;
            ok &= ans[i] != ans[j];
        }
        cout << (ok ? ans : "IMPOSSIBLE") << endl;
        assert(ok == (mx * 2 <= n));
    }

#ifdef LOCAL
    cerr << "\n== " << 1.0 * clock() / CLOCKS_PER_SEC << " sec.\n";
#endif
    return 0;
}
