#include <bits/stdc++.h>

using namespace std;

int main () {
    int t, caso = 1;
    scanf ("%d", &t);
    while (t--) {
        int d, n;
        scanf ("%d %d", &d, &n);
        double mx = 1.0e-9;
        for (int i = 0; i < n; i++) {
            int k, s;
            scanf ("%d %d", &k, &s);
            mx = max (mx, (double) (d - k) / s);
        }
        printf ("Case #%d: %lf\n", caso++, (double) d / mx);
    }
    return 0;
}
