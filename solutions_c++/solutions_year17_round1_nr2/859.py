#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < n; i ++)
typedef long long LL;
const int N = 55;
const int inf = 1e9;
int Q[N][N];
int R[N];

template<int N, typename T> struct MaxFlow {
	int src, sink, list[N], tot, Q[N], s, t, d[N], cur[N];
	struct Edge { int v, x; T cap; } E[555555];
	void init() {
		memset(list, -1, sizeof list);
		tot = 0;
	}
	void addedge(int u, int v, T cap) {
		E[tot] = (Edge) {v, list[u], cap};
		list[u] = tot ++;
		E[tot] = (Edge) {u, list[v], 0};
		list[v] = tot ++;
	}
	bool bfs() {
		memset(d, -1, sizeof d);
		memcpy(cur, list, sizeof cur);
		d[src] = 0;
		s = t = 0;
		Q[t ++] = src;
		while(s < t) {
			int u = Q[s ++];
			for(int i = list[u]; ~i; i = E[i].x) {
				Edge &e = E[i];
				if(d[e.v] == -1 && E[i].cap > 0) {
					d[Q[t ++] = e.v] = d[u] + 1;
				}
			}
		}
		return d[sink] != -1;
	}
	T dfs(int u, T in) {
		if(u == sink)    return in;
		T flow = 0, f;
		for(int &i = cur[u]; ~i; i = E[i].x) {
			Edge &e = E[i];
			if(e.cap > 0 && d[e.v] == d[u] + 1) {
				if(f = dfs(e.v, std::min(in - flow, e.cap))) {
					flow += f;
					e.cap -= f;
					E[i^1].cap += f;
					if(flow == in)    break;
				}
			}
		}
		if(flow < in)    d[u] = -1;
		return flow;
	}
	T dinic(int _src, int _sink) {
		src = _src;
		sink = _sink;
		T flow = 0;
		while(bfs())    flow += dfs(src, inf);
		return flow;
	}
};

MaxFlow<5000, int> F;
int n, P;

int idx(int i, int j) {
	return i*P + j;
}

struct Node {
	int L, R;

	Node(){}
	Node(int q, int p) {
		L = ceil(q / (p * 1.1));
		R = int(q / (p * 0.9));
	}

} interval[N][N];

int main() {
	int T;
	scanf("%d", &T);
	rep(cas, T) {
		scanf("%d%d", &n, &P);
		rep(i, n) {
			scanf("%d", R + i);
		}
		rep(i, n) {
			rep(j, P) {
				scanf("%d", &Q[i][j]);
				interval[i][j] = Node(Q[i][j], R[i]);
			}
		}
		F.init();
		int src = n*P, sink = n*P+1;
		for (int i = 1; i < n; i ++) {
			for (int j = 0; j < P; j ++) {
				if (interval[i][j].R < interval[i][j].L) {
					continue;
				}
				for (int pj = 0; pj < P; pj ++) {
					if (interval[i-1][pj].R < interval[i-1][pj].L) {
						continue;
					}
					if (!(interval[i][j].R < interval[i-1][pj].L) && !(interval[i][j].L > interval[i-1][pj].R)) {
						F.addedge(idx(i-1, pj), idx(i, j), 1);
					}
				}
			}
		}
		rep(i, P) {
			if (interval[0][i].R >= interval[0][i].L) {
				F.addedge(src, i, 1);
			}
			F.addedge(idx(n-1, i), sink,  1);
		}
		int answer = F.dinic(src, sink);
		printf("Case #%d: %d\n", cas + 1, answer);
	}
	return 0;
}
