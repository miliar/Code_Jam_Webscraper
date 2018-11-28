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
	return x >= 0 && x < n && y >= 0 && y < m;
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

int n, p, a[N];
vector<int> v[N];

inline void gen() {
	return;
}

inline bool read() {
	if (!(cin >> n >> p)) return false;
	forn(i, n) (cin >> a[i]);
	//p = 4;
	return true;
}

map<vector<int>, int> dp[N][5];

inline void solve() {
	forn(i, N) v[i].clear();
	forn(i, n) {
		v[a[i] % p].push_back(a[i]);
	}

	forn(i, p) sort(all(v[i]));
	forn(i, N) forn(j, 5) dp[i][j].clear();
	vector<int> init(p, 0);
	dp[0][0][init] = 0;
	forn(step, n) forn(mod, p) {
	//	cerr << "step mod == " << step << ' ' << mod << endl;
		const auto& curMap = dp[step][mod];
		for (const pair<vector<int>, int>& vv : curMap) {
			vector<int> vec = vv.x;
			int val = vv.y;
		//	cerr << "vec == " << endl;
			//forn(j, sz(vec)) cerr << vec[j] << ' '; cerr << endl;
		//	cerr << "val == " << val << endl;
			forn(type, p) {
				if (vec[type] + 1 <= sz(v[type])) {
					vec[type]++;
					int nmod = (mod - type + p) % p;
					/*
					if (mod >= v[type][vec[type] - 1]) {
						nmod = mod - v[type][vec[type] - 1];
					}
					else {
						nmod = (mod + v[type][vec[type] - 1]) % p;
						nmod = (p - nmod) % p;
					}
					*/
					int add = int(mod == 0);
					if (dp[step + 1][nmod].count(vec)) dp[step + 1][nmod][vec] = max(dp[step + 1][nmod][vec], val + add);
					else dp[step + 1][nmod][vec] = val + add;
				//	cerr << "get type == " << type << endl;
				//	cerr << "nval nmod == " << val + add << ' ' << nmod << endl;
					vec[type]--;
				}
			}
		}
	}

	int ans = 1;
	forn(mod, p) for (const auto& x : dp[n][mod]) ans = max(ans, x.y);
	cout << ans << endl;
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
		cerr << "curTime == " << clock() << " ms" << endl;
	}

#ifdef _DEBUG
	cerr << "TIME == " << clock() << " ms" << endl;
#endif
	return 0;
}