/// David Mateus Batista <david.batista3010@gmail.com>
/// Computer Science - Federal University of Itajuba - Brazil

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

#define INF 0x3F3F3F3F
#define LINF 0x3F3F3F3F3F3F3F3FLL
#define DINF (double)1e+30
#define EPS (double)1e-9
#define PI (double)acos(-1.0)
#define RAD(x) (double)(x*PI)/180.0
#define PCT(x,y) (double)x*100.0/y

#define pb push_back
#define mp make_pair
#define pq priority_queue
#define F first
#define S second

#define D(x) x&(-x)
#define SZ(x) (int)x.size()
#define ALL(x) x.begin(),x.end()
#define SET(a,b) memset(a, b, sizeof(a))

#define gcd(x,y) __gcd(x, y)
#define lcm(x,y) (x/gcd(x,y))*y

#define bitcnt(x) __builtin_popcountll(x)
#define lbit(x) 63-__builtin_clzll(x)
#define zerosbitll(x) __builtin_ctzll(x)
#define zerosbit(x) __builtin_ctz(x)

enum {North, East, South, West};
//{0, 1, 2, 3}
//{Up, Right, Down, Left}

int mi[] = {-1, 0, 1, 0, -1, 1, 1, -1};
int mj[] = {0, 1, 0, -1, 1, 1, -1, -1};

typedef int FTYPE; //type of flow
typedef int CTYPE; //type of cost
typedef pair<FTYPE,CTYPE>pfc;
const CTYPE CINF=INF;
const FTYPE FINF=INF;

void operator+=(pfc &p1, pfc &p2)
{
	p1.F+=p2.F;
	p1.S+=p2.S;
}

class graph
{
	const static int MN=1e+4;
public:
	int n=MN;
	FTYPE flow[MN];
	CTYPE dist[MN], pot[MN];
	int prev[MN], eidx[MN];

	struct Edge
	{
		int to;
		FTYPE cap;
		CTYPE cost;
		Edge(){};
		Edge(int _to, FTYPE _cap, CTYPE _cost)
		{
			to=_to;
			cap=_cap;
			cost=_cost;
		}//
	};
	struct node
	{
		int u;
		CTYPE d;
		node(){};
		node(int _u, CTYPE _d)
		{
			u=_u;
			d=_d;
		}
		bool operator <(const node &foo) const
		{
			return d>foo.d;
		}
	};
	graph(){};
	vector<int>adj[MN];
	vector<Edge>edge;
	inline void set(int _n)
	{
		n=_n;
	}
	inline void reset()
	{
		for(int i=0; i<n; i++)
			adj[i].clear();
		edge.clear();
	}
	inline void add_edge(int u, int v, FTYPE c, CTYPE cst)
	{
		adj[u].push_back(edge.size());
		edge.push_back(Edge(v, c, cst));
		adj[v].push_back(edge.size());
		edge.push_back(Edge(u, 0, -cst));
	}

	pfc dijkstra(int s, int t)
	{
		for(register int i=0; i<n; i++)
			dist[i]=CINF;
		dist[s]=0;
		flow[s]=FINF;
		priority_queue<node>heap;
		heap.push(node(s, 0));
		while(!heap.empty())
		{
			int u=heap.top().u;
			CTYPE d=heap.top().d;
			heap.pop();
			if(d>dist[u])
				continue;
			for(int i=0; i<adj[u].size(); i++)
			{
				int idx=adj[u][i];
				int v=edge[idx].to;
				CTYPE w=edge[idx].cost;
				if(!edge[idx].cap)
					continue;
				if(d+w<dist[v])
				{
					dist[v]=d+w;
					prev[v]=u;
					eidx[v]=idx;
					flow[v]=min(flow[u], edge[idx].cap);
					heap.push(node(v, d+w));
				}
			}
		}
		if(dist[t]==CINF)
			return mp(FINF, CINF);
		pfc ret=mp(flow[t], 0);
		for(int u=t; u!=s; u=prev[u])
		{
			int idx=eidx[u];
			edge[idx].cap-=flow[t];
			edge[idx^1].cap+=flow[t];
			ret.second+=flow[t]*edge[idx].cost;
		}
		return ret;
	}

	inline pfc mfmc(int s, int t)
	{
		pfc ret=mp(0, 0);
		pfc got;
		while((got=dijkstra(s, t)).first!=FINF)
			ret+=got;
		return ret;
	}
};

class graph2
{
	const static int N=1e+4;
public:
	vector< pair<int,int> >edge;
	vector<int>adj[N];
	int ptr[N];
	int dist[N];

