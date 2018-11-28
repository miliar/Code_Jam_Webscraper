#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=a;i<b;i++)


#define pi 2*acos(0.0)
int N, K, R[1010], H[1010];
int ord[1010];
void sol() {
    cin >> N >> K;
    rep(i, 0, N) scanf("%d%d", &R[i], &H[i]);

    rep(i, 0, N) ord[i] = i;
    sort(ord, ord + N, [&](int a, int b) {
        double aa = 1.0 * H[a] * R[a] * 2 * pi;
        double bb = 1.0 * H[b] * R[b] * 2 * pi;
        return aa > bb;
    });

    double ans = 0;
    rep(i, 0, N) {
        int ma = 0, f = 0;
        double a = 0;

        ma = max(ma, R[i]);
        a += 1.0 * H[i] * R[i] * 2 * pi;

        rep(_k, 0, K - 1) {
            int k = ord[_k];
            if (k == i) {
                f = 1;
                continue;
                
            }

            ma = max(ma, R[k]);
            a += 1.0 * H[k] * R[k] * 2 * pi;
        }
        if (f) {
            int k = ord[K - 1];
            ma = max(ma, R[k]);
            a += 1.0 * H[k] * R[k] * 2 * pi;
        }

        a += 1.0 * ma * ma * pi;

        ans = max(ans, a);
    }

    printf("%.10f\n", ans);
}
//-----------------------------------------------------------------------------------
int main() {
    int T; cin >> T;
    rep(t, 0, T) {
        printf("Case #%d: ", t + 1);
        sol();
    }
}