#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=a;i<b;i++)


int N, K;
double U, P[51];
void sol() {
    cin >> N >> K >> U;
    rep(i, 0, N) cin >> P[i];
    P[N] = 1;

    sort(P, P + N);
    rep(i, 0, N) {
        double c = U / (i + 1);
        double d = P[i + 1] - P[i];
        if (d <= c) {
            rep(j, 0, i + 1) P[j] = P[i + 1];
            U -= d * (i + 1);
        } else {
            rep(j, 0, i + 1) P[j] += c;
            break;
        }
    }

    double ans = 1;
    rep(i, 0, N) ans *= P[i];
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