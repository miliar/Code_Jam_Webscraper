#include <bits/stdc++.h>
using namespace std;

// IOI 2018

int t;
long long n, k, cur, v0, v1;
map<long long, bool> g;
map<long long, long long> f;

long long cal(long long x) {
    if (x == v0) return 0;
    if (x == v1) return 1;
    if (f.count(x)) return f[x];
    f[x] = cal((x - 1) / 2) + cal(x - 1 - (x - 1) / 2);
}

int main() {
    freopen("C_in.txt", "r", stdin);
    freopen("C_out.txt", "w", stdout);
    ios::sync_with_stdio(false);
    cin >> t;
    for (int T = 1; T <= t; ++T) {
        cin >> n >> k;
        f.clear(), g.clear();
        cur = 1, v0 = v1 = n;
        while (1) {
            if (k <= cur) {
                g[v0] = g[v1] = 1; break;
            }
            k -= cur; cur *= 2;
            v0 = (v0 - 1) / 2, v1 = v1 - 1 - (v1 - 1) / 2;
        }
        cal(n);
        cout << "Case #" << T << ": ";
        if (f[n] >= k) {
            cout << (v1 - 1 - (v1 - 1) / 2) << ' ' << ((v1 - 1) / 2) << '\n';
        }
        else {
            cout << (v0 - 1 - (v0 - 1) / 2) << ' ' << ((v0 - 1) / 2) << '\n';
        }
    }
}
