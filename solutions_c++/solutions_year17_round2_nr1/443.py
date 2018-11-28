#include <bits/stdc++.h>
#define foru(i, a, b) for (int i = a; i <= b; i++)
using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int TC;
    scanf("%d", &TC);

    foru(TT, 1, TC) {
        int d, n;
        scanf("%d%d", &d, &n);
        long double ans = 1e18;
        foru(i, 1, n) {
            int k, s;
            scanf("%d%d", &k, &s);
            ans = min(ans, ((long double)d * s) / (d - k));
        }
        cout << "Case #" << TT << ": " << fixed << setprecision(9) << ans << endl;
    }

}
