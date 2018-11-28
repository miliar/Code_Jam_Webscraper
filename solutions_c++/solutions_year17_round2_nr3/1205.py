#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ld = long double;

int n;
int e[1000];
int s[1000];
int d[1000][1000];
ld r[1000];
int q;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int TT;
    cin >> TT;
    for (int T = 0; T < TT; ++T) {
        cout << "Case #" << T + 1 << ": ";
        cin >> n >> q;
        for (int i = 0; i < n; ++i) {
            cin >> e[i] >> s[i];
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> d[i][j];
            }
        }
        cin >> q >> q;

        for (int i = 1; i < n; ++i) {
            r[i] = -1;
        }
        r[0] = 0;
        for (int i = 0; i < n; ++i) {
            int dst = 0;
            for (int j = i + 1; j < n; ++j) {
                dst += d[j - 1][j];
                if (dst > e[i]) {
                    break;
                }
                ld c_r = static_cast<ld>(dst) / s[i] + r[i];
                if (r[j] > c_r || r[j] < 0) {
                    r[j] = c_r;
                }
            }
        }
        cout << fixed << setprecision(10) << r[n - 1] << "\n";
    }
    return 0;
}
