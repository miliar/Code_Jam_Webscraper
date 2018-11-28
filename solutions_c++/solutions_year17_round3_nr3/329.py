#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#define For(i, n) for(int i = 0; i < (n); i ++)
using namespace std;
const int M = 60;
double p[M];
int main() {
    ios::sync_with_stdio(0);
    int t; cin >> t;
    for (int tc = 1; tc <= t; tc ++) {
        int n, k;
        double u;
        cin >> n >> k >> u;
        For(i, n) cin >> p[i];
        sort(p, p + n);
        For(i, n) {
            double x = 0;
            For(j, i)
                x += p[i] - p[j];
            if (x > u || i == n - 1) {
                if (x > u) i--;
                For (j, i) {
                    u -= p[i] - p[j];
                    p[j] = p[i];
                }
                For(j, i + 1)
                    p[j] += u / (i + 1);
                break;
            }
        }
        double ans = 1;
        For(i, n) ans *= p[i];
        cout << "Case #" << tc << ": ";
        cout << setprecision(8) << fixed << ans << endl;
    }
    return 0;
}
