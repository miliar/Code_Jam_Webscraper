#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mag (ll)1e9
#define mset(x,v) memset(x, v, sizeof(x))
#define inf 1000000000000000000
#define MOD 1000000007
#define dbg1(x) cout<<#x<<" "<<x<<endl;
#define dbg2(x,y) cout<<#x<<" "<<x<<" "<<#y<<" "<<y<<endl;
#define dbg3(x,y,z) cout<<#x<<" "<<x<<" "<<#y<<" "<<y<<" "<<#z<<" "<<z<<endl;
#define dbg4(x,y,z,k) cout<<#x<<" "<<x<<" "<<#y<<" "<<y<<" "<<#z<<" "<<z<<" "<<#k<<" "<<k<<endl;
#define pb push_back

double dis[123],speed[123];
double d[123][123];
double cum[123];
double dp[123][123];
ll vis[123][123];

double solve(ll idx,ll last){
    // cout<<idx<<" "<<last<<endl;
    if(vis[idx][last]!=-1)
        return dp[idx][last];
    vis[idx][last]=0;
    ll cost=cum[idx]-cum[last];
    double ans=1e18;
    //   cout<<"HI";
    if(cost<=dis[last]){
        ans=cost/speed[last];     
        if(last!=1){
            double mn=1e18;
            for(ll j=1;j<last;j++)
                mn=min(mn,solve(last,j));
            ans+=mn;
        }
    }
    return dp[idx][last]=ans;
} 

int main()
{   
    freopen("IP.txt", "r", stdin);
    freopen("OP.txt", "w", stdout);
    ll T;cin>>T;
    ll K=1;
    while(T--){
        ll n,q,u,v,i,j;cin>>n>>q;
        memset(vis,-1,sizeof(vis));
        for(i=1;i<=n;i++)
            cin>>dis[i]>>speed[i];
        for(i=1;i<=n;i++)
            for(j=1;j<=n;j++){
                cin>>d[i][j];
                dp[i][j]=0;

            }
        for(i=2;i<=n;i++)
            cum[i]=cum[i-1]+d[i-1][i];
        for(i=1;i<=q;i++){
            cin>>u>>v;
        }
        double ans=1e18;
        for(i=1;i<n;i++)
            ans=min(ans,solve(n,i));
        cout.precision(20);
        cout<<"Case #"<<K++<<": "<<ans<<endl;
    }

}
