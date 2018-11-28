#include "bits/stdc++.h"
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define rep(i,n) for(ll i=0;i<(ll)(n);i++)
#define all(a)  (a).begin(),(a).end()
#define pb emplace_back
//#define INF (1e9+1)
#define INF (1LL<<59)

#define int ll

signed main(){
    int T;
    cin>>T;
    rep(t,T){
        int n,q;
        cin>>n>>q;
        assert(q==1);
        vector<int> e(n),s(n);
        rep(i,n){
            cin>>e[i]>>s[i];
        }
        
        int dist[101][101];
        rep(i,n){
            rep(j,n){
                cin>>dist[i][j];
            }
        }
        
        vector<int> u(q),v(q);
        rep(i,q){
            cin>>u[i]>>v[i];
        }
        
        vector<int> d(n,0);
        for(int i=1;i<n;i++){
            d[i] = d[i-1]+dist[i-1][i];
        }
        
        double dp[101];
        rep(i,101)dp[i]=INF;
        
        dp[0] = 0;
        rep(i,n-1){
            for(ll j=i+1;j<n;j++){
                if(d[j]-d[i]>e[i])break;
                dp[j] = min( dp[j] , dp[i]+(double)(d[j]-d[i])/s[i] );
            }
        }
        cout<<"Case #"<<t+1<<": ";
        printf("%.20lf\n",dp[n-1]+(1e-9));
    }
}