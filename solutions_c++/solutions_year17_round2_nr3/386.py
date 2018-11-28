#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <cstdio>

//#include <cstdint>
//#include <cstdlib>
#include <cassert>
//#include <cctype>
#include <climits>
#include <functional>
#include <numeric>
#include <algorithm>
#include <cmath>
#include <ctime>

#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <list>
#include <deque>
#include <unordered_set>
#include <unordered_map>
#include <bitset>
#include <array>

using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define forn1(i, n) for(int i = 1; i <= int(n); i++)
#define sz(a) int((a).size())
#define all(a) (a).begin(), (a).end()
#define mp make_pair
#define pb push_back
#define x first
#define y second

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld PI = acosl(ld(-1));
const ld EPS = 1e-9;

template <typename T> inline T sqr(const T& x) {
	return x * x;
}

template <typename T> inline T abs(const T& x) {
	return x > 0 ? x : -x;
}

inline bool inside(int x, int y, int n, int m) {
	return x >= 1 && x <= n && y >= 1 && y <= m;
}

inline int rnd() {
	return abs(rand() ^ (rand() << 15));
}

inline int rnd(int n) {
	assert(n > 0);
	return rnd() % n;
}

inline int rnd(int lf, int rg) {
	return lf + rnd(rg - lf + 1);
}

inline li rndLL() {
	return rnd() * 1LL * rnd() + rnd();
}

const int dx[4] = { -1, 0, +1, 0 };
const int dy[4] = { 0, +1, 0, -1 };

const int dx8[8] = { -1, -1, 0, +1, +1, +1, 0, -1 };
const int dy8[8] = { 0, +1, +1, +1, 0, -1, -1, -1 };

const int N = int(111);

int n, q;
int g[N][N];
pt qs[N];
int maxdist[N], speed[N];

inline void gen() {
	n = 100;
	q = 100;
	forn(i, n) {
		maxdist[i] = rnd(INF) + 1;
		maxdist[i] = INF;
		speed[i] = rnd(1000) + 1;
	}

	forn(i, n) forn(j, n) {
		if (i == j) {
			g[i][j] = -1;
		}
		else {
			g[i][j] = rnd(INF) + 1;
		}
	}

	forn(i, q) {
		qs[i].x = rnd(n);
		qs[i].y = rnd(n);
		while (qs[i].x == qs[i].y) {
			qs[i].x = rnd(n);
			qs[i].y = rnd(n);
		}
	}
	return;
}

inline bool read() {
	//gen(); return true;
	if (scanf("%d %d", &n, &q) != 2) return false;
	forn(i, n) (scanf("%d %d", &maxdist[i], &speed[i]) == 2);
	forn(i, n) forn(j, n) (scanf("%d", &g[i][j]) == 1);
	forn(i, q) {
		(scanf("%d %d", &qs[i].x, &qs[i].y) == 2);
		qs[i].x--;
		qs[i].y--;
	}
	return true;
}

li d[N][N];
ld minTime[N][N];

inline void Dijkstra(li * d, int s) {
	forn(i, N) d[i] = INF64;
	d[s] = 0;
	set<pair<li, int> > Q;
	Q.insert(mp(0, s));

	while (!Q.empty()) {
		int v = Q.begin()->y;
		Q.erase(Q.begin());
		forn(i, n) {
			int to = i;
			if (g[v][to] != -1 && d[v] + g[v][to] < d[to]) {
				Q.erase(mp(d[to], to));
				d[to] = d[v] + g[v][to];
				Q.insert(mp(d[to], to));
			}
		}
	}
}

inline void prepareTimes() {
	forn(i, n) Dijkstra(d[i], i);
	forn(i, N) forn(j, N) minTime[i][j] = INF64;
	forn(i, n) forn(j, n) if (d[i][j] < INF64 / 2 && d[i][j] <= maxdist[i]) {
		minTime[i][j] = ld(d[i][j]) / speed[i];
	}
}

ld dp[N][N];
bool was[N];

inline void solve() {
	forn(i, N) was[i] = false;
	forn(kk, q) {
		int s = qs[kk].x, t = qs[kk].y;
		forn(i, N) forn(j, N) dp[i][j] = INF64;
		dp[0][s] = 0;
		forn(step, N - 1) forn(v, n) {
			ld cur = dp[step][v];
			if (cur > INF64 / 2) continue;
			forn(to, n) if (minTime[v][to] < INF64 / 2) {
				dp[step + 1][to] = min(dp[step + 1][to], cur + minTime[v][to]);
			}
		}

		ld nans = INF64;
		forn(step, N) nans = min(nans, dp[step][t]);
		if (nans > INF64 / 2) {
			cerr << "WTF BAD ANS" << endl;
			//assert(false);
		}
		if (kk) cout << ' ';
		cout << nans;
	}
	cout << endl;
	return;
}

int main() {
	/*
	ifstream in1("output.txt");
	ifstream in2("output01.txt");
	ld x1, x2;
	while (1) {
		string s1, s2;
		in1 >> s1;
		if (!in1) break;
		in2 >> s2;
		cerr << s1 << " == " << s2 << endl;
		if (s1 != s2) {
			cerr << "BAD!!!" << endl;
			while (1);
		}
		
		forn(k, 2) cin >> 
		in2 >> x2;
		cerr << x1 << ' ' << x2 << endl;
		ld diff = fabs(x1 - x2);
		if (diff > EPS) {
			cerr << "BAD!!!" << endl;
			while (1);
		}
		
	}

	return 0;
	*/
	//assert(false);
//#ifdef _DEBUG
	(freopen("input.txt", "rt", stdin));
	(freopen("output.txt", "wt", stdout));
//#endif

	cout << setprecision(10) << fixed;
	cerr << setprecision(10) << fixed;

	srand(int(time(NULL)));

	int T = 1;
	#define MULTITEST
#ifdef MULTITEST
	(scanf("%d", &T) == 1);
#endif

	forn(i, T) {
//#ifdef _DEBUG
		cerr << "TEST == " << i << endl;
//#endif
		(read());
		//read();
		prepareTimes();
		cout << "Case #" << i + 1 << ": ";
		solve();
		cerr << "curTime == " << clock() << " ms" << endl;
	}

#ifdef _DEBUG
	cerr << "TIME == " << clock() << " ms" << endl;
#endif
	return 0;
}