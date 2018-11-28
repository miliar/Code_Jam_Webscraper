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
typedef pair<ll,ll> ii;
typedef vector<int> vi;
typedef long double ld; 
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> pbds;
typedef set<int>::iterator sit;
typedef map<int,int>::iterator mit;
typedef vector<int>::iterator vit;

ll dist[101][101];

struct Graph
{
	struct edge
	{
		int v; ld weight;
	};
	vector<vector<edge> > adj;
	int n;
	
	Graph(int _n)
	{
		adj.resize(_n);
		n = _n;
	}
	
	void addedge(int u, int v, ld c)
	{
		edge tmp;
		tmp.v = v; tmp.weight = c;
		adj[u].pb(tmp);
	}
	
	void reset()
	{
		adj.clear();
	}
	
	vector<ld> dist;
	vi par;
	
	void dijkstra(int s)
	{
		ld INFI = ld(1e18);
		dist.assign(n, INFI);
		par.assign(n, -1);
		dist[s] = 0; par[s] = -1;
		priority_queue<pair<ld,int> , vector<pair<ld,int> >, greater<pair<ld,int> > > pq;
		pq.push(ii(0, s));
		while(!pq.empty())
		{
			int u = pq.top().se; ld d = pq.top().fi; pq.pop();
			for(int i = 0; i < adj[u].size(); i++)
			{
				int v = adj[u][i].v; ld w = adj[u][i].weight;
				if(d + w < dist[v])
				{
					dist[v] = d + w;
					par[v] = u;
					pq.push(mp(dist[v], v));
				}
			}
		}
	}
	
	vector<vector<ld> > d;
	
	void Floyd()
	{
		ld INFIN = ld(1e18);
		d.resize(n);
		for(int i = 0; i < n; i++)
		{
			d[i].assign(n, INFIN);
		}
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < adj[i].size(); j++)
			{
				d[i][adj[i][j].v] = adj[i][j].weight;
			}
			d[i][i] = 0;
		}
		for(int k = 0; k < n; k++)
		{
			for(int i = 0; i < n; i++)
			{
				for(int j = 0; j < n; j++)
				{
					d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
				}
			}
		}
	}
};
ll spd[1001];
const ld eps=1e-7;
ll maxd[1001];

int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int t; cin>>t;
	for(int zz = 1; zz <= t; zz++)
	{
		cout<<"Case #"<<zz<<": ";
		int n,q ;cin>>n>>q;
		for(int i=0;i<n;i++)
		{
			cin>>maxd[i]>>spd[i];
		}
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				cin>>dist[i][j];
			}
		}
		Graph G(n);
		for(int i=0;i<n;i++)
		{
			Graph g(n);
			for(int j=0;j<n;j++)
			{
				for(int k=0;k<n;k++)
				{
					if(dist[j][k]!=-1)
					{
						g.addedge(j,k,dist[j][k]);
					}
				}
			}
			g.dijkstra(i);
			for(int j=0;j<n;j++)
			{
				if(g.dist[j]<=maxd[i]+eps)
				{
					if(i!=j)
					{
						G.addedge(i,j,ld(g.dist[j])/ld(spd[i]));
					}
				}
			}
		}
		G.Floyd();
		for(int i=0;i<q;i++)
		{
			int u, v; cin>>u>>v;
			u--; v--;
			cout<<fixed<<setprecision(11)<<G.d[u][v]<<' ';
		}	
		cout<<'\n';
		cerr<<"Case #"<<zz<<" solved.\n";
	}
}


