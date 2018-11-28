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

const ll INF = 1e18;
const ld eps = 1e-10;
const ld PI = acos(-1.0L);
const int MAXN = 1e5;

int hd, ad, hk, ak, b, d;

ll emul(int k, int t) {
   // cerr << "emul " << k << ' ' << t << '\n';
    int a = ak;
    int h = hd;
    ll ans = 0;
    while (k > 0) {
        if (t > 0 && h > a - d) {
            t--;
            a -= d;
            if (a < 0)
                a = 0;
        } else if (k > 1 && h <= a) {
            h = hd;
        } else {
            k--;
        }
        h -= a;
        assert(k == 0 || h > 0);
        ans++;
    }
    return ans;
}
void solve() {
    cin >> hd >> ad >> hk >> ak >> b >> d;
    if (ad >= hk) {
        cout << 1;
        return;
    }
    if (ak < hd && max(2 * ad, ad + b) >= hk) {
        cout << 2;
        return;
    }
    if (ak - d >= hd || 2 * ak - 3 * d >= hd) {
        cout << "IMPOSSIBLE";
        return;
    }
    int k = (hk +ad - 1)/ ad;
    if (b > 0) {
        int cnt = 0;
        do {
            ad += b;
            cnt++;
            k = min(k, cnt + (hk + ad - 1) / ad);
        } while (ad < hk);
    }
    assert(k >= 3);
//    cerr << "K " << k << '\n';
    ll ans = INF;
    if (2 * ak < hd) {
        ans = min(ans, emul(k, 0));
    }
    if (2 * ak - 2 * d < hd) {
        ans = min(ans, emul(k, 1));
    }

    if (d > 0) {
        for (int i = 2; i <= ak; ++i) {
            ans = min(ans, emul(k, i));
        }
    }
    cout << ans;
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

