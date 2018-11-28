#include <bits/stdc++.h>

using namespace std;

const long double inf = 1e18;

void solve() {
    int d, n;
    cin >> d >> n;
    vector<pair<long double, long double>> a(n);
    for (int i = 0; i < n; ++i)
        cin >> a[i].first >> a[i].second;
    sort(a.begin(), a.end());
    a.push_back({d, 0});
    vector<long double> b(n, inf);
    for (int i = n - 1; i >= 0; --i) {
        for (int j = i + 1; j <= n; ++j) {
            long double dist = a[j].first - a[i].first;
            long double t = dist / (a[i].second - a[j].second);
            if (t <= 0)
                t = inf;
            b[i] = min(b[i], t);
        }
    }
    long double tl = 0, tr = inf;
    for (int iter = 0; iter < 100; ++iter) {
        long double tm = (tl + tr) / 2;
        bool ok = true;
        for (int i = 0; i < n; ++i) {
            long double dist = a[i].first;
            long double t = dist / (tm - a[i].second);
            if (t > 0 && t < b[i])
                ok = false;
        }
        if (ok)
            tl = tm;
        else tr = tm;
    }
    cout << fixed << setprecision(6) << tl;
}

int main() {
#ifdef __APPLE__
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int t = 1;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cerr << "Case #" << i << " is working\n";
        cout << "Case #" << i << ": ";
        solve();
        cout << "\n";
        cerr << "Case #" << i << " is done\n";
    }

    return 0;
}

