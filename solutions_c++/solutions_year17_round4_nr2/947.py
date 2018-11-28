#include <bits/stdc++.h>

using namespace std;

#define forn(i,n) for (int i = 0; i < int(n); i++)
#define ford(i,n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i,l,r) for (int i = int(l); i <= int(r); i++)
#define all(a) a.begin(), a.end()
#define sz(a) int(a.size())
#define mp make_pair
#define pb push_back
#define ft first
#define sc second
#define x first
#define y second

template<typename X> inline X abs(const X& a) { return a < 0 ? -a : a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9;

int n, c, m;
vector<pt> v;
const int N = 2000 + 5;
vector<int> q[N];

inline bool read() {
	cin >> n >> c >> m;
	cerr << n << ' ' << c << ' ' << m << endl;
	v.resize(m);
	forn (i, N)
		q[i].clear();
	forn (i, m) {
		cin >> v[i].x >> v[i].y;
		q[v[i].x - 1].pb(v[i].y - 1);
	}
	return true;
}
   
int ans = 0;
set<int> used[N];

struct edge {
	int to, cost, flow, cap, back;
};

vector<edge> g[N];

void add_edge(int v, int u, int cost, int cap = 1) {
	edge fe = {u, cost, 0, cap, sz(g[u])};
	edge be = {v, -cost, 0,  0, sz(g[v])};
	g[v].pb(fe);
	g[u].pb(be);	
}

bool inq[N];
int d[N];
pt p[N];

bool enlarge(int s, int t) {
	forn (i, N)
		d[i] = INF;
	d[s] = 0;
	queue<int> q;
	q.push(s);
	while(!q.empty()) {
		int v = q.front();
		q.pop();
		inq[v] = false;
		forn (i, sz(g[v])) {
			edge e = g[v][i];
			if (e.cap == e.flow)
				continue;
			if (d[e.to] > d[v] + e.cost) {
				d[e.to] = d[v] + e.cost;
				p[e.to] = mp(v, i);
				if (!inq[e.to]) {
					inq[e.to] = true;
					q.push(e.to);
				}	
			}
		}
	}
	if (d[t] == INF)
		return false;
	ans += d[t];
	while(t != s) {
		int v = p[t].x, i = p[t].y;
		g[v][i].flow++;
		g[t][g[v][i].back].flow--;
		assert(g[t][g[v][i].back].to == v);
		t = v;
	}
	return true;
}

int maxflow(int s, int t) {
	ans = 0;
	int flow = 0;
	while(enlarge(s, t))
		flow++;
	return flow;
}

int ok(int mid) {
	forn (i, N)
		used[i].clear(), g[i].clear();
	int f = 0;
	forn (i, n)
		for (int man : q[i]) {
			if (man != 0)
				continue;
			used[f++].insert(i);
			if (f > mid)
				return false;
		}
	int cnt2 = m - mid;
	int s = cnt2 + mid;
	int t = s + 1;
	f = 0;
	forn (i, n) {
		for (int man : q[i]) {
			if (man == 0)
				continue;
			forn (j, mid)
				if (!used[j].count(i))
					add_edge(f, cnt2 + j, 0);
				else {
					if (i != 0)
						add_edge(f, cnt2 + j, 1);
				}
			f++;
		}
	}
	forn (i, f)
		add_edge(s, i, 0);
	cerr << mid << endl;
	forn (i, mid)
		add_edge(cnt2 + i, t, 0);
	int add = f - maxflow(s, t);
	assert(add >= 0);
	return mid + add;
}

inline void solve() {
	int cnt1 = 0;
	forn (i, m)
		cnt1 += v[i].y == 1;   
	cout << ok(cnt1) << ' ';
	cout << ans << endl;
}

int main()
{
#ifdef SU2
	assert(freopen("in.in", "r", stdin));
	assert(freopen("output.txt", "w", stdout));
#endif

	cout << setprecision(25) << fixed;
	cerr << setprecision(10) << fixed;

	srand(int(time(NULL)));

	int t;
	cin >> t;
	forn (i, t) {
		cerr << i + 1 << endl;
		cout << "Case #" << i + 1 << ": ";
	assert(read());
	solve();
	
	}

#ifdef SU2
	cerr << "TIME: " << clock() << endl;
#endif

	return 0;
}	