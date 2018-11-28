#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define pi pair<ll,ll>
#define pii pair<pi, ll>
#define f first
#define s second
#define ll long long
#define rep(i,n) for(int i=0;i<n;i++)
#define fre freopen("in.txt","r",stdin)
double P[1011];
double U;
int N,K;
bool ok(double m) {
    double cur = 0;
    rep(i,N) {
        cur += max(0.0,m-P[i]);
    }
    if(cur<=U) return 1;
    return 0;
}
int main() {
    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin >> t;
    int cc = 0;
    while(t--){
            cc++;
        cin >> N >> K;
        cin >> U;
        rep(i,N) {
            cin >> P[i];
        }
        double lo = 0;
        double hi = 1+1e-3;
        double mid;
        rep(j,50) {
            mid = (hi+lo)/2;
            if(ok(mid)) lo = mid;
            else hi = mid;
        }
        double ans = 1;
        rep(i,N) {
            ans*=max(lo,P[i]);
        }
        cout << "Case #"<<cc<<": ";
        cout << setprecision(10)<<fixed<<ans <<"\n";
    }
}
