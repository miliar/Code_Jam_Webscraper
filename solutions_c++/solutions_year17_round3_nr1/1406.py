#include<bits/stdc++.h>
using namespace std;

#define MAX 1010

typedef long long ll;
const ll inf = 1ll<<61;
const double pi=acos(-1.0);

ll dp[MAX][MAX][2];
ll k,n;
vector< pair<ll,ll> > v;

ll cal(ll ni, ll ki, bool isFirst)
{
    if(ki==k)
        return 0;
    if(ni==n)
        return -inf;
    if(dp[ni][ki][isFirst] != -1)
        return dp[ni][ki][isFirst];
    ll ret1,ret2;
    ret1=ret2=0;
    ret1=v[ni].first*v[ni].second*2+cal(ni+1,ki+1,0);
    if(isFirst)
        ret1+=v[ni].first*v[ni].first;
    ret2=cal(ni+1,ki,isFirst);
    return dp[ni][ki][isFirst]=max(ret1,ret2);
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    ll t,ti,i,j,a,b;
    double ans;
    scanf("%lld",&t);
    for(ti=1; ti<=t; ++ti)
    {
        v.clear();
        scanf("%lld %lld",&n,&k);
        for(i=0; i<n; ++i)
        {
            scanf("%lld %lld",&a,&b);
            v.push_back({a,b});
        }
        sort(v.begin(),v.end());
        reverse(v.begin(),v.end());
        memset(dp,-1,sizeof(dp));
        ans=pi*cal(0,0,1);
        printf("Case #%lld: %.8lf\n",ti,ans);
    }
    return 0;
}
