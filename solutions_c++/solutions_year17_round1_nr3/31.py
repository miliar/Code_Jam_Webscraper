#include <bits/stdc++.h>
using namespace std;
#define sz(x) ((int) (x).size())
#define forn(i,n) for (int i = 0; i < int(n); ++i)
typedef long long ll;
typedef long long i64;
typedef long double ld;
const int inf = int(1e9) + int(1e5);
const ll infl = ll(2e18) + ll(1e10);

ll Hd, Ad, Hk, Ak, B, D;

ll calc(int nd, int nb) {
    ll hp = Hd;
    ll ad = Ad;
    ll ak = Ak;
    ll hk = Hk;
    bool healed = false;
    ll res = 0;
    forn (i, nd) {
        if (hp - (ak - D) <= 0) {
            if (healed)
                return 1e18;
            healed = true;
            hp = Hd - ak;
            ++res;
            continue;
        }
        ak = max<ll>(ak - D, 0);
        hp -= ak;
        assert(hp > 0);
        ++res;
        healed = false;
    }
    forn (i, nb) {
        if (hp - ak <= 0) {
            if (healed)
                return 1e18;
            healed = true;
            hp = Hd - ak;
            ++res;
            continue;
        }
        ad += B;
        hp -= ak;
        assert(hp > 0);
        ++res;
        healed = false;
    }
    while (hk > 0) {
        if (hk - ad <= 0)
            return res + 1;
        if (hp - ak <= 0) {
            if (healed)
                return 1e18;
            healed = true;
            hp = Hd - ak;
            ++res;
            continue;
        }
        hk -= ad;
        hp -= ak;
        assert(hp > 0);
        ++res;
        healed = false;
    }
    return res;
}

int test = 1;
void solve() {
    cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
    ll res = 1e18;
    forn (nd, 101)
        forn (nb, 101) {
            res = min(res, calc(nd, nb));
        }
    cout << "Case #" << test++ << ": ";
    if (res == 1e18)
        cout << "IMPOSSIBLE\n";
    else
        cout << res << '\n';
}

int main() {
    #ifdef LOCAL
    assert(freopen("c.in", "r", stdin));
    #else
    #endif
    int tn;
    cin >> tn;
    forn (i, tn)
        solve();
}
