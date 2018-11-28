#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <queue>

#define mp make_pair
#define pb push_back


typedef long long ll;
typedef long double ld;

using namespace std;

#ifndef LOCAL
#define cerr _cer
struct _cert
{
    template <typename T> _cert& operator << (T) { return *this; }
};
_cert _cer;
#endif

template <typename T> void dprint(T begin, T end) {
    for (auto i = begin; i != end; i++) {
		cerr << (*i) << " ";
    }
    cerr << "\n";
}
const int MAXN = 120;

int was[MAXN * 2];
int a[MAXN][MAXN];
int b[MAXN][MAXN];
int ao[MAXN][MAXN];
int bo[MAXN][MAXN];
int n;
int m;
int q[MAXN * 2];
int p[MAXN * 2];
vector<int> eds[MAXN * 2];
int us11[MAXN];
int us12[MAXN];
int us21[MAXN * 2];
int us22[MAXN * 2];

int dfs1(int v) {
	was[v] = 1;
	for (int u: eds[v]) {
		if (q[u] == -1) {
			q[u] = v;
			p[v] = u;
			return 1;
		}
	}
	for (int u: eds[v]) {
		if (!was[q[u]] && dfs1(q[u])) {
			q[u] = v;
			p[v] = u;
			return 1;
		}
	}
	return 0;
}

void solve() {
	cin >> n >> m;
	for (int i = 0; i < n; ++i)
		us11[i] = 0, us12[i] = 0;
	for (int i = 0; i < 2 * n - 1; ++i)
		eds[i].clear(), us21[i] = 0, us22[i] = 0;
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
			a[i][j] = 0, b[i][j] = 0; 
	for (int i = 0; i < m; ++i) {
		int x, y;
		char c;
		cin >> c >> x >> y;
		--x, --y;
		if (c == 'x' || c == 'o') {
			us11[x] = 1;
			us12[y] = 1;
			a[x][y] = 1;
		}
		if (c == '+' || c == 'o') {
			us21[x + y] = 1;
			us22[x - y + n - 1] = 1;
			b[x][y] = 1;
		}
	}
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
			ao[i][j] = a[i][j], bo[i][j] = b[i][j];
	vector<int> vv1;
	vector<int> vv2;
	for (int i = 0; i < n; ++i)
		if (!us11[i])
			vv1.push_back(i);
	for (int i = 0; i < n; ++i)
		if (!us12[i])
			vv2.push_back(i);
	int g = min(vv1.size(), vv2.size());
	for (int i = 0; i < g; ++i)
		a[vv1[i]][vv2[i]] = 1;
	for (int i = 0; i < 2 * n - 1; ++i) {
		for (int j = 0; j < 2 * n - 1; ++j) {
			if (us21[i] || us22[j])
				continue;
			int x = (i + j) - (n - 1);
			if (x % 2 != 0)
				continue;
			x /= 2;
			if (x < 0 || x >= n)
				continue;
			int y = i - x;
			if (y < 0 || y >= n)
				continue;
			eds[i].push_back(j);
		}
	}
	for (int i = 0; i < 2 * n - 1; ++i)
		p[i] = -1;
	for (int j = 0; j < 2 * n - 1; ++j)
		q[j] = -1;
	for (int i = 0; i < 2 * n - 1; ++i) {
		if (us21[i])
			continue;
		memset(was, 0, sizeof(was[0]) * (2 * n));
		dfs1(i);
	}
	for (int i = 0; i < 2 * n - 1; ++i) {
		if (p[i] == -1)
			continue;
		int x = (i + p[i]) - (n - 1);
		x /= 2;
		int y = i - x;
		b[x][y] = 1;
	}
	int ans = 0;
	int ch = 0;
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j) {
			ans += a[i][j], ans += b[i][j];
			if (a[i][j] != ao[i][j] || b[i][j] != bo[i][j])
				++ch;
		}
	cout << ans << " " << ch << "\n";
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j) {
			if (a[i][j] != ao[i][j] || b[i][j] != bo[i][j]) {
				if (a[i][j] && b[i][j])
					cout << "o ";
				else if (a[i][j])
					cout << "x ";
				else
					cout << "+ ";
				cout << i + 1 << " " << j + 1 << "\n";
			}
		}
}

int main() {
	int tt;
	cin >> tt;
	for (int i = 0; i < tt; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}


