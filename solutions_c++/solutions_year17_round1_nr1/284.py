#include <algorithm>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <sstream>
#include <vector>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;

#define FOR(i,n) for (int i=0; i<n; ++i)
#define FORVEC(it,v) for (auto it=(v).begin(); it != (v).end(); ++it)
#define NUL(arr) memset(arr, 0, sizeof(arr));
#define SORT(x) sort((x).begin(), (x).end());

char p[25][25];
int r, c;
string names;

void solve()
{
	names = "";
	cin >> r >> c;
	FOR(y, r) FOR(x, c) cin >> p[y][x];
	FOR(y, r) FOR(x, c) {
		if (p[y][x] != '?') {
			int xl = x - 1;
			while (xl >= 0 && p[y][xl] == '?') {
				p[y][xl] = p[y][x];
				--xl;
			}
			int xr = x + 1;
			while (xr < c && p[y][xr] == '?') {
				p[y][xr] = p[y][x];
				++xr;
			}
		}
	}
	FOR(x, c) {
		if (p[0][x] == '?') {
			int yd = 1;
			while (yd < r && p[yd][x] == '?') ++yd;
			for (int y=0; y<yd; ++y) p[y][x] = p[yd][x];
		}
	}
	FOR(y, r) FOR(x, c) {
		if (p[y][x] == '?') {
			p[y][x] = p[y-1][x];
		}
	}
	FOR(y, r) {
		FOR(x, c) cout << p[y][x];
		cout << endl;
	}
}

int main()
{
	int t;
	cin >> t;
	for (int i=1; i<=t; ++i) {
		cout << "Case #" << i << ": " << endl;
		solve();
	}
	return 0;
}
