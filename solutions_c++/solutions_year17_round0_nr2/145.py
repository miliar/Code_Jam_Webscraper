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

bool good(ll n) {
    if (n < 10) return true;
    return good(n / 10) && (n % 10 >= n / 10 % 10);
}

ll solve(ll n) {
    if (good(n)) return n;
    return 10 * solve(n / 10 - (n % 10 != 9)) + 9;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    forn(i, 0, t) {
        cout << "Case #" << i + 1 << ": ";
        ll n;
        cin >> n;
        cout << solve(n) << '\n';
    }
}
