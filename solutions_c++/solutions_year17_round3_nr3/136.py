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

void solve() {
    int n;
    cin >> n >> n;
    ld u;
    cin >> u;
    vector<ld> p(n);
    forn(i, 0, n) cin >> p[i];
    sort(all(p));
    ld ans = 0.0;
    forn(i, 0, n) {
        ld x = 0;
        forn(j, 0, i) x += p[i] - p[j];
        ld rest = u - x;
        if (rest < -eps) continue;
        ld add = rest / (1 + i);
        ld loc = 1.0;
        fore(j, 0, i) loc *= (p[i] + add);
        forn(j, i + 1, n) loc *= p[j];
        ans = max(ans, loc);
    }
    cout << ans << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout << fixed << setprecision(10);
    int t;
    cin >> t;
    fore(i, 1, t) {
        cout << "Case #" << i << ": ";
        solve();
    }
}
