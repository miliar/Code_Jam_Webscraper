// need
#include <iostream>
#include <algorithm>

// data structure
#include <bitset>
//#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>
//#include <array>
//#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <complex>
//#include <deque>
#include<valarray>

// stream
//#include <istream>
//#include <sstream>
//#include <ostream>
#include<fstream>

// etc
#include <cassert>
#include <functional>
#include <iomanip>
//#include <typeinfo>
#include <chrono>
#include <random>
#include <numeric>

#define INIT std::ios::sync_with_stdio(false);std::cin.tie(0);
#define VAR(type, ...)type __VA_ARGS__;MACRO_VAR_Scan(__VA_ARGS__);
template<typename T> void MACRO_VAR_Scan(T& t) { std::cin >> t; }
template<typename First, typename...Rest>void MACRO_VAR_Scan(First& first, Rest&...rest) { std::cin >> first; MACRO_VAR_Scan(rest...); }
#define VEC_ROW(type, n, ...)std::vector<type> __VA_ARGS__;MACRO_VEC_ROW_Init(n, __VA_ARGS__); for(int i=0; i<n; ++i){MACRO_VEC_ROW_Scan(i, __VA_ARGS__);}
template<typename T> void MACRO_VEC_ROW_Init(int n, T& t) { t.resize(n); }
template<typename First, typename...Rest>void MACRO_VEC_ROW_Init(int n, First& first, Rest&...rest) { first.resize(n); MACRO_VEC_ROW_Init(n, rest...); }
template<typename T> void MACRO_VEC_ROW_Scan(int p, T& t) { std::cin >> t[p]; }
template<typename First, typename...Rest>void MACRO_VEC_ROW_Scan(int p, First& first, Rest&...rest) { std::cin >> first[p]; MACRO_VEC_ROW_Scan(p, rest...); }
#define OUT(d) std::cout<<d;
#define FOUT(n, d) std::cout<<std::fixed<<std::setprecision(n)<<d;
#define SOUT(n, c, d) std::cout<<std::setw(n)<<std::setfill(c)<<d;
#define SP std::cout<<" ";
#define TAB std::cout<<"\t";
#define BR std::cout<<"\n";
#define ENDL std::cout<<std::endl;
#define FLUSH std::cout<<std::flush;
#define VEC(type, c, n) std::vector<type> c(n);for(auto& i:c)std::cin>>i;
#define MAT(type, c, m, n) std::vector<std::vector<type>> c(m, std::vector<type>(n));for(auto& r:c)for(auto& i:r)std::cin>>i;
#define ALL(a) (a).begin(),(a).end()
#define FOR(i, a, b) for(int i=(a);i<(b);++i)
#define RFOR(i, a, b) for(int i=(b)-1;i>=(a);--i)
#define REP(i, n) for(int i=0;i<int(n);++i)
#define RREP(i, n) for(int i=(n)-1;i>=0;--i)
#define FORLL(i, a, b) for(ll i=ll(a);i<ll(b);++i)
#define RFORLL(i, a, b) for(ll i=ll(b)-1;i>=ll(a);--i)
#define REPLL(i, n) for(ll i=0;i<ll(n);++i)
#define RREPLL(i, n) for(ll i=ll(n)-1;i>=0;--i)
#define PAIR std::pair<int, int>
#define PAIRLL std::pair<ll, ll>
#define IN(a, x, b) (a <= x && x < b)
#define SHOW(d) {std::cerr << #d << "\t:" << d << "\n";}
#define SHOWVECTOR(v) {std::cerr << #v << "\t:";for(const auto& xxx : v){std::cerr << xxx << " ";}std::cerr << "\n";}
#define SHOWVECTOR2(v) {std::cerr << #v << "\t:\n";for(const auto& xxx : v){for(const auto& yyy : xxx){std::cerr << yyy << " ";}std::cerr << "\n";}}
#define SHOWPAIR(p) {std::cerr << #p << "\t:(" << p.first << ",\t" << p.second << ")\n";}
#define SHOWPAIRVECTOR2(v) {std::cerr << #v << "\t:\n";for(const auto& xxx : v){for(const auto& yyy : xxx){std::cerr<<'('<<yyy.first<<", "<<yyy.second<<") ";}std::cerr << "\n";}}
#define SHOWPAIRVECTOR(v) {for(const auto& xxx:v){std::cerr<<'('<<xxx.first<<", "<<xxx.second<<") ";}std::cerr<<"\n";}
#define SHOWQUEUE(a) {std::queue<decltype(a.front())> tmp(a);std::cerr << #a << "\t:";for(int i=0; i<static_cast<int>(a.size()); ++i){std::cerr << tmp.front() << "\n";tmp.pop();}std::cerr << "\n";}
template<typename T> inline T CHMAX(T& a, const T b) { return a = (a < b) ? b : a; }
template<typename T> inline T CHMIN(T& a, const T b) { return a = (a > b) ? b : a; }
#define EXCEPTION(msg) throw std::string("Exception : " msg " [ in ") + __func__ + " : " + std::to_string(__LINE__) + " lines ]"
#define TRY(cond, msg) try {if (cond) EXCEPTION(msg);}catch (std::string s) {std::cerr << s << std::endl;}
void CHECKTIME(std::function<void()> f) { auto start = std::chrono::system_clock::now(); f(); auto end = std::chrono::system_clock::now(); auto res = std::chrono::duration_cast<std::chrono::nanoseconds>((end - start)).count(); std::cerr << "[Time:" << res << "ns  (" << res / (1.0e9) << "s)]\n"; }

