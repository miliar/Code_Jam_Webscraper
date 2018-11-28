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

void printTest(string ans) {
    cout << "Case #" << curT << ": ";
    cout << ans << '\n';
    curT++;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(10);
    cout << fixed;
    srand(566);

    cin >> T;
    while (T--) {
        string num;
        cin >> num;
        int l = 0, r = 1;
        while (r < (int) num.size() && num[r - 1] <= num[r])
            r++;
        if (r == (int) num.size()) {
            printTest(num);
            continue;
        }
        l = r - 1;
        while (l > 0 && num[l] == num[l - 1])
            l--;
        num[l]--;
        for (int i = l + 1; i < (int) num.size(); i++)
            num[i] = '9';
        if (l == 0 && num[l] == '0')
            num = num.substr(1, num.size() - 1);
        printTest(num);
    }

#ifdef LOCAL
    cerr << "\n== " << 1.0 * clock() / CLOCKS_PER_SEC << " sec.\n";
#endif
    return 0;
}
