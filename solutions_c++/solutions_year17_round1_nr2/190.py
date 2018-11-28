#pragma GCC optimize(2)
#include <bits/stdc++.h>
#define LL long long
#define INF 0x3f3f3f3f
using namespace std;

template<class T> inline
void read(T& x) {
	int f = 1; x = 0;
	char ch = getchar();
	while (ch < '0' || ch > '9')   {if (ch == '-') f = -1; ch = getchar();}
	while (ch >= '0' && ch <= '9') {x = x * 10 + ch - '0'; ch = getchar();}
	x *= f;
}

/*============ Header Template ============*/

const int N = 50 + 5;
const int M = 100000 + 5;

struct dinic {
	int S, T;
	int cur[N * N], L[N * N], vis[N * N];
	int first[N * N], e;
	queue<int> Q;
	struct edge {int v, next, flow;} s[2 * M];

	void init() {e = 0; memset(first, -1, sizeof(first));}

	void addedge(int u, int v, int flow) {
		s[e].next = first[u]; s[e].v = v; s[e].flow = flow; first[u] = e++;
		s[e].next = first[v]; s[e].v = u; s[e].flow = 0;    first[v] = e++;
	}

	int lable() {
		while (!Q.empty()) Q.pop();
		memset(vis, 0, sizeof(vis));
		Q.push(S); vis[S] = 1, L[S] = 0;
		while (!Q.empty()) {
			int u = Q.front(); Q.pop();
			for (int e = first[u]; e != -1; e = s[e].next) {
				int v = s[e].v;
				if (!vis[v] && s[e].flow ) {
					vis[v] = 1;
					L[v] = L[u] + 1;
					Q.push(v);
				}
			}
		}
		return vis[T];
	}

	int dfs(int u, int a) {
		if (u == T || a == 0) return a;
		int flow = 0, f;
		for (int& e = cur[u]; e != -1; e = s[e].next) {
			int v = s[e].v;
			if (L[u] + 1 == L[v]) {
				int f = dfs(v, min(a, s[e].flow));
				s[e].flow -= f, s[e ^ 1].flow += f;
				flow += f;
				a -= f;
				if (a == 0) break;
			}
		}
		return flow;
	}

	int Maxflow(int s, int t) {
		S  = s; T = t;
		int flow = 0;
		while (lable()) {
			for (int i = S; i <= T; i++) cur[i] = first[i];
			flow += dfs(s, INF);
		}
		return flow;
	}

} g;

int n, m, idx;
int R[N], Q[N][N];
int lb[N][N], rb[N][N], in[N][N], out[N][N];

int main() {
	int T, kas = 0;
	read(T);
	while (T--) {
		read(n), read(m);
		for (int i = 1; i <= n; i++) read(R[i]);
		idx = 0;
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++) {
				read(Q[i][j]);
				in[i][j] = ++idx;
				out[i][j] = ++idx;
			}
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				double r = 1.0 * Q[i][j] / 0.9 / R[i];
				double l = 1.0 * Q[i][j] / 1.1 / R[i];
				lb[i][j] = (int)ceil(l);
				rb[i][j] = (int)floor(r);
				if (lb[i][j] > rb[i][j]) {
					lb[i][j] = rb[i][j] = 0;
				}
			}
		}
		g.init();
		int S = 0, T = 2 * n * m + 1;
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++) g.addedge(in[i][j], out[i][j], 1);
		for (int i = 1; i <= m; i++)
			if (rb[1][i] > 0) g.addedge(S, in[1][i], 1);
		for (int i = 1; i < n; i++)
			for (int j = 1; j <= m; j++)
				for (int k = 1; k <= m; k++) {
					if (max(lb[i][j], lb[i + 1][k]) <= min(rb[i][j], rb[i + 1][k]) && min(rb[i][j], rb[i + 1][k]) > 0) {
						g.addedge(out[i][j], in[i + 1][k], 1);
					}
				}
		for (int i = 1; i <= m; i++) if (rb[n][i] > 0)
				g.addedge(out[n][i], T, 1);
		printf("Case #%d: %d\n", ++kas, g.Maxflow(S, T));
	}
	return 0;
}
