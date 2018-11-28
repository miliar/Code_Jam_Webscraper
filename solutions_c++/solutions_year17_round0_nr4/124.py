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

std::ostream& operator<<(std::ostream& os, const PAIR& r) {
	os << "(" << r.first << ", " << r.second << ")";
	return os;
}

template<typename T>
void OUTPUT(int i, T d, T d2) {
	OUT("Case #")OUT(i)OUT(": ")OUT(d)SP OUT(d2)BR;
}

signed main() {
	INIT;

	VAR(int, T);
	REP(_, T) {
		VAR(int, n, m);
		std::vector<std::vector<bool>> g1(n, std::vector<bool>(n, true));
		std::vector<std::vector<bool>> g2(n, std::vector<bool>(n, true));
		REP(i, m) {
			VAR(char, op);
			VAR(int, r, c);
			--r; --c;
			if (op == '+' || op == 'o') {
				g1[r][c] = false;
			}
			if (op == 'x' || op == 'o') {
				g2[r][c] = false;
			}
		}
		auto r1(g1), r2(g2);
		{
			int N = 2 * n - 1;
			std::vector<std::vector<bool>> gg(N, std::vector<bool>(N, false));
			std::vector<int> ok1(N, 0);
			std::vector<int> ok2(N, 0);
			REP(i, N) REP(j, N) {
				if ((i + j) % 2 == n % 2) continue;
				if (std::abs(i - (n - 1)) + std::abs(j - (n - 1)) > n - 1) continue;
				gg[i][j] = true;
				++ok1[i];
				++ok2[j];
			}
			REP(i, n) REP(j, n) {
				if (!g1[i][j]) {
					int ii = n - 1 + i - j;
					int jj = i + j;
					gg[ii][jj] = false;
					REP(ti, N) {
						ok1[ti] -= gg[ti][jj];
						gg[ti][jj] = false;
					}
					REP(tj, N) {
						ok2[tj] -= gg[ii][tj];
						gg[ii][tj] = false;
					}
					ok1[ii] = 0;
					ok2[jj] = 0;
				}
			}
			while (true) {
				int min = INFINT;
				int min_i = -1, min_j = -1;
				REP(i, N) {
					if (ok1[i] <= 0) continue;
					if (min > ok1[i]) {
						min = ok1[i];
						min_i = i;
						min_j = -1;
					}
				}
				REP(j, N) {
					if (ok2[j] <= 0) continue;
					if (min > ok2[j]) {
						min = ok2[j];
						min_i = -1;
						min_j = j;
					}
				}
				if (min == INFINT) break;
				if (min_i != -1) {
					REP(j, N) {
						if (gg[min_i][j]) {
							int ii = (min_i + j - (n - 1)) / 2;
							int jj = (n - 1 + j - min_i) / 2;
							r1[ii][jj] = false;
							ok1[min_i] = 0;
							ok2[j] = 0;
							REP(ti, N) {
								ok1[ti] -= gg[ti][j];
								gg[ti][j] = false;
							}
							REP(tj, N) {
								ok2[tj] -= gg[min_i][tj];
								gg[min_i][tj] = false;
							}

						}
					}
				}
				else if (min_j != -1) {
					REP(i, N) {
						if (gg[i][min_j]) {
							int ii = (i + min_j - (n - 1)) / 2;
							int jj = (n - 1 + min_j - i) / 2;
							r1[ii][jj] = false;
							ok1[i] = 0;
							ok2[min_j] = 0;
							REP(ti, N) {
								ok1[ti] -= gg[ti][min_j];
								gg[ti][min_j] = false;
							}
							REP(tj, N) {
								ok2[tj] -= gg[i][tj];
								gg[i][tj] = false;
							}
						}
					}
				}
			}
		}
		{
			std::vector<bool> ok1(n, true);
			std::vector<bool> ok2(n, true);
			REP(i, n) REP(j, n) {
				if (!g2[i][j]) {
					ok1[i] = false;
					ok2[j] = false;
				}
			}
			REP(i, n) {
				if (!ok1[i]) continue;
				REP(j, n) {
					if (!ok2[j]) continue;
					r2[i][j] = false;
					ok1[i] = false;
					ok2[j] = false;
					break;
				}
			}
		}

		int cnt = 0;
		struct Data {
			char c;
			int i, j;
			Data(char c, int i, int j) : c(c), i(i), j(j) {}
		};
		std::vector<Data> data;
		REP(i, n) REP(j, n) {
			if (g1[i][j] != r1[i][j] || g2[i][j] != r2[i][j]) {
				char c;
				if (!r1[i][j] && r2[i][j]) c = '+';
				if (r1[i][j] && !r2[i][j]) c = 'x';
				if (!r1[i][j] && !r2[i][j]) c = 'o';
				data.emplace_back(Data(c, i + 1, j + 1));
			}
			cnt += !r1[i][j];
			cnt += !r2[i][j];
		}

		OUTPUT(_ + 1, cnt, (int)data.size());
		REP(i, data.size()) {
			OUT(data[i].c)SP OUT(data[i].i)SP OUT(data[i].j)BR;
		}

		//debug
		/*{
			REP(i, n) {
				REP(j, n) {
					char c = '.';
					if (!r1[i][j] && r2[i][j]) c = '+';
					if (r1[i][j] && !r2[i][j]) c = 'x';
					if (!r1[i][j] && !r2[i][j]) c = 'o';
					OUT(c);
				}BR;
			}
		}*/
	}
	return 0;
}