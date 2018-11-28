#include <bits/stdc++.h>
#define INF 1'000'000'000'000
using namespace std;
//typedef tuple<double,int,int> piii;
int e[110];
double s[110];
long long mp[110][110];
double np[110][110];
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout<<fixed<<setprecision(12);

	int T, no=1;
	cin>>T;
	while(T--)
	{
		int n,q;
		cin>>n>>q;
		for(int i=0;i<n;i++)
			cin>>e[i]>>s[i];
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
			{
				cin>>mp[i][j];
				if(mp[i][j]==-1)
					mp[i][j]=INF;
			}
		for(int k=0;k<n;k++)
			for(int i=0;i<n;i++)
				for(int j=0;j<n;j++)
					mp[i][j]=min(mp[i][j], mp[i][k]+mp[k][j]);
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
			{
				if(mp[i][j]>e[i])
					np[i][j]=INF;
				else
					np[i][j]=(double)mp[i][j]/s[i];
			}
		for(int k=0;k<n;k++)
			for(int i=0;i<n;i++)
				for(int j=0;j<n;j++)
					np[i][j]=min(np[i][j], np[i][k]+np[k][j]);
		cout<<"Case #"<<no++<<":";
		while(q--)
		{
			int u,v;
			cin>>u>>v;
			u--; v--;
			cout<<" "<<np[u][v];
			//priority_queue<piii, vector<piii>, greater<piii>> pq;
			//pq.push(make_tuple(0,u,u));
			//static double dis[110][110];
			//for(int i=0;i<n;i++)
			//	for(int j=0;j<n;j++)
			//		dis[i][j]=10'000'000'000'000.;
			//dis[u][u]=0;
			//while(pq.size())
			//{
			//	piii now=pq.top(); pq.pop();
			//	int d, i, from;
			//	tie(d,i,from) = now;
			//	if(d>dis[i][from]) continue;
			//	for(int j=0;j<n;j++)
			//	{

			//	}
			//}
		}
		cout<<endl;
	}
}