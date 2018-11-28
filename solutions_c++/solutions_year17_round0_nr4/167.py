#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define sz(x) ((int)(x).size())
#define rep(i,l,r) for(int i=(l);i<(r);++i)
//-------
const int N = 407;
const int M = 1e5 + 7;
int n, m, tot, r[N], c[N], d[N], fd[N];
int S[] = { 0, 1, 1, 2 };
char CH[] = { " x+o" };
struct Node {
	char ch;
	int x, y;
	Node() {
	}
	Node(char _ch, int _x, int _y) {
		ch = _ch, x = _x, y = _y;
	}
};
int a[N][N], b[N][N];
void calc_x() {
	rep(i, 0, n)
		rep(j, 0, n)
			if (!r[i] && !c[j])
				++tot, ++a[i][j], ++r[i], ++c[j];	
//	printf("tot_x = %d\n", tot);
}
struct MaxFlow {
	static const ll LINF = 1e18 + 7;
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
bool check(int D, int F) {
	int x = (D + F - (n - 1)) >> 1;
	int y = D - x;
	return !(x < 0 || x >= n || y < 0 || y >= n);
}
void calc_plus() {
	int S = 0, T = (n << 2) + 1;
	G.init(T + 1);
	rep(i, 0, 2 * n) {
		G.addEdge(S, i + 1, 1);
		G.addEdge(2 * n + i + 1, T, 1);
	}	
	rep(i, 0, n)
		rep(j, 0, n)
			if (!d[i + j] && !fd[i - j + n - 1])
				G.addEdge(i + j + 1, 2 * n + 1 + i - j + n - 1, 1);
	int tmp = G.dinic(S, T);
//	printf("maxflow = %d\n", tmp);
	tot += tmp;
//	printf("tot_plus = %d\n", tot);
	for (int i = 0; i < G.et; i += 2) {
		if (G.e[i].s == S || G.e[i].t == T || G.e[i].v)
			continue;
		int D = G.e[i].s - 1;
		int F = G.e[i].t - 1 - 2 * n - (n - 1);
		int x = (D + F) >> 1;
		int y = D - x;
//		printf("%d, %d, x = %d, y = %d\n", D, F + n - 1, x, y);
		a[x][y] |= 2;
	}
}
int main() {
	freopen("D.out", "w", stdout);
	int T;
	scanf("%d", &T);
	rep(cas, 0, T) {
		scanf("%d%d", &n, &m);
		rep(i, 0, n << 1)
			r[i] = c[i] = d[i] = fd[i] = 0;
		tot = 0;
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		rep(i, 0, m) {
			char ch;
			int x, y;
			scanf(" %c %d %d", &ch, &x, &y);
			--x, --y;
			tot += ch == 'o' ? 2 : 1;
			if (ch != 'x') // +
				b[x][y] |= 2, ++d[x + y],  ++fd[x - y + n - 1];
			if (ch != '+') // x
				b[x][y] |= 1, ++r[x], ++c[y];
		}
		calc_x(), calc_plus();
		int add = 0;			
		rep(i, 0, n)
			rep(j, 0, n) {
				add += a[i][j] > 0;
				if (a[i][j] > 0)
					a[i][j] |= b[i][j];
			}
		printf("Case #%d: %d %d\n", cas + 1, tot, add);
		rep(i, 0, n)
			rep(j, 0, n)
				if (a[i][j] > 0)
					printf("%c %d %d\n", CH[a[i][j]], i + 1, j + 1);		
	}
	return 0;
}
