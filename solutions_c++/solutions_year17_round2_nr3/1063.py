#include <bits/stdc++.h>
#define ll long long
#define INF 1000000000
using namespace std;


double dis[123],sp[123],d[123][123],cs[123],dp[123][123];
ll mark[123][123];

double DP(ll idx,ll last){
    if(mark[idx][last]!=-1) return dp[idx][last];
    mark[idx][last]=0;
    ll cost=cs[idx]-cs[last];
    double res=1e18;
    if(cost<=dis[last]){
        res=cost/sp[last];     
        if(last!=1){
            double mn=1e18;
            for(ll j=1;j<last;j++) mn=min(mn,DP(last,j));
            res+=mn;
        }
    }
    return dp[idx][last]=res;
} 

int main()
{   
    freopen("small.in", "r", stdin);
    freopen("small.out", "w", stdout);
    ll ts;cin>>ts;
    ll K=1;
    while(ts--){
        ll n,q,u,v,i,j;cin>>n>>q;
        memset(mark,-1,sizeof(mark));
        for(i=1;i<=n;i++)
            cin>>dis[i]>>sp[i];
        for(i=1;i<=n;i++)
            for(j=1;j<=n;j++){
                cin>>d[i][j];
                dp[i][j]=0;

            }
        for(i=2;i<=n;i++)
            cs[i]=cs[i-1]+d[i-1][i];
        for(i=1;i<=q;i++){
            cin>>u>>v;
        }
        double res=1e18;
        for(i=1;i<n;i++)
            res=min(res,DP(n,i));
        cout.precision(20);
        cout<<"Case #"<<K++<<": "<<res<<endl;
    }

}