std::ostream& operator<<(std::ostream& os, const PAIR& r) {
	os << "(" << r.first << ", " << r.second << ")";
	return os;
}

#define int ll
using ll = long long;
using ull = unsigned long long;
constexpr int INFINT = 1 << 30;                          // 1.07x10^ 9
constexpr int INFINT_LIM = (1LL << 31) - 1;              // 2.15x10^ 9
constexpr ll INFLL = 1LL << 60;                          // 1.15x10^18
constexpr ll INFLL_LIM = (1LL << 62) - 1 + (1LL << 62);  // 9.22x10^18
constexpr double EPS = 1e-7;
constexpr int MOD = 1000000007;
constexpr double PI = 3.141592653589793238462643383279;

template<typename T>
void OUTPUT(int i, T d) {
	OUT("Case #")OUT(i)OUT(": ")OUT(d)BR;
}

// Dinic法
class Dinic {
private:
	struct Edge {
		int to, cap, rev;
		Edge(int t, int c, int r) :to(t), cap(c), rev(r) {}
	};
	int V;
	std::vector<std::vector<Edge>> graph;
	std::vector<int> level, iter;

public:
	Dinic(int v) : V(v) {
		graph.resize(v);
		level.resize(v, -1);
		iter.resize(v, 0);
	}
	// fromからtoへ向かう容量capの辺をグラフに追加する
	void addEdge(int from, int to, int cap) {
		graph[from].emplace_back(to, cap, graph[to].size());
		graph[to].emplace_back(from, 0, graph[from].size() - 1);
	}

	// sからの最短距離をBFSで計算する
	void bfs(int s) {
		std::fill(level.begin(), level.end(), -1);
		std::queue<int> queue;
		level[s] = 0;
		queue.push(s);
		while (!queue.empty()) {
			int v = queue.front(); queue.pop();
			for (int i = 0; i < graph[v].size(); ++i) {
				Edge& e = graph[v][i];
				if (e.cap > 0 && level[e.to] < 0) {
					level[e.to] = level[v] + 1;
					queue.push(e.to);
				}
			}
		}
	}

	// 増加パスをDFSで探す
	int dfs(int v, int t, int f) {
		if (v == t) return f;
		for (int& i = iter[v]; i < graph[v].size(); ++i) {
			Edge& e = graph[v][i];
			if (e.cap > 0 && level[v] < level[e.to]) {
				int d = dfs(e.to, t, std::min(f, e.cap));
				if (d > 0) {
					e.cap -= d;
					graph[e.to][e.rev].cap += d;
					return d;
				}
			}
		}
		return 0;
	}

	// sからtへの最大流を求める
	int maxFlow(int s, int t) {
		int res = 0;
		while (true) {
			bfs(s);
			if (level[t] < 0) return res;
			std::fill(iter.begin(), iter.end(), 0);
			int f;
			while ((f = dfs(s, t, (1LL << 31) - 1)) > 0) {
				res += f;
			}
		}
	}
};

signed main() {
	INIT;
	
	VAR(int, T);

	REP(_, T) {
		VAR(int, n, p);
		VEC(int, r, n);
		MAT(int, q, n, p);

		if (n == 1) {
			int ans = 0;
			REP(j, p) {
				int k1 = std::floor(10.0*q[0][j] / 11 / r[0]) - 1;
				CHMAX(k1, 0LL);
				int k2 = std::floor(10.0*q[0][j] / 9 / r[0]) + 1;
				FOR(k, k1, k2 + 1) {
					if (9 * k*r[0] <= 10 * q[0][j] && 10 * q[0][j] <= 11 * k*r[0]) {
						++ans;
						break;
					}
				}
			}
			OUTPUT(_ + 1, ans);
		}
		else {

			struct Data {
				int min, max;
				Data() : min(-1), max(-2) {}
			};

			std::vector<std::vector<Data>> v(n, std::vector<Data>(p));
			REP(i, n) {
				REP(j, p) {
					int k1 = std::floor(10.0*q[i][j] / 11 / r[i]) - 1;
					CHMAX(k1, 0LL);
					int k2 = std::floor(10.0*q[i][j] / 9 / r[i]) + 1;
					FOR(k, k1, k2 + 1) {
						if (9 * k*r[i] <= 10 * q[i][j] && 10 * q[i][j] <= 11 * k*r[i]) {
							v[i][j].min = k;
							break;
						}
					}
					RFOR(k, k1, k2 + 1) {
						if (9 * k*r[i] <= 10 * q[i][j] && 10 * q[i][j] <= 11 * k*r[i]) {
							v[i][j].max = k;
							break;
						}
					}
				}
			}

			Dinic g(n*p + 2);
			REP(j, p) {
				g.addEdge(0, j + 1, 1);
			}
			REP(i, n - 1) {
				REP(j, p) REP(j2, p) {
					if (v[i][j].max < v[i + 1][j2].min || v[i + 1][j2].max < v[i][j].min) continue;
					g.addEdge(i*p + j + 1, (i + 1)*p + j2 + 1, 1);
				}
			}
			REP(j, p) {
				g.addEdge((n - 1)*p + j + 1, n*p + 1, 1);
			}
			int ans = g.maxFlow(0, n*p + 1);
			OUTPUT(_ + 1, ans);
		}
	}

	return 0;
}