#include <bits/stdc++.h>
using namespace std;
#define int long long
#undef int
int main()
{
#define int long long
    int T;
    cin >> T;
    for (int I = 1; I <= T; I++) {
        int K, N;
        cin >> K >> N;
        double U;
        cin >> U;
        double p[51];
        double sum = 0.0;
        for (int i = 0; i < N; i++) {
            cin >> p[i];
        }
        assert(K==N);
        double L = 0;
        double R = 1;
        double ans = 0;
        while (fabs(L - R) >= 1e-9) {
            double mid = (L + R) / 2.0;
            double UU = U;
            for (int i = 0; i < N; i++) {
                if (p[i] >= mid)
                    continue;
                UU = UU - (mid - p[i]);
            }
            if (UU < 0) {
                R = mid;
            } else {
                L = mid;
                ans = max(ans, mid);
            }
        }
        double Ans = 1.0;
        for (int i = 0; i < N; i++) {
            if (p[i] >= ans)
                Ans *= p[i];
            else
                Ans *= ans;
        }
        printf("Case #%lld: %.17f\n", I, Ans);
    }
    return 0;
}
