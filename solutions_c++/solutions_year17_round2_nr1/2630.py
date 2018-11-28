#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    int n;
    long long d;
    int k[1111], s[1111];
    for (int z = 1; z <= t; z++) {
        long double ans = 0;
        cin >> d >> n;
        for (int i = 1; i <= n; i++) {
            cin >> k[i] >> s[i];
            ans = max(ans, (long double)(1.0 * (d - k[i]) / s[i]));
        }
        cout << "Case #" << z << ": " << fixed << setprecision(6) << (long double)(d / ans) << '\n';
    }
    return 0;
}
