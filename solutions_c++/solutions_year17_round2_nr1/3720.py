#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A.txt", "w", stdout);
    long long t, n, d, x, y;
    int cases = 1;
    cin >> t;
    while (t--) {
        cin >> d >> n;
        double ans = 0.0;
        for (int i=0;i<n;i++) {
            cin >> x >> y;
            ans = max(ans, (d - x + 0.0) / y);
        }
        printf ("Case #%d: %.6f\n", cases++, d/ans);
    }
    return 0;
}
