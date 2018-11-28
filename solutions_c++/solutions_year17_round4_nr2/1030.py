#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define fbo find_by_order
#define ook order_of_key

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef long double ld; 
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> pbds;
typedef set<int>::iterator sit;
typedef map<int,int>::iterator mit;
typedef vector<int>::iterator vit;
const int MX = 2001;
const int INF = 10000000;
struct MaxFlow //by yutaka1999, have to define INF and MX (the Max number of vertices)
{
	struct edge
	{
		int to,cap,rev;
		edge(int to=0,int cap=0,int rev=0):to(to),cap(cap),rev(rev){}
	};
	vector <edge> vec[MX];
	int level[MX];
	int iter[MX];
	
	void addedge(int s,int t,int c) //adds an edge of cap c to the flow graph
	{
		int S=vec[s].size(),T=vec[t].size();
		vec[s].push_back(edge(t,c,T));
		vec[t].push_back(edge(s,0,S));
	}
	void bfs(int s)
	{
		memset(level,-1,sizeof(level));
		queue <int> que;
		level[s] = 0;
		que.push(s);
		while (!que.empty())
		{
			int v = que.front();que.pop();
			for(int i=0;i<vec[v].size();i++)
			{
				edge&e=vec[v][i];
				if (e.cap>0&&level[e.to]<0)
				{
					level[e.to]=level[v]+1;
					que.push(e.to);
				}
			}
		}
	}
	ll flow_dfs(int v,int t,ll f)
	{
		if (v==t) return f;
		for(int &i=iter[v];i<vec[v].size();i++)
		{
			edge &e=vec[v][i];
			if (e.cap>0&&level[v]<level[e.to])
			{
				ll d=flow_dfs(e.to,t,min(f,ll(e.cap)));
				if (d>0)
				{
					e.cap-=d;
					vec[e.to][e.rev].cap+=d;
					return d;
				}
			}
		}
		return 0;
	}
	ll maxflow(int s,int t) //finds max flow using dinic from s to t
	{
		ll flow = 0;
		while(1)
		{
			bfs(s);
			if (level[t]<0) return flow;
			memset(iter,0,sizeof(iter));
			while (1)
			{
				ll f=flow_dfs(s,t,INF);
				if(f==0) break;
				flow += f;
			}
		}
	}
};
int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0);
	freopen("B-small2.in", "r", stdin);
	freopen("B-small2.out", "w", stdout);
	int t; cin>>t;
	for(int zz = 1; zz <= t; zz++)
	{
		cout<<"Case #"<<zz<<": ";
		int n,m,c; cin>>n>>c>>m;
		multiset<ii> tickets;
		multiset<ii> bac;
		for(int i=0;i<m;i++)
		{
			int pos,idx;
			cin>>pos>>idx;
			pos--; idx--;
			tickets.insert(mp(pos,idx));
		}
		//cout<<tmp+max(cnt[1][0],cnt[1][1])<<' '<<min(cnt[1][0],cnt[1][1])<<'\n';
		//cout<<tmp<<' '<<cnt[0][0]<<' '<<cnt[0][1]<<' '<<cnt[1][0]<<' '<<cnt[1][1]<<'\n';
		bac=tickets;
		int ans1=0;
		for(int i = 1; i <= m; i++)
		{
			bool used[1001];
			memset(used,0,sizeof(used));
			vector<ii> backup;
			for(int j = 0; j < n; j++)
			{
				if(tickets.empty()) break;
				while(!tickets.empty())
				{
					ii tmp = (*tickets.begin());
					if(used[tmp.se])
					{
						backup.pb(tmp);
						tickets.erase(tickets.begin());
						continue;
					}
					else
					{
						if(j<=tmp.fi)
						{
							used[tmp.se]=1;
							tickets.erase(tickets.begin());
							break;
						}
						else
						{
							backup.pb(tmp);
							tickets.erase(tickets.begin());
							continue;
						}
					}
				}
			}
			while(!backup.empty())
			{
				tickets.insert(backup.back());
				backup.pop_back();
			}
			if(tickets.empty())
			{
				//cout<<i<<' ';
				ans1=i;
				break;
			}
			if(i==m&&!tickets.empty()) assert(0);
		}
		tickets=bac;
		//cerr<<tickets.size()<<'\n';
		bool used[1001][1001];
		memset(used,0,sizeof(used));
		/*
		for(int i = 1; i <= ans1; i++)
		{
			bool used[1001];
			memset(used,0,sizeof(used));
			vector<ii> backup;
			for(int j = 0; j < n; j++)
			{
				if(tickets.empty()) break;
				while(!tickets.empty())
				{
					ii tmp = (*tickets.begin());
					//cerr<<j<<' '<<tmp.fi<<'\n';
					if(used[tmp.se])
					{
						backup.pb(tmp);
						tickets.erase(tickets.begin());
						continue;
					}
					else
					{
						if(j==tmp.fi)
						{
							//cerr<<"HERE"<<endl;
							used[tmp.se]=1;
							tickets.erase(tickets.begin());
							break;
						}
						else if(tmp.fi>j)
						{
							break;
						}
						else if(j>tmp.fi)
						{
							backup.pb(tmp);
							tickets.erase(tickets.begin());
							continue;
						}
					}
				}
			}
			while(!backup.empty())
			{
				tickets.insert(backup.back());
				backup.pop_back();
			}
		}
		*/
		vi vec[1001];
		for(multiset<ii>::iterator it = tickets.begin(); it != tickets.end(); it++)
		{
			vec[(*it).se].pb((*it).fi);
		}
		MaxFlow mf;
		int s=vec[0].size()+vec[1].size()+1;
		int e=s+1;
		for(int i = 0; i < vec[0].size(); i++)
		{
			mf.addedge(s,i,1);
			for(int j = 0; j < vec[1].size(); j++)
			{
				if(vec[0][i]!=vec[1][j]) mf.addedge(i,j+vec[0].size(),1);
			}
		}
		for(int j=0;j<vec[1].size();j++)
		{
			mf.addedge(j+vec[0].size(),e,1);
		}
		int res = mf.maxflow(s,e);
		int tic = m;
		tic-=res*2;
		tic-=(ans1-res);
		cout<<ans1<<' '<<max(tic,0)<<'\n';
		//assert(ans1==tmp+max(cnt[1][0],cnt[1][1]));
		//assert(tickets.size()==min(cnt[1][0],cnt[1][1]));
		cerr<<"Case #"<<zz<<" solved.\n";
	}
}


