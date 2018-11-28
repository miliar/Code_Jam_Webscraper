#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    freopen("/home/nimloth/coding/6sem/codejam/C-small-1-attempt0 (1).in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cout.setf(ios::fixed);
    cout.precision(13);
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int n, k;
        double p[55];
        cin >> n >> k;
        double u;
        cin >> u;
        for (int i = 0; i < n; i++) {
            cin >> p[i];
        }
        sort(p, p + n);
        int upd = 1;
        double ans = -1;
        for (int i = 0; i < n - 1; i++) {
            if ((p[i + 1] - p[i]) * upd <= u) {
                u = u - (p[i + 1] - p[i]) * upd;
                upd++;
            } else {
                ans = 1;
                for (int j = 0; j < upd; j++) {
                    ans = ans * (p[i] + (u / upd));
                }
                for (int j = i + 1; j < n; j++) {
                    ans = ans * p[j];
                }
                break;
            }
        }
        if (ans == -1) {
            ans = 1;
            for (int j = 0; j < n; j++) {
                ans = ans * (p[n - 1] + (u / n));
            }
        }
        cout << "Case #" << t + 1 << ": " << ans << "\n";
    }
    return 0;
}