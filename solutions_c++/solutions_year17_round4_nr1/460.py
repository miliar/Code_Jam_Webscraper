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

const int NMAX = 101;

int n, p;
int s[4];
int t[NMAX][NMAX][NMAX][NMAX][4];

int solve() {
	scanf("%d%d", &n, &p);
	seta(s, 0);
	int sum = 0;
	forn(i, n) {
		int x;
		scanf("%d", &x);
		x %= p;
		s[x]++;
		sum += x;
	}
	sum %= p;
	forn(i0, s[0]+1)
		forn(i1, s[1] + 1)
		forn(i2, s[2] + 1)
		forn(i3, s[3] + 1)
		forn(j, 4)
		t[i0][i1][i2][i3][j] = 0;
	t[0][0][0][0][0] = 0;

	forn(i0, s[0] + 1)
		forn(i1, s[1] + 1)
		forn(i2, s[2] + 1)
		forn(i3, s[3] + 1)
		forn(j, 4) {
		int v = t[i0][i1][i2][i3][j];
		if (j == 0) v++;
		if (i0 < s[0]) t[i0 + 1][i1][i2][i3][j] = max(t[i0 + 1][i1][i2][i3][j], v);
		if (i1 < s[1]) t[i0][i1 + 1][i2][i3][(j + 1) % p] = max(t[i0][i1 + 1][i2][i3][(j + 1) % p], v);
		if (i2 < s[2]) t[i0][i1][i2 + 1][i3][(j + 2) % p] = max(t[i0][i1][i2 + 1][i3][(j + 2) % p], v);
		if (i3 < s[3]) t[i0][i1][i2][i3 + 1][(j + 3) % p] = max(t[i0][i1][i2][i3 + 1][(j + 3) % p], v);
	}
	return t[s[0]][s[1]][s[2]][s[3]][sum];
}

int main() {
	//	freopen ((task + ".in").data(), "r", stdin);
	//	freopen ((task + ".out").data(), "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.in.out.txt", "w", stdout);
	int tt;
	scanf("%d", &tt);
	for (int i = 1; i <= tt; i++) {
		printf("Case #%d: %d\n", i, solve());
	}
	return 0;
}
