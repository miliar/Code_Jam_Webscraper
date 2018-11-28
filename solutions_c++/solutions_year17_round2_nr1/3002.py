#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int ti=0; ti<T; ti++) {
        int d, n;
        int k[1010], m[1010];
        cin >> d >> n;
        double max_t = 0, t;
        for (int i=0; i<n; i++) {
            cin >> k[i] >> m[i];
            t = 1.0*(d-k[i])/m[i];
            // cout << d-k[i] << "/" << m[i] << "=" << t << endl;
            if (t-max_t > 1e-7) {
                max_t = t;
            }
        }
        // cout << max_t << endl;
        printf("Case #%d: %.6lf\n", ti+1, 1.0*d/max_t);
    }
}
