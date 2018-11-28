#include <bits/stdc++.h>

using namespace std;

int true_main (int test) {
    int d, n;
    cin >> d >> n;

    double ans = 0;
    for (int i = 0; i < n; ++i) {
        double k, s;
        cin >> k >> s;
        ans = max(ans, (d - k) / s);
    }

    cout.precision(6);
    cout << "Case #" << test << ": " << fixed << d / ans << "\n";
}

main () {
#define FILES
#ifdef FILES
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t) {
        true_main(t);
    }
}
