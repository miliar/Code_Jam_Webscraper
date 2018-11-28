// Nurbakyt Madibek
// Look at my code! IT'S AWESOME

#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <ctime>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <cassert>
#include <unordered_map>
#include <bitset>
#include <unordered_set>

using namespace std;

#define pb push_back
#define pp pop_back
#define f first
#define s second
#define mp make_pair
#define sz(a) (int)((a).size())
#ifdef _WIN32
#  define I64 "%I64d"
#else
#  define I64 "%lld"
#endif
#define fname "."

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair < int, int > pi;

const int mod = (int)1e9 + 7;
const int inf = (int)1e9 + 123;
const ll infl = (ll)1e18 + 123;
const double eps = 1e-6;

const int MAX_N = (int)1e5 + 123;

int n, p;
int r[100];
int q[100][100];

pi get(int x, int need) {
    int l = 1, r = (int)1e6, mid = -1, L = -1, R = -1;
    while(l <= r) {
        mid = (l + r) / 2;
        if (1ll * need * 10 <= 1ll * mid * x * 11) {
            L = mid;
            r = mid - 1;
        }
        else
            l = mid + 1;
    }
    
    l = 1, r = (int)1e6, mid = -1;
    while(l <= r) {
        mid = (l + r) / 2;
        if (1ll * need * 10 >= 1ll * mid * x * 9) {
            R = mid;
            l = mid + 1;
        }
        else
            r = mid - 1;
    }
//    cout << x << " and " << need << " is " << L << ' '<< R << endl;
    if (L == -1 || R == -1 || L > R)
        return mp(-1, -1);
    return mp(L, R);
}

struct num {
    int row, col, x, tp, right;
};

bool cmp(const num &a, const num &b) {
    if (a.x != b.x)
        return a.x < b.x;
    return a.tp < b.tp;
}

vector < num > st;

set < pair < int, pi > > t[100];

void solve() {
    cin >> n >> p;
    for (int i = 1; i <= n; i++)
        cin >> r[i];
    st.clear();
    int mini = inf, maxi = -inf;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= p; j++) {
            scanf("%d", &q[i][j]);
            pi seg = get(r[i], q[i][j]);
            if (seg.f == -1)
                continue;
//            cout << i << ' ' << j << " is " << seg.f << ' '<< seg.s << endl;
            mini = min(mini, seg.f), maxi = max(maxi, seg.s);
            st.pb(num({i, j, seg.f, -1, seg.s}));
            st.pb(num({i, j, seg.s, 1, -1}));
        }
    }
    if (mini != inf)
        for (int i = mini; i <= maxi; i++)
            st.pb(num({-1, -1, i, 0, -1}));
    sort(st.begin(), st.end(), &cmp);
    int ans = 0;
    for (int i = 1; i <= n; i++)
        t[i].clear();
    int cnt = n;
    for (auto i : st) {
        if (i.tp == -1) {
            if (t[i.row].empty())
                cnt--;
            t[i.row].insert(mp(i.right, mp(i.row, i.col)));
        }
        else if (i.tp == 0) {
            while(cnt == 0) {
//                bool bad = 0;
//                for (int j = 1; j <= n; j++)
//                    if (t[j].empty()) {
//                        bad = 1;
//                        break;
//                    }
//                if (bad)
//                    break;
                ans++;
                for (int j = 1; j <= n; j++) {
                    assert(!t[j].empty());
                    if (sz(t[j]) == 1)
                        cnt++;
                    t[j].erase(t[j].begin());
                }
            }
        }
        else {
            int sz = sz(t[i.row]);
            t[i.row].erase(mp(i.x, mp(i.row, i.col)));
            if (sz > 0 && sz(t[i.row]) == 0)
                cnt++;
        }
    }
    cout << ans << endl;
}

int main() {
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base :: sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int tests;
    cin >> tests;
    for (int it = 1; it <= tests; it++) {
        cout << "Case #" << it << ": ";
        solve();
    }
    return 0;
}
