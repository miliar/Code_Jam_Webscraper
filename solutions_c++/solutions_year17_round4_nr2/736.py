#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <queue>

using namespace std;

int n, c, m;

struct Node {
	int p, b;
} nodes[1111];

int times[1111];

namespace flow {
	int cnt, begin[2222], end[2222222], next[2222222], cap[2222222], cost[2222222];
	int s, t;

	void clear() {
		cnt = 0;
		memset(begin, -1, sizeof(begin));
	}

	void addEdge(int u, int v, int c, int w) {
		next[cnt] = begin[u];
		begin[u] = cnt;
		end[cnt] = v;
		cap[cnt] = c;
		cost[cnt ++] = w;
	}

	void add(int u, int v, int c, int w) {
		addEdge(u, v, c, w);
		addEdge(v, u, 0, -w);
	}

	int dist[2222];
	queue<int> q;
	int pre[2222];
	bool inq[2222];

	bool spfa() {
		memset(dist, 0x3f, sizeof(dist));
		memset(inq, 0, sizeof(inq));
		dist[s] = 0;
		q.push(s);
		inq[s] = true;
		while (q.size()) {
			int u = q.front();
			q.pop();
			for (int now = begin[u], v; now != -1; now = next[now]) {
				if (cap[now] && dist[v = end[now]] > dist[u] + cost[now]) {
					dist[v] = dist[u] + cost[now];
					pre[v] = now;
					if (v == t && dist[v] == 0) {
						return true;
					}
					if (!inq[v]) {
						q.push(v);
						inq[v] = true;
					}
				}
			}
		}
		return dist[t] != 0x3f3f3f3f;
	}

	int maxflow, mincost;

	void solve() {
		while (spfa()) {
			int f = 0x3f3f3f3f;
			for (int u = t; u != s; u = end[pre[u] ^ 1]) {
				f = min(f, cap[pre[u]]);
			}
			for (int u = t; u != s; u = end[pre[u] ^ 1]) {
				cap[pre[u]] -= f;
				cap[pre[u] ^ 1] += f;
			}
			maxflow += f;
			mincost += f * dist[t];
		}
	}
}

void init() {
	flow::clear();
	flow::s = c + n;
	flow::t = c + n + 1;
	for (int i = 0; i < m; ++ i) {
		flow::add(nodes[i].b, c + nodes[i].p, 1, 0);
		for (int j = 0; j < nodes[i].p; ++ j) {
			flow::add(nodes[i].b, c + j, 1, 1);
		}
	}
	flow::maxflow = 0;
	flow::mincost = 0;
}

void delta(int cur) {
	for (int i = 0; i < c; ++ i) {
		if (cur < times[i]) {
			flow::add(flow::s, i, 1, 0);
		}
	}
	for (int j = 0; j < n; ++ j) {
		flow::add(c + j, flow::t, 1, 0);
	}
	flow::solve();
}

bool check(int rds) {
	flow::clear();
	flow::s = c + n;
	flow::t = c + n + 1;
	for (int i = 0; i < c; ++ i) {
		flow::add(flow::s, i, min(times[i], rds), 0);
	}
	for (int j = 0; j < n; ++ j) {
		flow::add(c + j, flow::t, rds, 0);
	}
	for (int i = 0; i < m; ++ i) {
		flow::add(nodes[i].b, c + nodes[i].p, 1, 0);
		for (int j = 0; j < nodes[i].p; ++ j) {
			flow::add(nodes[i].b, c + j, 1, 1);
		}
	}
	flow::solve();
	return (flow::maxflow == m);
}

int main() {
	int T;
	scanf("%d", &T);
	for (int kase = 1; kase <= T; ++ kase) {
		scanf("%d%d%d", &n, &c, &m);
		memset(times, 0, sizeof(times));
		for (int i = 0; i < m; ++ i) {
			scanf("%d%d", &nodes[i].p, &nodes[i].b);
			-- nodes[i].p;
			-- nodes[i].b;
			times[nodes[i].b] ++;
		}
		init();
		int ans = 1;
		while (true) {
			delta(ans);
			if (flow::maxflow == m) {
				printf("Case #%d: %d %d\n", kase, ans, flow::mincost);
				break;
			}
			ans ++;
		}
	}
	return 0;
}
