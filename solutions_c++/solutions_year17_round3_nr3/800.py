#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cassert>

using namespace std;

typedef long double ld;

int main() {
    freopen("c1.in", "r", stdin);
    freopen("c1.out", "w", stdout);

    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    cerr << t << endl;
    for (int tt = 1; tt <= t; tt++) {
        cerr << tt << endl;
        int n, k;
        cin >> n >> k;
        assert(n == k);

        ld u;
        cin >> u;
        vector<ld> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        sort(a.begin(), a.end());

        for (int i = 0; i < n; i++) {
            int cnt = i + 1;
            ld nxt = 1;
            if (i + 1 < n) {
                nxt = a[i + 1];
            }
            ld add = min(u / cnt, nxt - a[i]);
            for (int j = 0; j <= i; j++) {
                a[j] += add;
                u -= add;
            }
        }

        ld p = 1;
        for (int i = 0; i < n; i++) {
            p *= a[i];
        }

        cout.precision(20);
        cout << "Case #" << tt << ": " << p << endl;
    }

    return 0;
}