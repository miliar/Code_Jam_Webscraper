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
const int MAXN = 1e5;

void tfill(string &s) {
    int n = s.length();
    int f = 0;
    while (f < n && s[f] == '?')
        f++;
    assert(f < n);
    forn(i, f)
        s[i] = s[f];
    f++;
    while (f < n) {
        if (s[f] == '?') {
            s[f] = s[f - 1];
        }
        f++;
    }
}
void solve() {
    int r, c;
    cin >> r >> c;
    vector<string> t;
    forn(i, r) {
        string s;
        cin >> s;
        t.pb(s);
    }
    string emp = "";
    forn(i, c)
        emp += '?';
    int f = 0;
    while (f < r && t[f] == emp) {
        f++;
    }
    assert(f < r);
    tfill(t[f]);
    forn(i, f) {
        assert(t[i] == emp);
        t[i] = t[f];
    }
    f++;
    while (f < r) {
        if (t[f] == emp) {
            t[f] = t[f - 1];
        } else {
            tfill(t[f]);
        }
        f++;
    }
    cout << '\n';
    forn(i, r)
        cout << t[i] << '\n';
}

int main() {
#ifdef LOCAL
    freopen("a.in", "r", stdin);
    //freopen("", "w", stdout);
    //freopen("", "w", stderr);
#endif
    int T;
    cin >> T;
    forn(i, T) {
        printf("Case #%d:", i + 1);
        solve();
    }
    return 0;
}

