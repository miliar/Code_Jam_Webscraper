#include <bits/stdc++.h>

using namespace std;

long long solve(long long x[], long long xx[], long long q, long long y) {
    long long ns = 0;
    long long rofl[1234];
    for (int i = 1; i <= q; i++) rofl[i] = x[i] * xx[i];
    sort(rofl + 1, rofl + q + 1);
    for (int i = q; i >= q - y + 1; i--) ns += rofl[i];
    return ns;
}

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t; cin >> t;
    map <long long, long long> m;
    const double pi  = 3.141592653589793238463;
    for (int z = 1; z <= t; z++) {
        int n; cin >> n;
        int k; cin >> k;
        long long ans = 0;
        long long r[1234], h[1234];
        for (int i = 1; i <= n; i++) {
            cin >> r[i] >> h[i];
            m[r[i]] = h[i];
        }
        sort(r + 1, r + n + 1);
        for (int i = 1; i <= n; i++) h[i] = m[r[i]];
        for (int i = n; i >= k; i--) {
            long long ans2 = 0;
            ans2 += r[i] * r[i];
            ans2 += 2 * solve(r, h, i - 1, k - 1) + 2 * r[i] * h[i];
            ans = max(ans, ans2);
        }
        cout << "Case #" << z << ": " << fixed << setprecision(9) << ans * pi << "\n";
    }
    return 0;
}
