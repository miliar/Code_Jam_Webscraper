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
    ll n, k;
    cin >> n >> k;
    map<ll, ll> q;
    q[n] = 1;
    for (auto it = q.rbegin(); it != q.rend(); it++) {
        ll hl = it->first / 2, hr = (it->first - 1)/2;
        k -= it->second;
        if (k <= 0) {
            cout << hl << ' ' << hr;
            return;
        }
        q[hl] += it->second;
        q[hr] += it->second;
    }
    assert(false);
}

int main() {
#ifdef LOCAL
    freopen("c.in", "r", stdin);
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

