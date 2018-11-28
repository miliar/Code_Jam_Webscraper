#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ld = long double;

#define __fail() cout << "IMPOSSIBLE\n"; continue;

int n, k;
ld u;
ld p[100];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int TT;
    cin >> TT;
    for (int T = 0; T < TT; ++T) {
        cerr << T << endl;
        cout << "Case #" << T + 1 << ": ";
        cin >> n >> k >> u;
        for (int i = 0; i < n; ++i) {
            cin >> p[i];
        }
        p[n] = 1;
        ++n;
        sort(p, p + n);
        ld avg = p[0];
        int avg_c = 1;
        for (int i = 1; i < n; ++i) {
            if (u > 1e-7) {
                ld can_p = u / avg_c;
                if (can_p < p[i] - avg) {
                    avg += can_p;
                    u = 0;
                    break;
                } else {
                    u -= (p[i] - avg) * avg_c;
                    avg = p[i];
                    ++avg_c;
                }
            } else {
                break;
            }
        }
        ld res = 1;
        for (int i = 0; i < avg_c; ++i) {
            res *= avg;
        }
        for (int i = avg_c; i < n; ++i) {
            res *= p[i];
        }

        cout << fixed << setprecision(10) << res << "\n";
    }

    return 0;
}