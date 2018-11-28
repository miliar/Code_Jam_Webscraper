#pragma comment(linker, "/STACK:60000000")
#define _CRT_SECURE_NO_WARNINGS

#include <bitset>
#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>
#include <iomanip>
#include <complex>
#include <queue>
#include <functional>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)
#define next NEXT64
#define prev PREV64
#define y1 Y164

typedef long long int64;
typedef pair <int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;
const string task = "";

template <class T> T sqr(T x) { return x * x; }

string cols = "ROYGBV";
int num[256];

int n, m;
int cnt[6];
int deg[6];
int a[6][6];
vector<int> vans;

void add(int v, int w, int x) {
	a[v][w] += x;
	a[w][v] += x;
}

void dfs(int v) {
	forn(i, 6) {
		if (a[v][i] == 0) continue;
		a[v][i]--;
		a[i][v]--;
		dfs(i);
	}
	vans.pb(v);
}

bool ok(char c1, char c2) {
	if (c1 == c2) return false;
	if (c1 == 'O') return c2 != 'R' && c2 != 'Y';
	if (c1 == 'G') return c2 != 'Y' && c2 != 'B';
	if (c1 == 'V') return c2 != 'B' && c2 != 'R';
	return true;
}

string solve() {
	seta(a, 0);
	scanf("%d", &n);
	forn(i, 6) num[cols[i]] = i;
	forn(i, 6) {
		scanf("%d", &cnt[i]);
		deg[i] = cnt[i] * 2;
	}
	add(1, 4, deg[1]);
	deg[4] -= deg[1];
	deg[1] = 0;
	add(3, 0, deg[3]);
	deg[0] -= deg[3];
	deg[3] = 0;
	add(5, 2, deg[5]);
	deg[2] -= deg[5];
	deg[5] = 0;
	forn(i, 6) {
		if (deg[i] < 0) {
			return "IMPOSSIBLE";
		}
	}
	forn(i, n*2) {
		int x = 0;
		forn(j, 3)
			if (deg[j * 2] > deg[x]) x = j * 2;
		if (deg[x] == 0) break;
		int y = -1;
		forn(j, 3) {
			int v = j * 2;
			if (v == x) continue;
			if (y == -1 || deg[v] > deg[y]) y = v;
		}
		if (deg[x] <= 0 || deg[y] <= 0) return "IMPOSSIBLE";
		deg[x]--;
		deg[y]--;
		a[x][y]++;
		a[y][x]++;
	}
	vans.clear();
	forn(i, 6) {
		if (cnt[i] > 0) {
			dfs(i);
			break;
		}
	}
	if (vans.size() != n + 1) return "IMPOSSIBLE";

	string ans = "";
	forn(i, n) {
		ans += cols[vans[i]];
	}
	forn(i, n) {
		assert(ok(ans[i], ans[(i + 1) % n]));
	}
	return ans;
}

int main() {
	//	freopen ((task + ".in").data(), "r", stdin);
	//	freopen ((task + ".out").data(), "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.in.out", "w", stdout);
	int tt;
	scanf("%d", &tt);
	for (int i = 1; i <= tt; i++) {
		printf("Case #%d: %s\n", i, solve().data());
	}
	return 0;
}
