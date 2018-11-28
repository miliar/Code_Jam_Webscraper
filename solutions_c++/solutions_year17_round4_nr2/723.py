#include <bits/stdc++.h>
using namespace std;

// why am I so weak

int n, c, m;
vector<int> con[1055];

typedef pair<int, int> P;

#define ft first
#define sd second

P p[1055];

int prom;

vector<int> can[1055];
multiset<int> temp[1055];

inline bool trial(int have) {
	int a = 0;

	for (int i = 0; i < n; i++) {
		temp[i].clear();
		for (auto u : can[i]) {
			temp[i].insert(u);
		}
	}

	for (int i = 0; i < have; i++) {
		set<int> s;
		set<int> in;

		for (int j = 0; j < n; j++) {
			s.insert(j);

			vector<int> del;

			for (auto u : temp[j]) if (!s.empty() && !in.count(u)) {
				del.push_back(u);
				in.insert(u);
				a++;
				s.erase(*s.rbegin());
			}

			for (auto u : del) temp[j].erase(temp[j].find(u));
		}
	}

	return a == m;
}
const int INF = 1e9;
int iter[2050055], level[2050055];;

struct edge {int to; int cap; int rev;};
vector<edge> g[2050055];
void add_edge(int from, int to, int cap) {
	g[from].push_back((edge){to, cap, (int)g[to].size()});
	g[to].push_back((edge){from, 0, (int)g[from].size() - 1});
}
void bfs(int s) {
	queue<int> que;
	memset(level, -1, sizeof(level));
	que.push(s);

	level[s] = 0;

	while (!que.empty()) {
		int u = que.front(); que.pop();
		for (auto e : g[u]) {
			if (e.cap > 0 && level[e.to] < 0) {
				level[e.to] = level[u] + 1;
				que.push(e.to);
			}
		}
	}
}
int dfs(int v, int t, int f) {
	if (v == t) return f;

	for (int &i = iter[v]; i < (int)g[v].size(); i++) {
		edge &e = g[v][i];

		if (e.cap > 0 && level[e.to] > level[v]) {
			int d = dfs(e.to, t, min(f, e.cap));

			if (d > 0) {
				e.cap -= d;
				g[e.to][e.rev].cap += d;
				return d;
			}
		}
	}
	
	return 0;
}
int max_flow(int s, int t) {
	int res = 0;

	for (; ; ) {
		bfs(s);
		if (level[t] < 0) return res;
		int f;
		memset(iter, 0, sizeof(iter));
		while ((f = dfs(s, t, INF)) > 0) res += f;
	}
}
inline void calc(int have) {
	prom = 0;

	for (int i = 0; i < c; i++) {
		map<int, int> s;

		for (auto u : con[i]) {
			s[u]++;
		}

		for (auto p : s) {
			add_edge(c * n + have * n, i * n + p.first, p.second);
			for (int j = 0; j < have; j++) {
				add_edge(i * n + p.first, c * n + j * n + p.first, 1);
			}
		}
	}

	int s = c * n + have * n, t = s + 1;

	for (int i = 0; i < have; i++) for (int j = 0; j < n; j++) {
		add_edge(c * n + i * n + j, t, 1);
	}

	prom = m - max_flow(s, t);
}
int main() {
	int _t;

	scanf("%d", &_t);

	for (int _ = 0; _ < _t; _++) {
		printf("Case #%d: ", _ + 1);

		scanf("%d %d %d", &n, &c, &m);

		for (int i = 0; i < max(n, max(c, m)); i++) {
			con[i].clear();
			can[i].clear();
		}

		for (int i = 0; i < (int)2e6 + 5000; i++) {
			g[i].clear();
		}

		for (int i = 0; i < m; i++) {
			scanf("%d %d", &p[i].ft, &p[i].sd);
			p[i].ft--, p[i].sd--;
			con[p[i].sd].push_back(p[i].ft);
			can[p[i].ft].push_back(p[i].sd);
		}

		int lb = 0, ub = m;

		while (ub - lb > 1) {
			int mid = (ub + lb) >> 1;
			if (trial(mid)) ub = mid;
			else lb = mid;
		}

		calc(ub);
		printf("%d %d\n", ub, prom);
	}

	return 0;
}

