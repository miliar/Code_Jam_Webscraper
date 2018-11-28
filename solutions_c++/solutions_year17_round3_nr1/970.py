#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>

using namespace std;

typedef long double ld;

int main() {
    freopen("a1.in", "r", stdin);
    freopen("a1.out", "w", stdout);

    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++) {
        int n, k;
        cin >> n >> k;
        vector<pair<ld, ld>> a(n);
        ld mxr = 0;
        for (int i = 0; i < n; i++) {
            ld r, h;
            cin >> r >> h;
            mxr = max(mxr, r);
            a[i] = {r, 2 * M_PI * r * h};
        }
        sort(a.begin(), a.end());

        multiset<ld> st;
        ld sum_st = 0;

        ld best = 0;
        for (int i = 0; i < n; i++) {
            if (st.size() >= k - 1) {
                best = max(best, sum_st + M_PI * a[i].first * a[i].first + a[i].second);
            }

            st.insert(a[i].second);
            sum_st += a[i].second;
            while (st.size() > k - 1) {
                sum_st -= *st.begin();
                st.erase(st.begin());
            }
        }

        cout.precision(20);
        cout << "Case #" << tt << ": " << best << endl;
    }

    return 0;
}