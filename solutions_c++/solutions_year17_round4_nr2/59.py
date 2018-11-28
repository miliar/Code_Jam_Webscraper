#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define nfor(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i, l, r) for (int i = int(l); i < int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(x, y) make_pair((x), (y))
#define x first
#define y second

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

template<typename A, typename B> inline ostream& operator<< (ostream& out, const pair<A, B>& p) { return out << "(" << p.x << ", " << p.y << ")"; }
template<typename T> inline ostream& operator<< (ostream& out, const vector<T>& a) { out << "["; forn(i, sz(a)) { if (i) out << ','; out << ' ' << a[i]; } return out << " ]"; } 
template<typename T> inline ostream& operator<< (ostream& out, const set<T>& a) { return out << vector<T>(all(a)); }
template<typename X, typename Y> inline ostream& operator<< (ostream& out, const map<X, Y>& a) { return out << vector<pair<X, Y>>(all(a)); }
template<typename T> inline ostream& operator<< (ostream& out, pair<T*, int> a) { return out << vector<T>(a.x, a.x + a.y); }

inline ld gett() { return ld(clock()) / CLOCKS_PER_SEC; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

#ifdef SU1
#define LOG
#endif

const int K = 100 * 1000 + 3; //count of vertex
const int M = 3000 * 1000 + 13; //count of edges

struct edge
{
	int to;
	int cap;
	int cost;
	int flow;

	edge() {}
	edge(int to, int cap, int cost) : to(to), cap(cap), cost(cost), flow(0) {}
};

int sze = 0;
edge e[M];

vector<int> g[K];

inline void addEdge(int v, int to, int cap, int cost)
{
 	g[v].pb(sze);
 	e[sze++] = edge(to, cap, cost);

 	g[to].pb(sze);
 	e[sze++] = edge(v, 0, -cost);
	assert(sze < M);
}

int q[M], head, tail;
char inQ[K];
int d[K];
int p[K], pe[K];

int flow, cost;

inline bool enlarge(int s, int t)
{
	head = tail = 0;
		
	forn (i, t + 1)  //be careful!!
	{
		d[i] = INF;
		inQ[i] = 0;
	}
	
	d[s] = 0;
	inQ[s] = 1;
	q[tail++] = s;
	
	while (head != tail)
	{
		int v = q[head++];
		inQ[v] = 0;

		if (head == M)
			head = 0;
		
		forn (i, sz(g[v]))
		{
			int id = g[v][i];
			
			if (e[id].flow >= e[id].cap)
				continue;
				
			int to = e[id].to;
			
			if (d[to] > d[v] + e[id].cost)
			{
				d[to] = d[v] + e[id].cost;
				p[to] = v;
				pe[to] = id;
				
				if (!inQ[to])
				{
					inQ[to] = 1;
					q[tail++] = to;
					
					if (tail == M)
						tail = 0;
				}
			}
		}
	}
	
	if (d[t] == INF)
		return false;
		
	int addFlow = INF;
	
	for (int v = t; v != s; v = p[v])
	{
		int id = pe[v];
		
		addFlow = min(addFlow, e[id].cap - e[id].flow);
	}
	
	flow += addFlow;
	
	for (int v = t; v != s; v = p[v])
	{
		int id = pe[v];
		
		e[id].flow += addFlow;
		e[id ^ 1].flow -= addFlow;
	}
	
	cost += d[t] * addFlow;
	
	return true;
}

int n, m, k;
int seat[K], person[K];
int cs[K];

bool read() {
	if (!(cin >> n >> m >> k))
		return false;
	forn(i, m)
		cs[i] = 0;
	forn(i, k) {
		assert(cin >> seat[i] >> person[i]);
		seat[i]--;
		person[i]--;
		cs[person[i]]++;
	}
	return true;
}

int fr[K];

void solve(int tc) {
	printf("Case #%d: ", tc + 1);
	flow = 0;
	cost = 0;
	forn(i, K)
		g[i].clear();
	sze = 0;

	int S = k + 2 * n; 
	int T = S + 1;
		
	forn(i, k) {
		addEdge(S, i, 1, 0);
		addEdge(i, k + seat[i], 1, 0);
		addEdge(i, k + seat[i] + n, 1, 0);
	}
	
	forn(i, n)
		addEdge(k + n + i, k + i, k, 0);

	forn(i, n - 1)
		addEdge(k + n + i + 1, k + n + i, k, 0);


	int res = 0;
	int maxcs = 0;
	forn(i, m)
		maxcs = max(maxcs, cs[i]);

	while (flow < k || res < maxcs) {
		res++;
		forn(i, n)
			addEdge(k + i, T, 1, 0);
		while (enlarge(S, T));
	}

	forn(i, n) {
		fr[i] = res;
	}

	forn(i, k) {
		fr[seat[i]]--;
		if (fr[seat[i]] < 0)
			cost++;
	}

	assert(flow == k);
	cout << res << " " << cost << endl;
}

int main() {
#ifdef SU1
    assert(freopen("input.txt", "rt", stdin));
    assert(freopen("output.txt", "wt", stdout));
#endif
    
    cout << setprecision(10) << fixed;
    cerr << setprecision(5) << fixed;

	int t;
	assert(cin >> t);

	forn(test, t) {
		assert(read());
		ld stime = gett();
		solve(test);
		cerr << "Time: " << gett() - stime << endl;
		//break;
	}
	
    return 0;
}
