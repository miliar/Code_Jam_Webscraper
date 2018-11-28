#include<bits/stdc++.h>
using namespace std;
#define sd(x) scanf("%lld",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define ll long long
#define mod 1000000007
#define bitcount    __builtin_popcountll
#define pb push_back
#define fi first
#define se second
#define mp make_pair
#define pi pair<ll,ll>
ll dp[1003][1003];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    ll t,n,k,i,j,x;
    pi a[1003];
    double s;
    sd(t);
    for(x=1;x<=t;x++)
    {
    	sd(n);
    	sd(k);
    	for(i=1;i<=n;i++)
    	{
    		sd(a[i].fi);
    		sd(a[i].se);
    	}
    	memset(dp, 0, sizeof dp);
    	sort(a+1,a+n+1);
    	reverse(a+1,a+n+1);
    	for(i=1;i<=n;i++)
    	{
    		for(j=1;j<k;j++)
    			dp[i][j]=max(dp[i-1][j],dp[i-1][j-1]+2*a[i].fi*a[i].se);
    	}
    	j=0;
    	for(i=1;i<=n-k+1;i++)
    	{
    		j=max(j,dp[i+1][k-1]+2*a[i].fi*a[i].se+a[i].fi*a[i].fi);
    	}
    	s=j;
    	s*=3.14159265358979323846264338327950288419716939937510;
    	printf("Case #%lld: %.8lf\n",x,s);
    }
    return 0;
}