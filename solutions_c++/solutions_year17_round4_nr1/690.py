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
    int n, p;
    cin >> n >> p;
    vector<int> cnt(p);
    forn(i, 0, n) {
        int x;
        cin >> x;
        ++cnt[x % p];
    }
    int ans = cnt[0] + 1;
    for (int i = 1; ; ++i) {
        if (2 * i < p) {
            int x = min(cnt[i], cnt[p - i]);
            ans += x;
            cnt[i] -= x;
            cnt[p - i] -= x;
        } else if (2 * i == p) {
            int x = cnt[i] / 2;
            ans += x;
            cnt[i] -= 2 * x;
        } else break;
    }
    //cerr << ans << ' ';
    forn(i, 1, p) {
        int x = cnt[i] / p;
        ans += x;
    }
    int s = 0;
    forn(i, 0, p) s += i * cnt[i];
    if (s % p == 0) --ans;
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
