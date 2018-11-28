#include <bits/stdc++.h>

#define _overload(_1,_2,_3,name,...) name
#define _rep(i,n) _range(i,0,n)
#define _range(i,a,b) for(int i=int(a);i<int(b);++i)
#define rep(...) _overload(__VA_ARGS__,_range,_rep,)(__VA_ARGS__)

#define _rrep(i,n) _rrange(i,n,0)
#define _rrange(i,a,b) for(int i=int(a)-1;i>=int(b);--i)
#define rrep(...) _overload(__VA_ARGS__,_rrange,_rrep,)(__VA_ARGS__)

#define _all(arg) begin(arg),end(arg)
#define uniq(arg) sort(_all(arg)),(arg).erase(unique(_all(arg)),end(arg))
#define getidx(ary,key) lower_bound(_all(ary),key)-begin(ary)
#define clr(a,b) memset((a),(b),sizeof(a))
#define bit(n) (1LL<<(n))
#define popcount(n) (__builtin_popcountll(n))

using namespace std;

template<class T>bool chmax(T &a, const T &b) { return (a < b) ? (a = b, 1) : 0;}
template<class T>bool chmin(T &a, const T &b) { return (b < a) ? (a = b, 1) : 0;}

using ll = long long;
using R = long double;
const R EPS = 1e-9L; // [-1000,1000]->EPS=1e-8 [-10000,10000]->EPS=1e-7
inline int sgn(const R& r) {return (r > EPS) - (r < -EPS);}
inline R sq(R x) {return sqrt(max(x, 0.0L));}

const int dx[8] = {1, 0, -1, 0, 1, -1, -1, 1};
const int dy[8] = {0, 1, 0, -1, 1, 1, -1, -1};

// Problem Specific Parameter:

// Description: グラフの型定義
// Verifyed: Many Diffrent Problem

//Appropriately Changed
using edge = struct {int to;};
using G = vector<vector<edge>>;

//Appropriately Changed
void add_edge(G &graph, int from, int to) {
	graph[from].push_back({to});
	graph[to].push_back({from});
}

// Description: 2部グラフに対する最大マッチング
// TimeComplexity: $ \mathcal{O}(EV) $
// Verifyed: AOJ GRL_7_A

int bipartite_matching(const G &graph) {
	int res = 0, n = graph.size();
	vector<int> match(n, -1), used(n, 0);

	auto dfs = [&](int v) {
		auto func = [&](int v, auto func)->int{
			used[v] = true;
			for (auto &e : graph[v]) {
				const int u = e.to, w = match[u];
				if (w < 0 || (!used[w] && func(w, func))) {
					match[v] = u, match[u] = v;
					return true;
				}
			}
			return false;
		};
		return func(v, func);
	};

	rep(v, n) {
		if (match[v] >= 0) continue;
		fill(_all(used), false);
		if (dfs(v)) res++;
	}
	return res;
}

#define error(args...) { vector<string> _debug = split(#args, ',');err(begin(_debug), args);}

vector<string> split(const string& s, char c){
	vector<string> v;stringstream ss(s);string x;
	while (getline(ss, x, c)) v.emplace_back(x);
	return move(v);
}

void err(vector<string>::iterator it) {cerr << endl;}
template<typename T, typename... Args> void err(vector<string>::iterator it, T a,Args... args){
	cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << " ",err(++it, args...);
}
int main(void) {
	// GCJ Template
	int T;
	cin >> T;
	rep(testcase, 1, T + 1) {
		int n, c, m;
		cin >> n >> c >> m;

		int p[1010], b[1010];

		rep(i, m) {
			cin >> p[i] >> b[i];
			b[i]--;
		}

		if (c >= 3) continue;


		vector<int> tmp[2];
		rep(i, m) tmp[b[i]].push_back(p[i]);

		const int zero = tmp[0].size();
		const int one = tmp[1].size();

		G graph(m);
		G graph2(m);

		rep(i, zero)rep(j, one) {
			if (tmp[0][i] != tmp[1][j]) {
				add_edge(graph, i, j + zero);
			}
		}

		rep(i, zero)rep(j, one) {
			if (tmp[0][i] != 1 or tmp[1][j] != 1) {
				add_edge(graph2, i, j + zero);
			}
		}

		int cur = m - bipartite_matching(graph);
		int opt = m - bipartite_matching(graph2);
		int cost = cur - opt;

		//error(cur,opt);
		cout << "Case #" << testcase << ": " << opt << " " << cost << endl;
		cerr << "Case #" << testcase << ": Done!"  << endl;
	}
	return 0;
}