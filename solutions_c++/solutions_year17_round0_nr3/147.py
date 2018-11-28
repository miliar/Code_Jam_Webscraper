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
    ll n, k;
    cin >> n >> k;
    map<ll, ll, greater<ll>> dist;
    ++dist[n];
    while (1) {
        assert(!dist.empty());
        auto it = dist.begin();
        ll len = it->first, cnt = it->second;
        dist.erase(it);
        ll len1 = len / 2, len2 = (len - 1) / 2;
        if (k <= cnt) {
            cout << len1 << ' ' << len2 << '\n';
            return;
        }
        k -= cnt;
        dist[len1] += cnt;
        dist[len2] += cnt;
    }
} 

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    forn(i, 0, t) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
}
