#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define ll long long
#define INF 1e18
#define pb push_back
#define PI 3.141592653
vector <pair<ll,ll> > v;
ll dp[1010][1010];
ll m;
ll n;
ll find(ll curr,ll k)
{
	if(curr==n)
	{
		if(k!=0)
		{
			return -INF;
		}
		else
		{
			return 0;
		}
	}
	if(k==0)
		return 0;
	if(dp[curr][k]!=-1)
		return dp[curr][k];
	dp[curr][k]=0;
	if(m==k)
	{
		dp[curr][k]=max(v[curr].first*v[curr].first+2*v[curr].first*v[curr].second+find(curr+1,k-1),find(curr+1,k));
	}
	else
	{
		dp[curr][k]=max(2*v[curr].first*v[curr].second+find(curr+1,k-1),find(curr+1,k));
	}
	// cout<<curr<<" "<<k<<dp[curr][k]<<endl;
	return dp[curr][k];
}
int main()
{
	ll t,r,h;
	cin>>t;
	ll z=0;
	ll k;
	long double p=3.141592653;
	while(t--)
	{
		z++;
		cout<<"Case #"<<z<<": ";
		cin>>n>>k;
		m=k;
		for(int i=0;i<n;i++)
		{
			cin>>r>>h;
			v.push_back({r,h});
		}
		for(int i=0;i<=n;i++)
		{
			for(int j=0;j<=n;j++)
				dp[i][j]=-1;
		}
		sort(v.begin(),v.end());
		reverse(v.begin(),v.end());
		long double ans=find(0,k)*1.0;
		ans=ans*p;
		cout<<fixed<<setprecision(8)<<ans<<endl;
		v.clear();
	}
}