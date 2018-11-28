#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
#include<string>
#include<string.h>
#include<set>
#include<iomanip>
#define N 500
using namespace std;
pair<double,double>horse[N];
double edges[N][N];
pair<double,double>dist[N][N];
int main()
{
	int t;
	cout<<fixed;
	cin>>t;
	for(int o=1;o<=t;o++)
	{
		int n,q;
		double bub=1e15;
		cin>>n>>q;
		for(int i=1;i<=n;i++)
		{
			int x,y;
			cin>>horse[i].first>>horse[i].second;
		}
		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=n;j++)
			{
				cin>>edges[i][j];
			}
		}
		cout<<"Case #"<<o<<": ";
		for(int ola=0;ola<q;ola++)
		{
			int x,y;
			cin>>x>>y;
			set<pair< pair<double,double>,pair<int,int> > >s;
			for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
				{
					dist[i][j]=make_pair(bub,bub);
				}
			s.insert(make_pair(make_pair(0,bub-horse[x].first),make_pair(x,x)));
			dist[x][x]=make_pair(0,horse[x].first);
			//cout<<"hr:"<<bub-horse[x].first<<" "<<horse[x].first<<endl;
			while(s.size())
			{
				double lefd,tim;
				int u,hr;
				tim=s.begin()->first.first;
				lefd=bub-s.begin()->first.second;
				u=s.begin()->second.first;
				hr=s.begin()->second.second;
				s.erase(s.begin());
				//cout<<"time:"<<tim<<" city:"<<u<<" horse:"<<hr<<" leftwalk:"<<lefd<<" data:"<<dist[u][hr].first<<" "<<dist[u][hr].second<<endl;
				if(dist[u][hr]==make_pair(tim,lefd))
				{
					for(int i=1;i<=n;i++)
					{
						if(edges[u][i]!=-1)
						{
							if(lefd-edges[u][i]>=0&&dist[i][hr]>=make_pair(tim+edges[u][i]/horse[hr].second,bub-(lefd-edges[u][i])))
							{
								dist[i][hr]=make_pair(tim+edges[u][i]/horse[hr].second,(lefd-edges[u][i]));
								s.insert(make_pair(make_pair(tim+edges[u][i]/horse[hr].second,bub-(lefd-edges[u][i])),make_pair(i,hr)));
							}
						}
					}
					for(int i=1;i<=n;i++)
					{
						if(edges[u][i]!=-1)
						{
							if(horse[u].first-edges[u][i]>=0&&dist[i][u]>=make_pair(tim+edges[u][i]/horse[u].second,bub-(horse[u].first-edges[u][i])))
							{
								dist[i][u]=make_pair(tim+edges[u][i]/horse[u].second,(horse[u].first-edges[u][i]));
								s.insert(make_pair(make_pair(tim+edges[u][i]/horse[u].second,bub-(horse[u].first-edges[u][i])),make_pair(i,u)));
							}
						}
					}
				}
			}
			double sol=bub;
			for(int i=1;i<=n;i++)
				sol=min(sol,dist[y][i].first);
			cout<<setprecision(9)<<sol<<" ";
		}
		cout<<"\n";
	}
}