#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
#define  ll long long
#define pi pair<ll,ll>
#define f first
#define s second
pi R[1011];
ll dp[1011][1011];
ll sdp[1011];
int main() {
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin >> t;
    int N,K;
    double PII = 4* atan(1);
    rep(cc,t) {
        cin >> N >> K;
        rep(i,N) {
            cin >> R[i].f >> R[i].s;
        }
        sort(R,R+N);
        reverse(R,R+N);
        rep(i,N) {
            dp[i][1] = R[i].f*R[i].f + 2*R[i].f * R[i].s;
        }
        rep(i,K+1) {
            sdp[i] = -1e18;
        }
        sdp[0] = 0;
        rep(i,N) {
            for(int j=2;j<=min(K,i+1);j++) {
                dp[i][j] = 2* R[i].f*R[i].s + sdp[j-1];
            }
            for(int j=1;j<=min(K,i+1);j++) sdp[j] = max(sdp[j],dp[i][j]);
        }
        double ans = PII * sdp[K];
        cout << "Case #" << cc+1 << ": ";
        cout << setprecision(10) << fixed << ans << "\n";
     }
}
