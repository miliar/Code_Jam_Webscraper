#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=a;i<b;i++)




#define rrep(i,a,b) for(int i=a;i>=b;i--)
int D, N, K[1010], S[1010];
//-----------------------------------------------------------------------------------
double sol() {
    double t = 0;
    rep(i, 0, N) t = max(t, (double)(D - K[i]) / (double)S[i]);
    return D / t;
}
//-----------------------------------------------------------------------------------
int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int T; cin >> T;
    rep(t, 1, T + 1) {
        cin >> D >> N;
        rep(i, 0, N) scanf("%d%d", &K[i], &S[i]);
        printf("Case #%d: %.10f\n", t, sol());
        fprintf(stderr, "Finish : %d\n", t);
    }
}