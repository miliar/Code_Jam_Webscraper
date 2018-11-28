#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define ld long double
#define N ((ll)110)
#define INF ((ll)2e18)

ifstream fin("input.in");
ofstream fout("output.txt");

ll t,n,q,max_d[N],s[N],d[N][N];
ld dis[N][N];

int main()
{
	ios_base::sync_with_stdio(0);
	fin>>t;
	for(int qq=1;qq<=t;qq++)
	{
		fin>>n>>q;
		for(int i=1;i<=n;i++)fin>>max_d[i]>>s[i];
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
			{
				fin>>d[i][j];
				if(i==j)d[i][j]=0;
				if(d[i][j]==-1)d[i][j]=INF;
			}
		for(int k=1;k<=n;k++)
			for(int i=1;i<=n;i++)
				for(int j=1;j<=n;j++)
					d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
			{
				dis[i][j]=INF;
				if(d[i][j]<=max_d[i])dis[i][j]=(ld)d[i][j]/s[i];
			}
		for(int k=1;k<=n;k++)
			for(int i=1;i<=n;i++)
				for(int j=1;j<=n;j++)
					dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j]);
		fout<<"Case #"<<qq<<": ";
		for(int i=1;i<=q;i++)
		{
			ll v,u;
			fin>>v>>u;
			fout<<fixed<<setprecision(14)<<dis[v][u]<<" ";
		}
		fout<<"\n";
	}
	
	return 0;
}
