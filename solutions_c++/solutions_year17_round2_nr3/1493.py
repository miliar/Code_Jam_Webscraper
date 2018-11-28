#include<bits/stdc++.h>
using namespace std;
#define int long long
#define s second
#define f first
ofstream out("output.txt");
void solve(int now)
{
	int n,q;
	cin>>n>>q;
	vector<pair<signed,long double> > a(n);
	for (int i=0;i<n;i++)
	{
		cin>>a[i].f>>a[i].s;
	}
	int g[n][n];
	int f[n][n];
	long double dp[n][n];
	for (int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			dp[i][j]=1e18;
			cin>>g[i][j];
			f[i][j]=0;
		}
	}
	for (int i=0;i<n;i++)
	{
		for (int j=i+1;j<n;j++)
		{
			f[i][j]=f[i][j-1]+g[j-1][j];
		}
	}
	dp[0][0]=0;
	for (int i=1;i<n;i++)
	{
		for(int j=0;j<i;j++)
		{
		 	if (f[j][i]<=a[j].f)
			{
				dp[i][j]=min(dp[j][j]+(long double)f[j][i]/a[j].s,dp[i][j]);
				dp[i][i]=min(dp[i][j],dp[i][i]);
			}
		}
	}
	out<<"CASE #"<<now<<": ";
	for (int i=0;i<q;i++)
	{
		int a,b;
		cin>>a>>b;
		a--;
		b--;
		out<<setprecision(20)<<dp[b][b];
	}
	out<<"\n";
}
signed main()
{
	int t,now=1;
	cin>>t;
	while (t--)
	{
		solve(now);
		now++;
	}
	return 0;
}
