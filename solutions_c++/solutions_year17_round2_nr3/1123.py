#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
using namespace std;

typedef long long ll;
typedef pair<ll,ll> ii;
typedef vector<ll> vll;

#define inst freopen("in.txt", "r", stdin)
#define oust freopen("out.txt", "w", stdout)

ll n,q;
ii arr[109];
ll dis[109][109];
double dp[109][109];
int vis[109][109];
ll sum[109];
double inf = 1e16;

double hic(ll pos, ll hn) {
    //cout<<pos<<" "<<hn<<endl;
    double &res = dp[pos][hn];
    if(vis[pos][hn]!=-1) return res;
    if(pos==n) return 0;
    ll discov = sum[pos] - sum[hn];
    res = inf;
    if(arr[hn].first - discov >= dis[pos][pos+1]) res = dis[pos][pos+1]*1.0/arr[hn].second+hic(pos+1,hn);
    double x = inf;
    if(arr[pos].first >= dis[pos][pos+1]) x = dis[pos][pos+1]*1.0/arr[pos].second+hic(pos+1,pos);
    if(x<res) res=x;
    if(res>inf) res=inf;
    vis[pos][hn]=1;
    return res;
}

int main() {
    inst;oust;
    ll t, cs = 1;
    cin>>t;
    while(t--) {
        cin>>n>>q;
        for(int i=1;i<=n;i++) cin>>arr[i].first>>arr[i].second;
        for(int i = 1;i<=n;i++) {
            for(int j=1;j<=n;j++) cin>>dis[i][j];
        }
        int foo,bar;
        cin>>foo>>bar;
        memset(vis, -1,sizeof(vis));
        sum[1]=0;
        for(int i=2;i<=n;i++) sum[i]=sum[i-1]+dis[i-1][i];
        double ans = hic(1,1);
        //double ans  = 0;
        printf("Case #%d: %.10lf\n", cs++, ans);
    }
    return 0;
}
