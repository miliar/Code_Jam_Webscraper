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

inline ll sq(ll x) {
    return x * x;
}

void solve() {
    int n, k;
    cin >> n >> k;
    vector<pair<ll, ll>> x(n);
    forn(i, 0, n) {
        ll r, h;
        cin >> r >> h;
        x[i] = {r, r * h};
    }
    sort(all(x));
    //reverse(all(x));
    multiset<ll> good;
    ll sum = 0;
    forn(i, 0, k) {
        good.insert(x[i].sn);
        sum += x[i].sn;
    }
    ll ans = 2 * sum + sq(x[k - 1].fs);
    forn(i, k, n) {
        ll bad = *good.begin();
        good.insert(x[i].sn);
        sum += x[i].sn;
        ans = max(ans, 2 * (sum - bad) + sq(x[i].fs));
        auto it = good.begin();
        sum -= *it;
        good.erase(it);
        //cerr << ans << '\n';
    }
    cout << M_PI * ans << '\n';
}

void solve2() {
    int n, k;
    cin >> n >> k;
    vector<pair<ll, ll>> x(n);
    forn(i, 0, n) {
        cin >> x[i].fs >> x[i].sn;
    }
    ll ans = 0;
    forn(m, 0, (1 << n)) {
        vector<pair<ll, ll>> q;
        forn(i, 0, n) if (m & (1 << i))
            q.eb(x[i]);
        if (q.size() != k) continue;
        sort(all(q));
        ll loc = 0;
        forn(i, 0, k) loc += 2 * q[i].fs * q[i].sn;
        loc += q.back().fs * q.back().fs;
        ans = max(ans, loc);
    }
    cout << M_PI * ans << '\n';
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
