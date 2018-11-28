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


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(10);
    cout << fixed;
    srand(566);

    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        int d, n;
        cin >> d >> n;
        long double time = 0;
        for (int i = 0; i < n; i++) {
            int k, s;
            cin >> k >> s;
            time = std::max(time, (long double) 1.0 * (d - k) / s);
        }
        cout << d / time << '\n';
    }

#ifdef LOCAL
    cerr << "\n== " << 1.0 * clock() / CLOCKS_PER_SEC << " sec.\n";
#endif
    return 0;
}
