#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ull = unsigned long long;
using ld = long double;

#define forn(i, a, n) for (int i = a; i < n; ++i)
#define ford(i, a, n) for (int i = n - 1; i >= a; --i)
#define fore(i, a, n) for (int i = a; i <= n; ++i)
#define all(a) (a).begin(), (a).end()
#define fs first
#define sn second
#define trace(a)\
    for (auto i : a) cerr << i << ' ';\
    cerr << '\n'
#define eb emplace_back

#ifndef M_PI
const ld M_PI = acos(-1.0);
#endif

const ld eps = 1e-9;
const int INF = 2000000000;
const ll LINF = 1ll * INF * INF;
const ll MOD = 1000000007;

const int TIME = 24 * 60;

void solve() {
    int a, b;
    cin >> a >> b;
    vector<tuple<int, int, int>> e;
    forn(i, 0, a) {
        int st, fin;
        cin >> st >> fin;
        e.eb(st, fin, 0);
    }
    forn(i, 0, b) {
        int st, fin;
        cin >> st >> fin;
        e.eb(st, fin, 1);
    }
    sort(all(e));
    vector<int> tm(2, 0);
    for (auto q : e) {
        int st, fin, tp;
        tie(st, fin, tp) = q;
        tm[tp] += fin - st;
    }
    int ans = a + b;
    forn(i, 0, a + b - 1)
        if (get<2>(e[i]) == get<2>(e[i + 1])) ++ans;
    if (get<2>(e[0]) == get<2>(e.back())) ++ans;
    forn(TP, 0, 2) {
        multiset<int> times;
        forn(i, 0, a + b - 1) {
            if (get<2>(e[i]) == TP && get<2>(e[i + 1]) == TP) {
                times.insert(get<0>(e[i + 1]) - get<1>(e[i]));
            }
        }
        if (get<2>(e[0]) == TP && get<2>(e.back()) == TP) {
            times.insert(TIME + get<0>(e[0]) - get<1>(e.back()));
        }
        while (!times.empty()) {
            auto it = times.begin();
            if (tm[TP] + *it <= TIME / 2) {
                ans -= 2;
                tm[TP] += *it;
                times.erase(it);
            } else break;
        }
    }
    cout << ans << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    fore(i, 1, t) {
        cout << "Case #" << i << ": ";
        solve();
    }
}
