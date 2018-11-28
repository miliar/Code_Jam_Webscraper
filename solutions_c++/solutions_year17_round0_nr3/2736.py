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

int T, curT = 1;

void printTest(int64_t l, int64_t r) {
    cout << "Case #" << curT++ << ": " << l << ' ' << r << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(10);
    cout << fixed;
    srand(566);

    cin >> T;
    while (T--) {
        int64_t n, k;
        cin >> n >> k;
        
        map<int64_t, int64_t> cnt;
        cnt[n] = 1;
        while (true) {
            auto max = *std::max_element(all(cnt));
            if (k <= max.second) {
                printTest(max.first / 2, (max.first - 1) / 2);
                break;
            }
            k -= max.second;
            cnt[max.first / 2] += max.second;
            cnt[(max.first - 1) / 2] += max.second;
            cnt.erase(max.first);
        }
    }

#ifdef LOCAL
    cerr << "\n== " << 1.0 * clock() / CLOCKS_PER_SEC << " sec.\n";
#endif
    return 0;
}
