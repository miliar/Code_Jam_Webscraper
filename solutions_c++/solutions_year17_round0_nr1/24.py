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

void solve() {
    string s;
    int k;
    cin >> s >> k;
    int n = s.length();
    vector<bool> b;
    for (auto c : s) {
        b.pb(c == '+');
    }
    int ans = 0;
    for(int i = 0; i <= n - k; ++i) {
        if (!b[i]) {
            for (int j = i; j < i + k; ++j) {
                b[j] = !b[j];
            }
            ans++;
        }
    }
    for (int i = n - k + 1; i < n; ++i) {
        if (!b[i]) {
            cout << "IMPOSSIBLE";
            return;
        }
    }
    cout << ans;
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
        printf("Case #%d: ", i + 1);
        solve();
        printf("\n");
    }

    return 0;
}

