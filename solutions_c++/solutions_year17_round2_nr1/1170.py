#include <bits/stdc++.h>

using namespace std;
typedef unsigned long long ll;
typedef long double ld;
const double PI = acos(-1.);


int main() {
    freopen("/home/york_io/Documents/Code/contest/in.txt", "r", stdin);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        ll d, n;
        cin >> d >> n;
        vector<pair<ll, ll>> horses(n);
        for (int i = 0; i < n; ++i) {
            cin >> horses[i].first >> horses[i].second;
        }
        sort(horses.rbegin(), horses.rend());
        double time = 0.;
        for (int i = 0; i < n; ++i) {
            double tmp = (double) (d - horses[i].first) / horses[i].second;
            time = max(time, tmp);
        }
        double ans = (double) d / time;
        cout.precision(10);
        cout << fixed << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}