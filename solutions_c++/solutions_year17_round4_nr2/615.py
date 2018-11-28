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

int div_up(int a, int b) {
    return (a + b - 1) / b;
}

void solve() {
    int n, c, m;
    cin >> n >> c >> m;
    map<int, int> cnt;
    vector<int> here(n);
    forn(i, 0, m) {
        int id, pos;
        cin >> pos >> id;
        --pos;
        ++cnt[id];
        ++here[pos];
    }
    int ans = 0;
    for (auto p : cnt) {
        ans = max(ans, p.sn);
    }
    int sum = 0;
    forn(i, 0, n) {
        sum += here[i];
        ans = max(ans, div_up(sum, i + 1));
    }
    int free = 0, promote = 0;
    forn(i, 0, n) {
        if (here[i] <= ans) {
            free += ans - here[i];
            continue;
        }
        here[i] -= ans;
        promote += here[i];
        free -= here[i];
    }
    cout << ans << ' ' << promote << '\n';
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
