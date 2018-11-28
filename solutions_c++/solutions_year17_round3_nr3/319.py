#include <iostream>
#include <iomanip>

using namespace std;

int t, n, k;
double u, p[51], E = 1e-7;

int main() {
    cin >> t;
    for (int c = 0; c ++< t;) {
        cin >> n >> k >> u;
        for (int i = 0; i < n; ++i) cin >> p[i];
        sort(p, p + n);
        p[n] = 1;
        for (int i = 0; i < n && u > E; ++i) {
            double d = p[i+1] - p[i];
            double a = min(u, d * (i + 1));
            u -= a;
            a /= i + 1;
            for (int j = 0; j <= i; ++j) p[j] += a;
        }
        double x = 1;
        for (int i = 0; i < n; ++i) x *= p[i];
        cout << "Case #" << c << ": " << fixed << setprecision(6) << x << '\n';
    }
}
