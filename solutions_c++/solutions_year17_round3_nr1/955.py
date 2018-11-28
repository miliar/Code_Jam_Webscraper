/*input
4
2 1
100 20
200 10
2 2
100 20
200 10
3 2
100 10
100 10
100 10
4 2
9 3
7 1
10 1
8 4
*/

#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define PII pair<ll, ll>
#define f first
#define s second
#define F(i,a,b) for(ll i = (ll)(a); i <= (ll)(b); i++)
#define RF(i,a,b) for(ll i = (ll)(a); i >= (ll)(b); i--)
#define MAXN 1005
#define INF LLONG_MAX
#define mod 1000000007
using namespace std;


ll t;
ll n, k;
PII arr[MAXN];
ll r, h, dp[1005][1005];

ll func(ll ind, ll rem, bool flag)
{
	if(ind == 0)
	{
		if(rem == 0)
		{
			return 0;
		}
		else
			return LLONG_MIN;
	}
	ll ret = 0;
	if(dp[ind][rem]!=-1)
		return dp[ind][rem];
	if(rem>0)
	{
		ll tmp = 2 * arr[ind].f * arr[ind].s;
		if(!flag)
			tmp = tmp + arr[ind].f * arr[ind].f;
		ret = max(ret, tmp + func(ind-1, rem-1, 1)); 
	}
	ret = max(ret, func(ind-1, rem, flag));
	dp[ind][rem] = ret;
	return ret;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin>>t;
	F(cas,1,t)
	{
		memset(dp,-1,sizeof(dp));
		cin>>n>>k;
		F(i,1,n)
		{
			cin>>r>>h;
			arr[i].f = r;
			arr[i].s = h;
		}
		sort(arr+1,arr+1+n);
		double ans = M_PI * func(n,k,0);
		cout<<"Case #"<<cas<<": ";
		printf("%.11f\n",ans);
	}    
	return 0;
}