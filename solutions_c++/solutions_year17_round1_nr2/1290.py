#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <deque>
using namespace std;
const int MAX_N = 60;
const int MAX_M=1005000;
const int INF=1500000000;
long long x[MAX_N];
long long y[MAX_N][MAX_N];
long long kmin[MAX_N][MAX_N];
long long kmax[MAX_N][MAX_N];
vector <int> g[MAX_N];
int nnew[MAX_N];
int p[MAX_N];
int flag[MAX_N];
int dfs(int v,int ff)
{
	if (flag[v]==ff)
		return 0;
	flag[v]=ff;
	for (int i=0;i<g[v].size();i++)
	{
		int t=g[v][i];
		if (p[t]==-1||dfs(p[t],ff)==1)
		{
			p[t]=v;
			nnew[v]=1;
			return 1;
		}
	}
	return 0;
}
int parsoch(int n,int m)
{
	for (int i=0;i<MAX_N;i++)
	{
		flag[i]=0;
		nnew[i]=0;
		p[i]=-1;
	}
	int ans=0,ff=1,k=1;
	do
	{
		k=0;
		ff++;
		for (int i=0;i<m;i++)
		{
			if (nnew[i]==0&&dfs(i,ff)==1)
			{
				ans++;
				k=1;
			}
		}
	}while(k==1);
	return ans;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int Q,n,m;
	long long t,ans=0;
	cin>>Q;
	for (int q1=1;q1<=Q;q1++)
	{
		ans=0;
		for (int i=0;i<MAX_N;i++)
		{
			g[i].clear();
			x[i]=0;
			for (int j=0;j<MAX_N;j++)
			{
				kmax[i][j]=0;
				kmin[i][j]=INF;
				y[i][j]=0;
			}
		}
		cin>>n>>m;
		for (int i=0;i<n;i++)
			cin>>x[i];
		for (int i=0;i<n;i++)
		{
			for (int j=0;j<m;j++)
			{
				cin>>y[i][j];
				for (long long p=max(0ll,10*y[i][j]/(11*x[i])-5);p<=10*y[i][j]/(9*x[i])+5;p++)
				{
					if (9ll*p*x[i]<=10ll*y[i][j]&&y[i][j]*10ll<=11ll*p*x[i])
					{
						kmin[i][j]=min(p,kmin[i][j]);
						kmax[i][j]=max(p,kmax[i][j]);
					}
				}
			}
		}
		if (n==1)
		{
			for (int j=0;j<m;j++)
			{
				if (kmax[0][j]>0)
					ans++;
			}
		}
		else
		{
			for (int i=0;i<m;i++)
			{
				for (int j=0;j<m;j++)
				{
					if (kmax[0][i]>=kmin[1][j]&&kmax[0][i]<=kmax[1][j]||
						kmin[0][i]>=kmin[1][j]&&kmin[0][i]<=kmax[1][j]||
						kmax[1][j]>=kmin[0][i]&&kmax[1][j]<=kmax[0][i]||
						kmin[1][j]>=kmin[0][i]&&kmin[1][j]<=kmax[0][i])
					{
						g[i].push_back(j);
					}
				}
			}
			ans=parsoch(n,m);
		}
		cout<<"Case #"<<q1<<": "<<ans<<endl;
	}
	return 0;
}