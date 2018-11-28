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

int hd, ad, hk, ak, b, d;

inline void gen() {
	return;
}

inline bool read() {
	if (!(cin >> hd >> ad >> hk >> ak >> b >> d)) return false;
	return true;
}

int ds[N][N][N][N];

inline void add(queue<pair<pt, pt> >& q, int myh, int myat, int hish, int hisat, int d) {
	if (ds[myh][myat][hish][hisat] == INF) {
		ds[myh][myat][hish][hisat] = d;
		q.push(mp(pt(myh, myat), pt(hish, hisat)));
	}
}

inline void solve() {
	forn(i, N) forn(j, N) forn(k, N) forn(l, N) ds[i][j][k][l] = INF;
	ds[hd][ad][hk][ak] = 0;
	queue<pair<pt, pt> > q;
	q.push(mp(pt(hd, ad), pt(hk, ak)));

	while (!q.empty()) {
		pair<pt, pt> qq = q.front();
		q.pop();
		int myH = qq.x.x, myAt = qq.x.y;
		int hisH = qq.y.x, hisAt = qq.y.y;
		//Attack
		int curd = ds[myH][myAt][hisH][hisAt];
		if (hisH == 0) {
			cout << curd << endl;
			return;
		}

		{
			int nhisH = max(0, hisH - myAt);
			if (nhisH == 0) {
				add(q, myH, myAt, nhisH, hisAt, curd + 1);
			}
			else {
				int nmyH = max(0, myH - hisAt);
				if (nmyH) add(q, nmyH, myAt, nhisH, hisAt, curd + 1);
			}
		}

		{
			int nmyAt = min(100, myAt + b);
			int nmyH = max(0, myH - hisAt);
			if(nmyH) add(q, nmyH, nmyAt, hisH, hisAt, curd + 1);
		}

		{
			int nmyH = hd;
			nmyH = max(0, nmyH - hisAt);
			if (nmyH) add(q, nmyH, myAt, hisH, hisAt, curd + 1);
		}

		{
			int nhisAt = max(0, hisAt - d);
			int nmyH = max(0, myH - nhisAt);
			if (nmyH) add(q, nmyH, myAt, hisH, nhisAt, curd + 1);
		}
	}

	cout << "IMPOSSIBLE" << endl;
	return;
}

int main() {
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
		cout << "Case #" << i + 1 << ": ";
		solve();
		//cerr << "curTime == " << clock() << " ms" << endl;
	}

#ifdef _DEBUG
	cerr << "TIME == " << clock() << " ms" << endl;
#endif
	return 0;
}