#include <bits/stdc++.h>
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define RFOR(i,b,a) for (int i = (b)-1; i >= (a); i--)
#define ITER(it,a) for (__typeof(a.begin()) it = a.begin(); it != a.end(); it++)
#define FILL(a,value) memset(a, value, sizeof(a))

#define SZ(a) (int)a.size()
#define ALL(a) a.begin(), a.end()
#define PB push_back
#define MP make_pair

typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;

const double PI = acos(-1.0);
const int INF = 1000 * 1000 * 1000 + 7;
const LL LINF = INF * (LL) INF;

const int MAX = 2020;
/*
struct edge
{
	int from,to;
	LL cap, flow;
};

vector<edge> E;
VI g[MAX];
int D[MAX];
int Q[MAX];
int ptr[MAX];

void addEdge(int from,int to,int cap)
{
	edge e;
	e.from = from;
	e.to = to;
	e.cap = cap;
	e.flow = 0;
	g[from].PB(SZ(E));
	E.PB(e);

	swap(e.from,e.to);
	e.cap = 0;
	g[to].PB(SZ(e));
	E.PB(e);
}

int bfs(int s,int t)
{
	FILL(D,-1);
	D[s] = 0;
	Q[0] = s;
	int qh = 0,qt = 1;
	while(qh<qt && D[t] == -1)
	{
		int v = Q[qh++];
		FOR(i,0,SZ(g[v]))
		{
			edge e = E[g[v][i]];
			if(e.cap!=e.flow && D[e.to] == -1)
			{
				D[e.to] = D[v] + 1;
				Q[qt++] = e.to;
			}
		}
	}

	return D[t];
}

LL dfs(int v,int t,LL flow)
{
	if(v == t || !flow)return flow;
	for(;ptr[v]<SZ(g[v]);ptr[v]++)
	{
		int ind = g[v][ptr[v]];
		edge e = E[ind];
		if(D[e.to] == D[e.from] + 1 && e.cap != e.flow)
		{
			LL f = dfs(e.to,t,min(flow,e.cap - e.flow));
			if(f>0)
			{
				E[ind].flow += f;
				E[ind^1].flow -= f;
				return f;
			}
		}
	}

	return 0;
}

LL dinic(int from,int to)
{
	LL res = 0;
	while(bfs(from,to)!=-1)
	{
		FILL(ptr,0);
		while(true)
		{
			LL p = dfs(from,to,INF);
			if(p==0)break;
			res += p;
		}
	}

	return res;
}
*/

VI g[MAX];
int mt[MAX];
int P[MAX];
int U[MAX];
int iter;
bool kun(int x)
{
	if(U[x] == iter) return false;
	U[x] = iter;
	FOR(i,0,SZ(g[x]))
	{
		int to = g[x][i];
		if(mt[to] == -1)
		{
			mt[to] = x;
			P[x] = to;
			return true;
		}
	}

	FOR(i,0,SZ(g[x]))
	{
		int to = g[x][i];
		if(kun(mt[to]))
		{
			mt[to] = x;
			P[x] = to;
			return true;
		}
	}
	return false;
}

int doKun(int n)
{
	FILL(mt,-1);
	FILL(P,-1);
	FILL(U,-1);
	int res = 0;
	iter = 0;
	while(true)
	{
		iter++;
		bool ok = false;
		FOR(i,0,n)
		{
			if(P[i] == -1)
			{
				if(!kun(i))
				{
					ok = 1;
					res++;
				}
			}
		}
		if(!ok)break;
	}

	return res;
}

int CNT[8];

int n;
int COL[MAX];
string solve()
{
	FOR(i,0,n*2+47)g[i].clear();

	// 0 .. n-1 in
	// n .. n*2-1 out
	// n*2 .. n*2+3 -rby

	FOR(i,0,n)
	{
		FOR(j,0,n)
		{
			if(COL[i]&COL[j])continue;
			else g[i].PB(j);
		}
	}

	int f = doKun(n);
	if(f!=n)
	{
		return "IMPOSSIBLE";
	}


}

string CS = "0RYOBVG";
int main()
{
//	freopen("in.txt", "r", stdin);
	freopen("B.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tests;
	cin>>tests;
	FOR(test,1,tests+1)
	{
		cin>>n;
		int r,o,y,g,b,v;
		cin>>r>>o>>y>>g>>b>>v;

		CNT[1] = r;
		CNT[2] = y;
		CNT[4] = b;
		CNT[3] = o;
		CNT[5] = v;
		CNT[6] = g;

		int ind = 0;
		FOR(i,1,7)
		FOR(j,0,CNT[i])
		{
			COL[ind++] = i;
		}

		int mx = 0;
		FOR(i,0,3)
		{
			if(CNT[1<<i]>CNT[1<<mx])mx = i;
		}

		string res(n,'X');
		bool ok = true;
		ind = 0;
		FOR(i,0,CNT[1<<mx])
		{
			while(ind<n && (res[ind]!='X' || (ind>0 && res[ind-1]==CS[1<<mx])))++ind;
			if(ind>=n)
			{
				ok = false;
				break;
			}
			res[ind] = CS[1<<mx];
		}

		int mx2 = -1;
		FOR(i,0,3)
		{
			if(i!=mx && (mx2==-1 || CNT[1<<i]>CNT[1<<mx2]))mx2 = i;
		}

		FOR(i,0,CNT[1<<mx2])
		{
			while(ind<n && (res[ind]!='X' || (ind>0 && res[ind-1]==CS[1<<mx2])))++ind;
			if(ind>=n)
			{
				ind = 1;
			}
			res[ind] = CS[1<<mx2];
		}

		printf("Case #%d: ",test);

		FOR(i,0,3)
		{
			if(i==mx || i == mx2)continue;
			FOR(j,0,CNT[1<<i])
			{
				while(ind<n && (res[ind]!='X' || res[ind-1] == CS[1<<i]))++ind;
				if(ind>=n)
				{
					ind = 1;
				}
				res[ind] = CS[1<<i];
			}
		}

		FOR(i,0,n)
		{
			if(res[i] == res[(i+1)%n] || res[i] == 'X')ok=false;
		}

//		cerr<<res<<" "<<CS[1<<mx]<<endl;

		if(!ok) res = "IMPOSSIBLE";
		puts(res.c_str());
		cerr<<res<<endl;
	}
}
