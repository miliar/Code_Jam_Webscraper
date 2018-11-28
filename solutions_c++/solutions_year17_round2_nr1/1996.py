#include <cstdio>
#include <iostream>

using namespace std;

int main() {

    int t, n;
    double d, k, s, ans;

    cin >> t;

    for (int i = 0; i < t; i++) {
        cin >> d >> n;
        ans = -1;
        for (int  j = 0; j < n; j++) {
            cin >> k >> s;
            double tmp;
            tmp = (d - k) / s;
            if (tmp > ans) {
                ans = tmp;
            }
        }
        printf("Case #%d: %.6lf\n", i + 1, d / ans);
    }

}