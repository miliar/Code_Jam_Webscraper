#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <string>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <cassert>
#include <queue>
#include <bitset>

using namespace std;

#define FOR(a, b) for (int a = 0; a < (b); ++a)
#define clr(a) memset(a, 0, sizeof(a))
#define pb push_back
#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)
#ifdef LOCAL
#define debug(a) cerr << #a << ": " << a << '\n';
#else
#define debug(a)
#endif

typedef long long ll;
typedef long double ld;

const int INF = 1e9;
const ld eps = 1e-10;
const ld PI = acos(-1.0L);
const int MAXN = 1e5;
struct seg {
    int l, r;
    bool operator < (const seg & o) const {
        if (r != o.r)
            return r < o.r;
        return l < o.l;
    }
};

void solve() {
    int n, m;
    cin >> n >> m;
    vector<int> r(n);
    forn(i, n) {
        cin >> r[i];
    }
    vector<vector<seg>> s(n);
    forn(i, n) {
        forn(j, m) {
            int q;
            cin >> q;
            seg cur = {(10 * q + 11 * r[i] - 1) / (11 * r[i]), 10 * q / (9 * r[i])};
            if (cur.l <= cur.r)
                s[i].push_back(cur);
        }
        sort(s[i].begin(), s[i].end());
    }
    vector<int> p(n);
    int ans = 0;
    while (true) {
        seg inter = {0, INF};
        int mi = 0;
        forn(i, n) {
            if (p[i] >= s[i].size()) {
                goto stop;
            }
            inter.l = max(inter.l, s[i][p[i]].l);
            if (inter.r > s[i][p[i]].r) {
                inter.r = s[i][p[i]].r;
                mi = i;
            }
        }
        if (inter.l <= inter.r) {
            ans++;
            forn(i, n)
                p[i]++;
        } else {
            p[mi]++;
        }
    }
stop:
    cout << ans;
}

int main() {
#ifdef LOCAL
    freopen("b.in", "r", stdin);
    //freopen("", "w", stdout);
    //freopen("", "w", stderr);
#endif
    int T;
    cin >> T;
    forn(i, T) {
        printf("Case #%d: ", i + 1);
        solve();
        printf("\n");
    }
    return 0;
}

