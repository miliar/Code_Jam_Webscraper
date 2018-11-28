#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    int t;
    cin >> t;
    for (int test = 1; test <= t; ++test) {
        int d, n;
        cin >> d >> n;
        double max_t = 0;
        for (int i = 0; i < n; ++i) {
            int s, k;
            cin >> s >> k;
            double t = double(d - s)/double(k);
            if (t > max_t) {
                max_t = t;
            }
        }

        printf("Case #%d: %.6f\n", test, double(d)/max_t);
    }

    return 0;
}
