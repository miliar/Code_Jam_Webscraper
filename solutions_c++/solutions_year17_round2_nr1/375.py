#include <bits/stdc++.h>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int n;
        long double d;
        cin >> d >> n;
        vector<pair<int, int>> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i].first >> a[i].second;
        }
        sort(a.begin(), a.end());
        long double l = 1e-8, r = 1e20;
        while ((r - l)/max((long double)1.0, l) > 1e-8) {
            auto mid = (l+r)/2;
            auto my = d / mid;
            bool ok = true;
            for (auto pr : a) {
                double h = (d-pr.first) / pr.second;
                if (h > my) {
                    ok = false;
                }
            }
            //cout << "-> " << r << " " << l << endl;
            if (ok) {
                l = mid;
            } else {
                r = mid;
            }
        }
        cout << fixed << setprecision(10) << "Case #" << t << ": " << l << endl;
    }
}



