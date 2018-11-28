#include <bits/stdc++.h>
#define int long long
#define double long double
#define eps 1e-9

using namespace std;

void solve(int x) {

    double d;
    cin >> d;
    int n;
    cin >> n;
    double s[n], v[n];
    double ans = 1e18;
    for (int i = 0; i < n; i++) {
        cin >>  s[i] >> v[i];
        ans = min(ans, (d / (d - s[i]))  * v[i]);
    }
    cout << "Case #" << x << ':' << ' ';
    cout << fixed << setprecision(12) << ans << '\n';
}

signed main() {
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t = 1;
    cin >> t;
    for (int i = 1; i <= t; i++) solve(i);
    return 0;
}
