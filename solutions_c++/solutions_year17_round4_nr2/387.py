// .... .... .....!
// ...... ......!
// .... ....... ..... ..!
// ...... ... ... .... ... .... .....!
// ... .. ... .... ...?

#include<bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0, _n = (int)(n); i < _n; i++)
#define fer(i, x, n) for (int i = (int)(x), _n = (int)(n); i < _n; i++)
#define rof(i, n, x) for (int i = (int)(n), _x = (int)(x); i-- > _x; )
#define sz(x) (int((x).size()))
#define pb push_back
#define all(X) (X).begin(),(X).end()
#define X first
#define Y second
//#define endl '\n'

template<class P, class Q> inline void smin(P &a, Q b) { if (b < a) a = b; }
template<class P, class Q> inline void smax(P &a, Q b) { if (a < b) a = b; }

typedef long long ll;
typedef pair<int, int> pii;

////////////////////////////////////////////////////////////////////////////////

typedef int FT;
typedef int CT;
struct MinCostFlow {
	static const int maxn = 10000; // ..
	static const int maxm = 2000000;
	static const FT FlowEPS = FT(1e-7);
	static const FT FlowINF = FT(1<<29);
	static const CT CostINF = CT(1<<29); 

	int n, m;
	int to[2*maxm], prv[2*maxm], head[maxn], par[maxn];
	FT cap[2*maxm];
	CT cost[2*maxm], dis[maxn], pot[maxn];
	priority_queue<pair<CT,int>> pq;
	bool mark[maxn];

	void init (int _n) { n = _n, m = 0; rep (i, n) head[i] = -1, pot[i] = 0; }

	inline void add_edge (int u, int v, FT c, CT t) { // ..
		to[m] = v, cap[m] = c, cost[m] =  t, prv[m] = head[u], head[u] = m++;
		to[m] = u, cap[m] = 0, cost[m] = -t, prv[m] = head[v], head[v] = m++;
	}

	pair<FT, CT> pushflow (int source, int sink) {
		rep (i, n) mark[i] = false, dis[i] = CostINF;
		dis[source] = 0, par[source] = -1; pq.push ({0, source});

		while (!pq.empty()) {
			int u = pq.top().Y; pq.pop();
			if (mark[u]) continue; mark[u] = true;
			for (int e = head[u]; e != -1; e = prv[e]) if (cap[e] > FlowEPS && !mark[to[e]]) {
				CT ndis = dis[u] + cost[e] + pot[u] - pot[to[e]];
				if (ndis < dis[to[e]])
					dis[to[e]] = ndis, par[to[e]] = e, pq.push ({-ndis, to[e]});
			}
		}

		pair<FT, CT> ret = {0, 0};
		if (!mark[sink]) return ret;

//		rep (i, n) pot[i] += dis[i];
		ret.X = FlowINF;
		for (int e = par[sink]; e != -1; e = par[to[e^1]]) ret.X = min (ret.X, cap[e]);
		for (int e = par[sink]; e != -1; e = par[to[e^1]])
			cap[e] -= ret.X, cap[e^1] += ret.X, ret.Y += cost[e] * ret.X;
		return ret;
	}

	pair<FT, CT> getflow (int source, int sink) {

		for (bool cont = true; !(cont = !cont); ) {
			rep (u, n) for (int e = head[u]; e != -1; e = prv[e]) if (cap[e] > FlowEPS)
				if (pot[u] + cost[e] < pot[to[e]])
					pot[to[e]] = pot[u] + cost[e], cont = true;
		}

		pair<FT, CT> ret;
		for (pair<FT, CT> tmp; (tmp = pushflow (source, sink)).X; )
			ret.X += tmp.X, ret.Y += tmp.Y;
		return ret;
	}

	void cut (int u, bool clr = 1) { // u = source --> par[setA] = 1, par[setB] = 0;
		if (clr) memset (par, 0, n * sizeof par[0]);
		if (par[u]) return; par[u] = 1;
		for (int e = head[u]; e != -1; e = prv[e])
			if (cap[e] > FlowEPS) cut (to[e], 0);
	}
};
MinCostFlow graph;

const int maxm = 1000 + 10;

int n, c, m;
int p[maxm], b[maxm];
int cnt[maxm];

pii check(int md) {
	graph.init(c + n + n + m + 2);
	int st = c + n + n + m + 2 - 1;
	int ed = c + n + n + m + 2 - 2;
	rep(i, c) graph.add_edge(st, i, cnt[i], 0);

	rep(i, n) graph.add_edge(c + i, c + n + i, md, 0);
	rep(i, n) graph.add_edge(c + n + i, ed, md, 0);
	
	rep(i, n-1) graph.add_edge(c + i + 1, c + i, 10000, 0);

	rep(i, m) graph.add_edge(b[i], c + n + n + i, 1, 0);
	rep(i, m) graph.add_edge(c + n + n + i, c + n + p[i], 1, 0);
	rep(i, m) graph.add_edge(c + n + n + i, c + p[i] - 1, 1, 1);

	return graph.getflow(st, ed);
}

void run() {
	cin >> n >> c >> m;
	rep(i, m) cin >> p[i] >> b[i], p[i]--, b[i]--, cnt[b[i]]++;

	int lo = *max_element(cnt, cnt + c) - 1, hi = maxm;

	while(hi - lo > 1) {
		int md = (lo + hi) / 2;
		pii res = check(md);

		if(res.X == m)
			hi = md;
		else
			lo = md;
	}

	pii ans = check(hi);
	cerr << " $$$ " << ans.X << ' ' << ans.Y << endl;
	cout << hi << ' ' << ans.Y << endl;
}

void case_init() {
	rep(i, maxm) cnt[i] = 0;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);

	int start_clock = clock();
	int tt; cin >> tt;
	for(int tc = 1; tc <= tt; tc++) {
		int case_clock = clock();

		cerr << " -------- #" << tc << ".." << endl;
		case_init();
		cout << "Case #" << tc << ": ";
		run();

		cerr.setf(ios::fixed); cerr.precision(6);
		cerr << " -------- [" << ((clock() - case_clock) / (double)CLOCKS_PER_SEC) << " / " <<
			((clock() - start_clock) / (double)CLOCKS_PER_SEC) << "]" << endl;
	}

	return 0;
}

