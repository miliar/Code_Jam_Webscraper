//Template
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <climits>
#include <cmath>
#include <utility>
#include <set>
#include <map>
#include <queue>
#include <ios>
#include <iomanip>
#include <ctime>
#include <numeric>
#include <functional>
#include <fstream>
#include <string>
#include <vector>
#include <bitset>
#include <cstdarg>
#include <complex>
using namespace std;

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef long double ld;
#define pair(x, y) make_pair(x, y)
#define runtime() ((double)clock() / CLOCKS_PER_SEC)

inline int read() {
	static int r, sign;
	static char c;
	r = 0, sign = 1;
	do c = getchar(); while (c != '-' && (c < '0' || c > '9'));
	if (c == '-') sign = -1, c = getchar();
	while (c >= '0' && c <= '9') r = r * 10 + (int)(c - '0'), c = getchar();
	return sign * r;
}

template <typename T>
inline void print(T *a, int n) {
	for (int i = 1; i < n; ++i) cout << a[i] << " ";
	cout << a[n] << endl;
}
#define PRINT(_l, _r, _s, _t) { cout << #_l #_s "~" #_t #_r ": "; for (int _i = _s; _i != _t; ++_i) cout << _l _i _r << " "; cout << endl; }

#define N 100
int T = 0, Case = 0;
long long f[N + 1][N + 1], d[N + 1][N + 1], e[N + 1], s[N + 1];
double nd[N + 1][N + 1], nf[N + 1][N + 1];

const long long INFI = (long long)1e15;

int main(int argc, char *argv[]) {
#ifdef KANARI
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	cin >> T;
	while (T--) {
		int n, q;
		cin >> n >> q;
		for (int i = 1; i <= n; ++i)
			cin >> e[i] >> s[i];
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j) {
				cin >> d[i][j];
				if (d[i][j] == -1) d[i][j] = INFI;
				f[i][j] = d[i][j];
			}
		for (int i = 1; i <= n; ++i)
			f[i][i] = 0;
		for (int k = 1; k <= n; ++k)
			for (int i = 1; i <= n; ++i)
				for (int j = 1; j <= n; ++j)
					f[i][j] = min(f[i][j], f[i][k] + f[k][j]);
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j)
				if (f[i][j] <= e[i]) {
					nd[i][j] = (double)f[i][j] / s[i];
					nf[i][j] = nd[i][j];
				} else {
					nf[i][j] = (double)INFI;
				}
		for (int k = 1; k <= n; ++k)
			for (int i = 1; i <= n; ++i)
				for (int j = 1; j <= n; ++j)
					nf[i][j] = min(nf[i][j], nf[i][k] + nf[k][j]);
		cout << "Case #" << ++Case << ":";
		cout << fixed << setprecision(8);
		while (q--) {
			int x, y;
			cin >> x >> y;
			cout << " " << nf[x][y];
		}
		cout << endl;
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
