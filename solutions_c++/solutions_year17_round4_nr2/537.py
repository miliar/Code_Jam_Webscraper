#pragma comment(linker,"/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <map>
#include <set>
#include <ctime>
#include <algorithm>
#include <memory.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

#define WR printf
#define RE scanf
#define PB push_back
#define SE second
#define FI first

#define FOR(i,k,n) for(int i=(k); i<=(n); i++)
#define DFOR(i,k,n) for(int i=(k); i>=(n); i--)
#define SZ(a) (int)((a).size())
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define CLR(a) memset(a, 0, sizeof(a))

#define LL long long
#define VI  vector<int>
#define PAR pair<int ,int>
#define o_O 1000000000

void __never(int a){printf("\nOPS %d", a);}
#define ass(s) {if (!(s)) {__never(__LINE__);cout.flush();cerr.flush();abort();}}

// MCMF from e-maxx.ru

const int INF = 1000*1000*1000;

struct rib {
	int b, u, c, f;
	size_t back;
};

void add_rib (vector < vector<rib> > & g, int a, int b, int u, int c) {
	rib r1 = { b, u, c, 0, g[b].size() };
	rib r2 = { a, 0, -c, 0, g[a].size() };
	g[a].push_back (r1);
	g[b].push_back (r2);
}

void mcmf( vector < vector<rib> > & g, int s, int t, int & flow, int & cost, int k )
{
	int n = SZ(g);
	while (flow < k) {
		vector<int> id (n, 0);
		vector<int> d (n, INF);
		vector<int> q (n);
		vector<int> p (n);
		vector<size_t> p_rib (n);
		int qh=0, qt=0;
		q[qt++] = s;
		d[s] = 0;
		while (qh != qt) {
			int v = q[qh++];
			id[v] = 2;
			if (qh == n)  qh = 0;
			for (size_t i=0; i<g[v].size(); ++i) {
				rib & r = g[v][i];
				if (r.f < r.u && d[v] + r.c < d[r.b]) {
					d[r.b] = d[v] + r.c;
					if (id[r.b] == 0) {
						q[qt++] = r.b;
						if (qt == n)  qt = 0;
					}
					else if (id[r.b] == 2) {
						if (--qh == -1)  qh = n-1;
						q[qh] = r.b;
					}
					id[r.b] = 1;
					p[r.b] = v;
					p_rib[r.b] = i;
				}
			}
		}
		if (d[t] == INF)  break;
		int addflow = k - flow;
		for (int v=t; v!=s; v=p[v]) {
			int pv = p[v];  size_t pr = p_rib[v];
			addflow = min (addflow, g[pv][pr].u - g[pv][pr].f);
		}
		for (int v=t; v!=s; v=p[v]) {
			int pv = p[v];  size_t pr = p_rib[v],  r = g[pv][pr].back;
			g[pv][pr].f += addflow;
			g[v][r].f -= addflow;
			cost += g[pv][pr].c * addflow;
		}
		flow += addflow;
	}
}

// end MCMF

int n, c, m;
PAR p[1010];

int check( int rides )
{
	vector < vector<rib> > g (c+m+n+2);

	// 0 - s
	// 1..c - cutomers
	// c+1..c+m - tickets
	// c+m+1..c+m+n - seats
	// c+m+n+1 - t
	FOR(a,1,c) add_rib( g, 0, a, rides, 0 );
	FOR(a,1,m) add_rib( g, p[a].second, c+a, 1, 0 );
	FOR(a,1,m) FOR(b,1,p[a].first) add_rib( g, c+a, c+m+b, 1, b<p[a].first ? 1 : 0 );
	FOR(a,1,n) add_rib( g, c+m+a, c+m+n+1, rides, 0 );

	int flow = 0, cost = 0;
	mcmf( g, 0, c+m+n+1, flow, cost, m );
	if (flow==m) return cost;
	return -1;
}

bool F[4000];

bool dfs( vector < vector<rib> > & g, int v, int t )
{
	F[v] = true;
	if (v==t) return true;
	FA(a,g[v]) if (!F[g[v][a].b])
		if (g[v][a].u > 0)
			if (dfs( g, g[v][a].b, t ))
			{
				g[v][a].u--;
				g[g[v][a].b][g[v][a].back].u++;
				return true;
			}
	return false;
}

bool check2( int rides )
{
	vector < vector<rib> > g (c+m+n+2);

	// 0 - s
	// 1..c - cutomers
	// c+1..c+m - tickets
	// c+m+1..c+m+n - seats
	// c+m+n+1 - t
	FOR(a,1,c) add_rib( g, 0, a, rides, 0 );
	FOR(a,1,m) add_rib( g, p[a].second, c+a, 1, 0 );
	FOR(a,1,m) FOR(b,1,p[a].first) add_rib( g, c+a, c+m+b, 1, b<p[a].first ? 1 : 0 );
	FOR(a,1,n) add_rib( g, c+m+a, c+m+n+1, rides, 0 );

	int flow = 0;
	while (1)
	{
		CLR( F );
		if (dfs( g, 0, c+m+n+1 )) flow++;
		else break;
		if (flow==m) return true;
	}
	return false;
}

void sol()
{
	int mi = 0, ma = 1010;
	while (mi+1 < ma)
	{
		int sr = (mi+ma)/2;
		if (!check2(sr)) mi = sr;
		else ma = sr;
	}
	cout << ma << " " << check(ma);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	cin >> T;
	FOR(z,1,T)
	{
		cerr << z << "\n";
		cin >> n >> c >> m;
		FOR(a,1,m) cin >> p[a].first >> p[a].second;
		cout << "Case #" << z << ": ";
		sol();
		cout << "\n";
	}
	cerr << "time = " << clock() << "\n";
	return 0;
}
