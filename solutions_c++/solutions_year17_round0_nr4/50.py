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

template<int MX, ll INF> struct MaxFlow //by yutaka1999, have to define INF and MX (the Max number of vertices)
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

char ans[101][101];
char x[4] = {'.', '+', 'x', 'o'};
int res[101][101];
char a[101][101];
int n;

bool isvalid(int x, int y)
{
	return (x>=0&&x<n&&y>=0&&y<n);
}

int check()
{
	int sc = 0;
	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j < n; j++)
		{
			if(ans[i][j]=='+') sc++;
			else if(ans[i][j]=='x') sc++;
			else if(ans[i][j]=='o') sc+=2;
		}
	}
	for(int i = 0; i < n; i++)
	{
		int cnt = 0;
		for(int j = 0; j < n; j++)
		{
			if(a[i][j]=='x'||a[i][j]=='o') cnt++;
		}
		if(cnt>1) return -1;
		cnt=0;
		for(int j = 0; j < n; j++)
		{
			if(a[j][i]=='x'||a[j][i]=='o') cnt++;
		}
		if(cnt>1) return -1;
	}
	for(int i = 0; i <= 2*n; i++)
	{
		int cnt = 0;
		for(int j = 0; j < n; j++)
		{
			int x = j; int y = i - j;
			if(isvalid(x, y))
			{
				if(a[x][y]=='+'||a[x][y]=='o') cnt++;
			}
		}
		if(cnt>1) return -1;
	}
	for(int i = -n; i <= n; i++)
	{
		int cnt = 0;
		for(int j = 0; j < n; j++)
		{
			int x = j; int y = i + j;
			if(isvalid(x, y))
			{
				if(a[x][y]=='+'||a[x][y]=='o') cnt++;
			}
		}
		if(cnt>1) return -1;
	}
	return sc;
}

void out()
{
	vector<pair<char,ii> > vec;
	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j < n; j++)
		{
			if(a[i][j]!=ans[i][j])
			{
				vec.pb(mp(ans[i][j],mp(i,j)));
			}
		}
	}
	int tmp = check();
	assert(tmp>=0);
	cout<<tmp<<' '<<vec.size()<<'\n';
	for(int i = 0; i < vec.size(); i++)
	{
		cout<<vec[i].fi<<' '<<vec[i].se.fi+1<<' '<<vec[i].se.se+1<<'\n';
	}
}

const int MAXN1 = 1001;
const int MAXN2 = 1001;
const int MAXM = 50001;

int n1, n2, edges, last[MAXN1], pre[MAXM], head[MAXM];
int matching[MAXN2], dist[MAXN1], Q[MAXN1];
bool used[MAXN1], vis[MAXN1];

void init(int _n1, int _n2) {
    n1 = _n1;
    n2 = _n2;
    edges = 0;
    for(int i = 0; i < n1; i++)
    {
		last[i] = -1;
	}
}

void addedge(int u, int v) {
    head[edges] = v;
    pre[edges] = last[u];
    last[u] = edges++;
}

void bfs() {
	for(int i = 0; i < n1; i++)
	{
		dist[i]=-1;
	}
    int sizeQ = 0;
    for (int u = 0; u < n1; ++u) {
        if (!used[u]) {
            Q[sizeQ++] = u;
            dist[u] = 0;
        }
    }
    for (int i = 0; i < sizeQ; i++) {
        int u1 = Q[i];
        for (int e = last[u1]; e >= 0; e = pre[e]) {
            int u2 = matching[head[e]];
            if (u2 >= 0 && dist[u2] < 0) {
                dist[u2] = dist[u1] + 1;
                Q[sizeQ++] = u2;
            }
        }
    }
}

bool dfs(int u1) {
    vis[u1] = true;
    for (int e = last[u1]; e >= 0; e = pre[e]) {
        int v = head[e];
        int u2 = matching[v];
         if (u2 < 0 || ((!vis[u2] && dist[u2] == dist[u1] + 1) && dfs(u2))) {
            matching[v] = u1;
            used[u1] = true;
            return true;
        }
    }
    return false;
}

int maxMatching() {
	for(int i=0;i<n1;i++) used[i]=0;
	for(int i=0;i<n2;i++) matching[i]=-1;
    for (int res = 0;;) {
        bfs();
        fill(vis, vis + n1, false);
        int f = 0;
        for (int u = 0; u < n1; ++u)
            if (!used[u] && dfs(u))
                ++f;
        if (!f)
            return res;
        res += f;
    }
}

bool usedrow[1001];
bool usedcol[1001];
bool usedsum[1001];
bool useddiff[1001];

int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0);
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	map<char,int> M;
	M['.']=0;
	M['x']=2;
	M['+']=1;
	M['o']=3;
	int t; cin>>t;
	for(int zz = 1; zz <= t; zz++)
	{
		cout<<"Case #"<<zz<<": ";
		memset(usedrow,0,sizeof(usedrow));
		memset(usedsum,0,sizeof(usedsum));
		memset(usedcol,0,sizeof(usedcol));
		memset(useddiff,0,sizeof(useddiff));
		int m; cin>>n>>m;
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < n; j++)
			{
				a[i][j]='.';
				res[i][j]=0;
			}
		}
		
		for(int i = 0; i < m; i++)
		{
			char c; int x, y;
			cin>>c>>x>>y;
			x--; y--;
			a[x][y]=c;
			res[x][y]=M[c];
			if(M[c]&2)
			{
				usedrow[x]=1;
				usedcol[y]=1;
			}
			if(M[c]&1)
			{
				usedsum[x+y]=1;
				useddiff[x-y+n]=1;
			}
		}
		init(n,n);
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < n; j++)
			{
				if(!usedrow[i]&&!usedcol[j])
				{
					addedge(i,j);
				}
			}
		}
		maxMatching();
		for(int i = 0; i < n; i++)
		{
			//cerr<<i<<' '<<matching[i]<<'\n';
			if(matching[i]!=-1) res[matching[i]][i]|=2;
		}
		init(2*n,2*n);
		for(int i = 0; i < 2*n; i++)
		{
			for(int j = 0; j < 2*n; j++)
			{
				if(!usedsum[i]&&!useddiff[j])
				{
					if((i+j+n)%2==0)
					{
						int x = (i+j-n)/2; int y = (i-j+n)/2;
						if(isvalid(x,y))
						{
							//cerr<<x<<' '<<y<<'\n';
							addedge(i,j);
						}
					}
				}
			}
		}
		maxMatching();
		for(int i = 0; i < 2*n; i++)
		{
			//cerr<<i<<' '<<matching[i]<<'\n';
			if(matching[i]!=-1)
			{
				assert((i+matching[i]+n)%2==0);
				int x = (matching[i]+i-n)/2;
				int y = (matching[i]-i+n)/2;
				//cerr<<x<<' '<<y<<'\n';
				assert(isvalid(x,y));
				res[x][y]|=1;
			}
		}
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < n; j++)
			{
				ans[i][j]=x[res[i][j]];
			}
		}
		out();
		cerr<<"Case #"<<zz<<" solved.\n";
	}
}
