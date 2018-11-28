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

int T, k;
string s;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(10);
    cout << fixed;
    srand(566);

    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> s >> k;
        int cnt = 0;
        for (int i = 0; i < (int) s.size() - k + 1; i++) {
            if (s[i] == '+')
                continue;
            for (int j = 0; j < k; j++)
                s[i + j] = s[i + j] == '-' ? '+' : '-';
            cnt++;
        }
        for (char c : s)
            if (c == '-')
                cnt = -1;
        cout << "Case #" << t << ": ";
        if (cnt == -1) {
            cout << "IMPOSSIBLE";
        } else {
            cout << cnt;
        }
        cout << '\n';
    }

#ifdef LOCAL
    cerr << "\n== " << 1.0 * clock() / CLOCKS_PER_SEC << " sec.\n";
#endif
    return 0;
}
