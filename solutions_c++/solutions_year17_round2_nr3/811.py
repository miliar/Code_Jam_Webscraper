#include <bits/stdc++.h>
using namespace std;
#define ld long double
const int N=105;
ld dp[N];
ld x[N];
ld v[N],d[N];
int q;
int main()
{
	int t;
	cin>>t;
	int ci=1;
	while(t--)
	{
		int n;
		cin>>n>>q;
		for(int i=1;i<=n;i++)
		{
			int a,b;
			cin>>a>>b;
			d[i]=a;
			v[i]=b;
		}
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
			{
				int x1;
				cin>>x1;
				if(x1!=-1)
				{
					x[j]=x1;
				}
			}
		x[1]=0;
		for(int i=2;i<=n;i++)
			x[i]=x[i-1]+x[i];
		int s,e;
		cin>>s>>e;
		//s==1, e==n
		dp[1]=0;
		ld INF=1e18;
		for(int i=2;i<=n;i++)
		{
			dp[i]=INF;
			for(int j=1;j<i;j++)
			{
				ld need=x[i]-x[j];
				ld ti=need/v[j];
				if(need>d[j])
					continue;
				dp[i]=min(dp[i],dp[j]+ti);
			}
		}
		cout<<"Case #"<<ci<<": ";
		ci++;
		cout<<setprecision(25)<<dp[n]<<endl;
	}
	return 0;
}
