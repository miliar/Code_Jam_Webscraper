#include <bits/stdc++.h>

using namespace std;

const long double EPS = 1e-9;
const int MAX_N = 100;

int tc, n;
double u;
double p[MAX_N];

int main() {
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cout.precision(20);
    cin >> tc;
    for (int t = 0; t < tc; t++) {
        cout << "Case #" << t + 1 << ": ";
        cin >> n >> n >> u;
        for (int i = 0; i < n; i++) {
            cin >> p[i];
        }
        sort(p, p + n);
        for (int i = 0; i < n; i++) {
            long double nx = 1;
            if (i != n - 1) {
                nx = p[i + 1];
            }
            long double pl = (long double) u / (long double) (i + 1);
            if (pl < EPS) {
                break;
            }
            if (p[i] + pl + EPS < nx) {
                for (int j = 0; j <= i; j++) {
                    p[j] += pl;
                }
                break;
            }
            for (int j = 0; j <= i; j++) {
                u -= nx - p[j];
                p[j] = nx;
            }
        }
        long double ans = 1;
        for (int i = 0; i < n; i++) {
            ans *= (long double) p[i];
        }
        cout << (double) ans << "\n";
    }
}


