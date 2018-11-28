#include<bits/stdc++.h>
#include<assert.h>
using namespace std;
typedef long long ll;
#define sz(x) ((int)(x).size())
#define rep(i,l,r) for(int i=(l);i<(r);++i)
//-------
struct MinCost {
	const static int N = 2e2 + 7;
	const static int M = 1e5 + 7;
	const static ll LINF = 1e18 + 7;
	const static double DINF = 1e18 + 7;
	struct Edge {
		int s, t, cap, nxt;
		double cost;
		Edge() {
		}
		Edge(int _s, int _t, int _cap, double _cost, int _nxt) {
			s = _s, t = _t, cap = _cap, cost = _cost, nxt = _nxt;
		}
	} e[M * 2];
	double dis[N];
	queue<int> que;
	int n, et, pre[N], vis[N], head[N];
	void init(int _n) {
		n = _n, et = 0;
		memset(head, -1, sizeof(head[0]) * n);
	}
	void addEdge(int s, int t, int cap, double cost) {
		assert(cost + (1e-8) >= -1);
		e[et] = Edge(s, t, cap, cost, head[s]), head[s] = et++;
		e[et] = Edge(t, s, 0, -cost, head[t]), head[t] = et++;
	}
	bool bfs(int S, int T) {
		rep(i, 0, n)
			pre[i] = -1, dis[i] = DINF, vis[i] = false;
		dis[S] = 0, vis[S] = true, que.push(S);
		while (!que.empty()) {
			int u = que.front();
			for (int i = head[u]; ~i; i = e[i].nxt) {
				int v = e[i].t;
				if (e[i].cap > 0 && dis[v] > dis[u] + e[i].cost) {
					pre[v] = i, dis[v] = dis[u] + e[i].cost;
					if (!vis[v])
						vis[v] = true, que.push(v);
				}
			}
			vis[u] = false, que.pop();
		}
		return dis[T] != DINF;
	}
	pair<ll, double> solve(int S, int T) {
		ll maxflow = 0;
		double mincost = 0;
		while (bfs(S, T)) {
			ll flow = LINF;
			for (int i = pre[T]; ~i; i = pre[e[i].s])
				flow = min(flow, (ll) e[i].cap);
			for (int i = pre[T]; ~i; i = pre[e[i].s])
				e[i].cap -= flow, e[i ^ 1].cap += flow;
			maxflow += flow, mincost += flow * dis[T];
		}
		return make_pair(maxflow, mincost);
	}
} G;
const int N = 107;
int n, q, e[N], s[N];
ll d[N][N]; 
double solve(int u, int v) {
	int S = 0, T = n + 1;
	G.init(T + 1);
	G.addEdge(S, u, 1, 0), G.addEdge(v, T, 1, 0);
	rep(i, 1, n + 1)
		rep(j, 1, n + 1) {
			if (i == j)
				continue;
			if (d[i][j] != -1 && e[i] >= d[i][j])
				G.addEdge(i, j, 1, 1.0 * d[i][j] / s[i]);
		}
	pair<ll, double> ret = G.solve(S, T);
	return ret.second;
}
int main() {
	freopen("C.out", "w", stdout);
	int T;
	scanf("%d", &T);
	rep(cas, 0, T) {
		scanf("%d%d", &n, &q);
		rep(i, 1, n + 1)
			scanf("%d%d", &e[i], &s[i]);
		rep(i, 1, n + 1)
			rep(j, 1, n + 1)
				scanf("%lld", &d[i][j]);
		rep(k, 1, n + 1)
			rep(i, 1, n + 1)
				rep(j, 1, n + 1) {
					if (d[i][k] == -1 || d[k][j] == -1)
						continue;
					if (d[i][j] == -1 || d[i][j] > d[i][k] + d[k][j])
						d[i][j] = d[i][k] + d[k][j];
				}
//		rep(i, 1, n + 1) {
//			rep(j, 1, n + 1)
//				printf("%d ", d[i][j]), assert(-1 <= d[i][j]);
//			puts("");
//		}
		printf("Case #%d:", cas + 1);
		rep(_q, 0, q) {
			int u, v;
			scanf("%d%d", &u, &v);
			double ans = solve(u, v);	
			printf(" %.12f", ans);
		}
		cout << endl;
	}
	return 0;
}
