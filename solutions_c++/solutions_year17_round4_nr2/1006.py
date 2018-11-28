#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define sz(x) ((int)(x).size())
#define rep(i,l,r) for(int i=(l);i<(r);++i)
//-------
const int N = 1e3 + 7;
const int M = 1e6 + 7;
const ll LINF = 1e10 + 7;
int n, m, c;
vector<int> e[N];
struct MaxFlow {
	// N - 点数, M - 边数
	int n, et, dis[N], que[N], cur[N], head[N];
	struct Edge {
		int s, t, v, nxt;
		Edge() {
		}
		Edge(int _s, int _t, int _v, int _nxt) {
			s = _s, t = _t, v = _v, nxt = _nxt;
		}
	} e[M * 2], b[M * 2];
	void undo() {
		rep(i, 0, et)
			e[i] = b[i];
	}
	void backup() {
		rep(i, 0, et)
			b[i] = e[i];
	}
	void init(int _n) {
		n = _n, et = 0;
		memset(head, -1, sizeof(head[0]) * n);
	}
	void addEdge(int s, int t, int v) {
		e[et] = Edge(s, t, v, head[s]), head[s] = et++;
		e[et] = Edge(t, s, 0, head[t]), head[t] = et++;
	}
	bool bfs(int S, int T) {
		int qh = 0, qt = 0;
		memset(dis, -1, sizeof(dis[0]) * n);
		dis[S] = 0, que[qt++] = S;
		while (qh < qt)
			for (int i = head[que[qh++]]; ~i; i = e[i].nxt)
				if (e[i].v && !~dis[e[i].t]) {
					dis[que[qt++] = e[i].t] = 1 + dis[e[i].s];
					if (e[i].t == T)
						return true;
				}
		return false;
	}
	ll dinic(int S, int T) {
		int u, qt;
		ll maxflow = 0;
		while (bfs(S, T)) {
			memcpy(cur, head, sizeof(cur[0]) * n);
			u = S, qt = 0;
			while (~cur[S]) {
				if (u == T) {
					ll flow = LINF;
					for (int i = qt - 1; i >= 0; --i)
						flow = min(flow, (ll) e[que[i]].v);
					for (int i = qt - 1; i >= 0; --i) {
						e[que[i]].v -= flow, e[que[i] ^ 1].v += flow;
						if (!e[que[i]].v)
							qt = i;
					}
					u = e[que[qt]].s, maxflow += flow;
				} else if (~cur[u] && e[cur[u]].v
						&& dis[u] + 1 == dis[e[cur[u]].t]) {
					que[qt++] = cur[u];
					u = e[cur[u]].t;
				} else {
					while (u != S && !~cur[u])
						u = e[que[--qt]].s;
					cur[u] = e[cur[u]].nxt;
				}
			}
		}
		return maxflow;
	}
} G;
pair<int, int> solve() {
	if (c > 2)
		return make_pair(0, 0);	
	int c1 = 0, c2 = 0;
	int S = 0, T = sz(e[1]) + sz(e[2]) + 1;
	G.init(T + 1);				
	rep(i, 0, sz(e[1]))
		if (e[1][i] != 1) 
			G.addEdge(S, i + 1, 1);
		else
			++c1;
	rep(i, 0, sz(e[1]))
		rep(j, 0, sz(e[2]))
			if (e[1][i] != e[2][j])
				G.addEdge(i + 1, sz(e[1]) + j + 1, 1);		
	rep(i, 0, sz(e[2])) 
		if (e[2][i] != 1)
			G.addEdge(sz(e[1]) + i + 1, T, 1);
		else
			++c2;
	int l1 = max(0, sz(e[1]) - c1 - c2), l2 = max(0, sz(e[2]) - c1 - c2);
//	printf("l1 = %d, l2 = %d\n", l1, l2);
	int x = c1 + c2 + max(l1, l2);
	int y = max(0ll, (ll)min(l1, l2) - G.dinic(S, T)); 
	return make_pair(x, y);	
}
int main() {
	freopen("B.out", "w", stdout);
	int T;
	scanf("%d", &T);
	rep(cas, 0, T) {
		scanf("%d%d%d", &n, &c, &m);
		rep(i, 1, c + 1) e[i].clear();	
		rep(i, 0, m) {
			int p, b;
			scanf("%d%d", &p, &b);
			e[b].push_back(p);
		}
//		printf("%d %d\n", sz(e[1]), sz(e[2]));
		pair<int, int> ans = solve();
		printf("Case #%d: %d %d\n", cas + 1, ans.first, ans.second);
	}
	return 0;
}
