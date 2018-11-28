#include <bits/stdc++.h>

#define FOR(i,b,e) for(int i=(b); i <= (e); ++i)
#define FORD(i,b,e) for(int i=(b); i >= (e); --i)
#define REP(i,n) for(int i=0; i < (n); ++i)
#define SIZE(c) (int) (c).size()
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define ST first
#define ND second
#define FWD(i,a,b) for (int i=(a); i<(b); ++i)
#define BCK(i,a,b) for (int i=(a); i>(b); --i)
#define PI 3.14159265358979311600
#define pb push_back
#define mp make_pair
#define st first
#define nd second

using namespace std;

typedef long long ll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;

typedef vector < int > VI;
typedef vector<ll> VL;

typedef long double K;

struct MinCostFlow {
	typedef int capacity_t;
	typedef int cost_t;

	const cost_t INF = 1000 * 1000 * 1000 + 7;
	const capacity_t MAX_CAP = 1000 * 1000 * 1000 + 7;

	struct edge {
		int from, v;
		capacity_t cap, flow;
		cost_t cost, dist;
		int rev_index;
		
		bool residual() { return flow < cap; }
		
		edge(int _f, int _v, capacity_t _cap, cost_t _cost):
			from(_f), v(_v), cap(_cap), flow(0), cost(_cost), dist(_cost) {}
	};

	int n, s, t;
	vector <cost_t> d;
	vector <edge*> p;
	vector <vector<edge>> g;
	vector<int> queued;
	
	MinCostFlow(int n): n(n), d(n), p(n), g(n), queued(n) {}
	
	void bellman() {
		FOR(i,0,n-1) { d[i] = INF; queued[i] = 0; }
		queue <int> q;
		
		d[s] = 0;
		q.push(s); queued[s] = 0;
		
		while (!q.empty()) {
			int u = q.front(); q.pop(); queued[u] = 0;
			
			for (auto &i : g[u]) if (i.residual() && d[i.v] > d[u] + i.dist) {
				d[i.v] = d[u] + i.dist;
				p[i.v] = &i;
				if (!queued[i.v]) { q.push(i.v); queued[i.v] = 1; }
			}
		}
	}

	pair <capacity_t,cost_t> computeFlow(int s, int t) {
		this->s = s;
		this->t = t;

		capacity_t flow = 0;
		cost_t cost = 0;

		while (true) {
			bellman();

			if (d[t] == INF) break;
			cost_t c = 0;
			capacity_t f = MAX_CAP;
			
			for (int u=t; u!=s; u=p[u]->from) {
				f = min(f, p[u]->cap - p[u]->flow);
			}
			
			for (int u=t; u!=s; u=p[u]->from) {
				p[u]->flow += f;
				g[p[u]->v][p[u]->rev_index].flow -= f;
				c += p[u]->cost;
			}
			
			flow += f; cost += f * c;
		}
		
		return {flow, cost};
	}
	
	void add(int a, int b, capacity_t f, cost_t c) {
		assert(a != b);
		
		g[a].pb(edge(a, b, f, c));
		g[b].pb(edge(b, a, 0, -c));
		g[a].back().rev_index = SIZE(g[b])-1;
		g[b].back().rev_index = SIZE(g[a])-1;
	}
};

int n, c, m;
vector<int> p, b, cnt;

int flow, cost;

bool ok(int days) {
	int all = 2 + m + n + n;
	MinCostFlow flow(all);
	int source = all - 1;
	int sink = all - 2;

	for (int i = 1; i < n; ++i) {
		flow.add(i + n + m, i + n + m - 1, 1005, 0);
	}

	for (int i = 0; i < n; ++i) {
		flow.add(i + n + m, m + i, 1005, 0);
	}

	for (int i = 0; i < m; ++i) {
		flow.add(source, i, 1, 0);
		flow.add(i, n + m + p[i], 1, 1);
		flow.add(i, m + p[i], 1, 0);
	}
	for (int i = 0; i < n; ++i) {
		flow.add(m + i, sink, days, 0);
	}
	auto result = flow.computeFlow(source, sink);
	::flow = result.first;
	::cost = result.second;

	return result.first == m;
}

void solve() {
	cin >> n >> c >> m;
	p.assign(m, 0);
	b.assign(m, 0);
	cnt.assign(c, 0);
	REP(i, m) {
		cin >> p[i] >> b[i];
		--p[i]; --b[i];
		++cnt[b[i]];
	}
	int l = 0, r = m + 1;
	REP(i, c) l = max(l, cnt[i] - 1);

	while (r - l > 1) {
		int m = (l + r) / 2;
		if (ok(m)) r = m; else l = m;
	}

	l = r;

	ok(l);

	cout << l << ' ' << cost << '\n';
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int t;
	cin >> t;
	REP(i, t) {
		cout << "Case #" << i+1 << ": ";
		cerr << i << endl;
		solve();
	}

	return 0;
}