#include <bits/stdc++.h>

using namespace std;

int main() {
//    freopen("sample.in", "r", stdin);
//    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin >> tc;
    for (int ti = 1; ti <= tc; ++ti) {
        printf("Case #%d: ", ti);
        long long d; 
        int n;
        cin >> d; cin >> n;
        vector<pair<int, long long>> h(n);
        for (int i = 0; i < n; ++i) {
            int ki, si;
            cin >> ki >> si;
            h[i] = {d-ki, si*d};
        }
        long double lo = 0, ri = 1e18;

        for (int it = 0; it < 333; ++it) {
            long double mid = (lo+ri)*0.5;
            bool ok = true;
            for (int i = 0; i < n; ++i) {
                if (h[i].first*mid > h[i].second) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                lo = mid;
            }
            else {
                ri = mid;
            }
        }

        printf("%.7Lf\n", lo);
    }
    return 0;
}
