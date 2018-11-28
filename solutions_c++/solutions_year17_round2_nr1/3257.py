#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    int t, d, n, k, s;
    double m = -1;
    cin >> t;
    for (int i = 0; i < t; i++) {
        m = -1;
        cin >> d >> n;
        for (int j = 0; j < n; j++) {
            cin >> k >> s;
            double restTime = ((double)d - (double)k) / (double)s;
            m = max(restTime, m);
        }
        printf("Case #%d: %.6lf\n", i+1, d/m);
    }
}