	graph2(){};
	void clear()
	{
		for(int i=0; i<N; i++)
			adj[i].clear();
		edge.clear();
	}
	void add_edge(int u, int v, int c)
	{
		adj[u].push_back(edge.size());
		edge.push_back(mp(v, c));
		adj[v].push_back(edge.size());
		edge.push_back(mp(u, 0)); //(u, c) if is non-directed
	}
	bool dinic_bfs(int s, int t)
	{
		memset(dist, -1, sizeof(dist));
		dist[s]=0;

		queue<int>bfs;
		bfs.push(s);
		while(!bfs.empty() && dist[t]==-1)
		{
			int u=bfs.front();
			bfs.pop();
			for(int i=0; i<adj[u].size(); i++)
			{
				int idx=adj[u][i];
				int v=edge[idx].F;

				if(dist[v]==-1 && edge[idx].S>0)
				{
					dist[v]=dist[u]+1;
					bfs.push(v);
				}
			}
		}
		return dist[t]!=-1;
	}
	int dinic_dfs(int u, int t, int flow)
	{
		if(u==t)
			return flow;
		for(int &i=ptr[u]; i<adj[u].size(); i++)
		{
			int idx=adj[u][i];
			int v=edge[idx].F;
			if(dist[v]==dist[u]+1 && edge[idx].S>0)
			{
				int cf=dinic_dfs(v, t, min(flow, edge[idx].S));
				if(cf>0)
				{
					edge[idx].S-=cf;
					edge[idx^1].S+=cf;
					return cf;
				}
			}
		}
		return 0;
	}
	int maxflow(int s, int t)
	{
		int ret=0;
		while(dinic_bfs(s, t))
		{
			memset(ptr, 0, sizeof(ptr));
			int cf=dinic_dfs(s, t, INF);
			if(cf==0)
				break;
			ret+=cf;
		}
		return ret;
	}
};

const int MN=1e+3+35;
int n, m, c;
int lim;

//F buyer, S position
pii data[MN];
int aux[MN];
graph g;
graph2 g2;
pfc ans;

int haha(int x)
{
	g2.clear();
	for(int i=1; i<=c; i++)
		g2.add_edge(0, i, aux[i]);
	//objective -> sink
	for(int i=1; i<=n; i++)
		g2.add_edge(i+c, n+c+1, x);
	//range
	for(int i=1; i<n; i++)
	{
		g2.add_edge((n+c+1)+i, i+c+1, m);
		g2.add_edge((n+c+1)+i, (n+c+1)+(i+1), m);
	}

	for(int i=0; i<m; i++)
	{
		g2.add_edge(data[i].F, data[i].S+c, 1);
		if(data[i].S<n)
			g2.add_edge(data[i].F, (n+c+1)+data[i].S, 1);
	}
	return g2.maxflow(0, n+c+1)==m;
}

int f(int x)
{
	g.set(2*(n+c)+1);
	g.reset();

	//source=0, sink=(n+c+1)

	//source -> position
	for(int i=1; i<=c; i++)
		g.add_edge(0, i, aux[i], 0);
	//objective -> sink
	for(int i=1; i<=n; i++)
		g.add_edge(i+c, n+c+1, x, 0);
	//range
	for(int i=1; i<n; i++)
	{
		g.add_edge((n+c+1)+i, i+c+1, m, 0);
		g.add_edge((n+c+1)+i, (n+c+1)+(i+1), m, 0);
	}

	for(int i=0; i<m; i++)
	{
		g.add_edge(data[i].F, data[i].S+c, 1, 0);
		if(data[i].S<n)
			g.add_edge(data[i].F, (n+c+1)+data[i].S, 1, 1);
	}

	ans=g.mfmc(0, n+c+1);
	return ans.F==m;
}

template<class num>inline void rd(num &x)
{
	char c;
	while(isspace(c = getchar()));
	bool neg = false;
	if(!isdigit(c))
		neg=(c=='-'), x=0;
	else
		x=c-'0';
	while(isdigit(c=getchar()))
		x=(x<<3)+(x<<1)+c-'0';
	if(neg)
		x=-x;
}

int main()
{
	#ifdef LOCAL_PROJECT
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	#else
	#endif

	int tt;
	rd(tt);
	for(int t=1; t<=tt; t++)
	{
		SET(aux, 0);
		rd(n), rd(c), rd(m);

		int L=0;
		for(int i=0; i<m; i++)
		{
			int x, y;
			rd(x), rd(y);
			x=n-x+1;
			data[i]={y, x};
			aux[y]++;
			L=max(L, aux[y]);
		}
		int lo=L, hi=m;
		while(abs(lo-hi)>1)
		{
			int mid=(lo+hi)/2;
			if(haha(mid))
				hi=mid;
			else
				lo=mid;
		}
		while(lo>L && haha(lo-1))
			lo--;
		while(lo<m && !haha(lo))
			lo++;
		f(lo);
		printf("Case #%d: %d %d\n", t, lo, ans.S);
	}
	return 0;
}