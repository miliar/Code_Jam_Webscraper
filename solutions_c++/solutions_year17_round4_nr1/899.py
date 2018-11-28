// VSCF.cpp : Defines the entry point for the console application.
//
#include <bits/stdc++.h>
#include "gurobi_c++.h"
using namespace std;
#define int long long
#define M_PI 3.14159265358979323846
typedef long long LL;
typedef pair<int, int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i)  decltype(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SZ(x) (int)x.size()
#define SIZE(x) SZ(x)
#define ALL(c) c.begin(),c.end()
#define MAXN 1000010
typedef long double LD;
typedef vector<int> VI;

template<class TH> void _dbg(const char *sdbg, TH h) { cerr << sdbg << "=" << h << "\n"; }
template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a) {
	while (*sdbg != ',')cerr << *sdbg++; cerr << "=" << h << ","; _dbg(sdbg + 1, a...);
}

template<class T> ostream &operator<<(ostream &os, vector<T> V) {
	os << "["; for (auto vv : V)os << vv << ","; return os << "]";
}

template<class L, class R> ostream &operator<<(ostream &os, pair<L, R> P) {
	return os << "(" << P.ST << "," << P.ND << ")";
}

#define debug(...) _dbg(#__VA_ARGS__, __VA_ARGS__)

pair<int, vector<int>> brut(vector<int> inp, int n, int p) {
	sort(ALL(inp));
	pair<int, vector<int>> best = { 0, {} };
	do {
		int r = 0;
		int sum = 0;
		REP(i, n) {
			if (!sum) {
				r++;
			}
			sum += inp[i];
			sum %= p;
		}
		best = max(best, { r, inp});
	} while (next_permutation(ALL(inp)));
	return best;
}

vector<int> gen(int n, int p) {
	vector<int> res;
	REP(i, n) {
		res.push_back(rand() % p);
	}
	return res;
}

int wzor(vector<int> inp, int n, int p) {
	vector<int> r(p);
	int total = 0;
	REP(i, n) {
		r[inp[i] % p]++;
		total += inp[i];
		total %= p;
	}

	int sc = r[0] + 1;
	if (p == 2) {
		sc += r[1] / 2;
	}
	else if (p == 3) {
		int tmp1 = min(r[1], r[2]);
		r[1] -= tmp1;
		r[2] -= tmp1;
		sc += tmp1;
		sc += r[1] / 3;
		sc += r[2] / 3;
	}
	else if (p == 4) {
		sc += r[2] / 2;
		r[2] = r[2] & 1;
		int tmp1 = min(r[1], r[3]);
		r[1] -= tmp1;
		r[3] -= tmp1;
		int other = max(r[1], r[3]);
		sc += tmp1;
		if (r[2]) {
			if (other >= 2) {
				other -= 2;
				sc++;
			}
		}
		sc += other / 4;
	}
	if (!total) {
		sc--;
	}
	return sc;
}

void test() {
	int co = 6;
	FOR(p, 2, 4) {
		REP(j, 100) {
			vector<int> inp = gen(6, p);
			pair<int, vector<int>> res = brut(inp, co, p);
			int res2 = wzor(inp, co, p);
			if (res.first != res2) {
				debug(p, inp, res, res2);
				exit(0);
			}
		}
	}
}

int32_t main(int argc, char ** argv) {
	ios_base::sync_with_stdio(0);
	//wzor({ 0,1,1,0,1,2 }, 6, 3);
	//test();
	int t;
	cin >> t;
	REP(_, t) {
		int n , p;
		cin >> n >> p;
		vector<int> inp(n);
		REP(i, n) {
			cin >> inp[i];
		}
		
		cout << "Case #" << _ + 1 << ": " << wzor(inp, n, p) << "\n";
	}
	return 0;
}
