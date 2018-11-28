#include<bits/stdc++.h>
#define mod 1000000007
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define PI 3.14159265358979323846
using namespace std; 
bool cmp(pair<long long int,long long int> a,pair<long long int,long long int> b)
{
	return a.ff*a.ss>b.ff*b.ss;
}
long long int dp[1001][1001];
vector<pair<long long int,long long int> > v;
	int n,k;
long long int solve(int i,int j)
{
	if(i>=k||j>=n)
	{
		return 0;
	}
	if(~dp[i][j])
		return dp[i][j];
	long long int ans=0;
	if(i==0)
		ans = max(solve(i,j+1),v[j].ff*v[j].ff + 2*v[j].ff*v[j].ss + solve(i+1,j+1));
	else
		ans = max(solve(i,j+1),2*v[j].ff*v[j].ss + solve(i+1,j+1));
	return dp[i][j] = ans;

}
int main()
{
	int t,cs=0;
	scanf("%d",&t);
	while(t--)
	{	
		cs++;
		scanf("%d %d",&n,&k);
		memset(dp,-1,sizeof(dp));
		v.clear();
		v.resize(n);
		for( int i=0;i<n;i++)
		{
			scanf("%lld %lld",&v[i].ff,&v[i].ss);
		}
		sort(v.rbegin(),v.rend());
		// long long int base = v[0].ff*v[0].ff + 2*v[0].ff*v[0].ss;
		// sort(v.begin()+1,v.end(),cmp);
		// for( int i=1;i<k;i++)
		// {
		// 	base+=2*v[i].ff*v[i].ss;
		// }

		// double ans = (double)PI*base;

		// vector<vector<double> > dp(k+1,vector<double>(n+1,0));

		// for(int i=1;i<=n;i++)
		// {
		// 	dp[1][i] = v[i-1].ff*v[i-1].ff + 2*v[i-1].ff*v[i-1].ss;
		// }
		// for(int i=2;i<=k;i++)
		// {
		// 	for(int j = 2;j<=n;j++)
		// 	{
		// 		for(int bb=1;bb<j;bb++)
		// 		{
		// 		dp[i][j] = max(dp[i-1][j],dp[i][bb] + 2*v[j-1].ff*v[j-1].ss);
		// 	    }
		// 	}
		// }
		double ans = PI*solve(0,0);
		printf("Case #%d: %.9lf\n",cs,ans);
				
	}

	return 0;
}