#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=a;i<b;i++)




int N, Q, E[101], S[101], D[101][101], U[101], V[101];
//-----------------------------------------------------------------------------------
double dp[101];
#define INF 1e18
#define rrep(i,a,b) for(int i=a;i>=b;i--)
typedef long long ll;
void sol() {
    cin >> N >> Q;
    rep(i, 0, N) cin >> E[i] >> S[i];
    rep(y, 0, N) rep(x, 0, N) cin >> D[y][x];
    rep(i, 0, Q) cin >> U[i] >> V[i];
    rep(i, 0, Q) U[i]--, V[i]--;

    rep(q, 0, Q) {
        rep(i, 0, N) dp[i] = INF;
        dp[0] = 0;
        
        rep(i, 1, N) {
            ll sm = 0;
            rrep(j, i - 1, 0) {
                sm += D[j][j + 1];
                if (sm <= E[j]) dp[i] = min(dp[i], dp[j] + (double)sm / S[j]);
            }
        }

        printf("%.10f", dp[N-1]);
        if (q != Q - 1) printf(" ");
        else printf("\n");
    }
}
//-----------------------------------------------------------------------------------
int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int T; cin >> T;
    rep(t, 1, T + 1) {
        printf("Case #%d: ", t);
        sol();
        fprintf(stderr, "Finish : %d\n", t);
    }
}