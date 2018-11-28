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
const ld EPS = 1e-8;
const ld PI = acos(-1.0L);

struct ticket {
    int p, b;
    bool operator < (const ticket & o) const {
        return p < o.p;
    }
};

void solve() {
    int n, m, c;
    cin >> n >> c >> m;
    vector<ticket> t;
    vector<int> cb(c);
    vector<int> cp(n);

    int r = 0;
    forn(i, m) {
        int p, b;
        cin >> p >> b;
        p--, b--;
        t.push_back({p, b});
        cb[b]++;
        cp[p]++;
    }
    forn(i, c) {
        r = max(r, cb[i]);
    }
    int sum = 0;
    forn(i, n) {
        sum += cp[i];
        r = max(r, (sum + i)/ (i + 1));
    }
    int p = 0;
    forn(i, n) {
        if (cp[i] > r) {
            p += cp[i] - r;
        }
    }
    cout << r << ' ' << p << '\n';
//    sort(t.begin(), t.end());
}

int main() {
#ifdef LOCAL
    freopen("b.in", "r", stdin);
    //freopen("", "w", stdout);
    //freopen("", "w", stderr);
#endif
    int T;
    cin >> T;
    forn(t, T) {
        printf("Case #%d: ", t +1);
        solve();
    }
    return 0;
}

