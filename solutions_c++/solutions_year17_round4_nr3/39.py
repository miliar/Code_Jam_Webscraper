#include <bits/stdc++.h>
using ll = long long;
using ld = long double;
using namespace std;

const int LMIRROR = -1;
const int RMIRROR = -2;
const int EMPTY = -3;

int mx[4] = { 0, 1, 0, -1 };
int my[4] = { 1, 0, -1, 0 };

const int C = 103;
int a[C][C];
vector <int> visit[C][C];

const int MAXN = C * C * 2;
vector <int> e[MAXN];
int k;
int xc[MAXN], yc[MAXN];
int ans[MAXN];
string anss[MAXN];

int parsesym(char c, int cx, int cy) {
	switch (c) {
	case '/':
		return LMIRROR;
	case '\\':
		return RMIRROR;
	case '#':
		return  0;
	case '.':
		return EMPTY;
	default:
		xc[++k] = cx;
		yc[k] = cy;
		return k;
	}
}

vector <pair <int, int> > gov;

bool Go(int x, int y, int d) {
	do {
		x += mx[d], y += my[d];
		gov.emplace_back(x, y);
		if (a[x][y] == LMIRROR) {
			d = (3 - d);
		}
		if (a[x][y] == RMIRROR) {
			d ^= 1;
		}
	} while (a[x][y] < 0);
	return !a[x][y];
}

void Ad(int fr, int t) {
	e[fr].push_back(t);
}

int N(int x) {
	return (2 * k + 1 - x);
}

void Force(int x) {
	Ad(N(x), x);
}

vector <int> dv;

bool Dfs(int v) {
	if (v <= k) {
		if (ans[v] != 0) return (ans[v] == 1);
		dv.push_back(v);
		ans[v] = 1;
	} else {
		int v2 = N(v);
		if (ans[v2] != 0) return (ans[v2] == 2);
		dv.push_back(v2);
		ans[v2] = 2;
	}

	for (int u : e[v])
		if (!Dfs(u)) return false;
	
	return true;
}

#define No() { cout << "IMPOSSIBLE\n"; return; }
int cas = 0;
void Solve() {
	k = 0;
	memset(a, 0, sizeof(a));
	int r, c;
	cin >> r >> c;
	int sz = r * c;

	for (int i = 1; i <= r; i++) {
		string s;
		cin >> s;
		anss[i] = s;
		for (int j = 0; j < s.length(); j++) {
			a[i][j + 1] = parsesym(s[j], i, j + 1);
			visit[i][j + 1].clear();
		}
	}

	for (int i = 1; i <= 2 * k; i++)
		e[i].clear();

	for (int i = 1; i <= k; i++) {
		int x = xc[i], y = yc[i];
		gov.clear();
		if (Go(x, y, 0) && Go(x, y, 2)) {
			for (auto p : gov) {
				visit[p.first][p.second].push_back(i);
			}
		} else Force(N(i));

		gov.clear();
		if (Go(x, y, 1) && Go(x, y, 3)) {
			for (auto p : gov) {
				visit[p.first][p.second].push_back(N(i));
			}
		} else Force(i);

	}

	for (int i = 1; i <= r; i++) {
		for (int j = 1; j <= c; j++) {
			if (a[i][j] != EMPTY) continue;
			if (visit[i][j].size() == 0) {
				No();
			}
			if (visit[i][j].size() == 1) {
				Force(visit[i][j][0]);
				continue;
			}
			int aa = visit[i][j][0], bb = visit[i][j][1];
			Ad(N(aa), bb);
			Ad(N(bb), aa);
		}
	}

	for (int i = 1; i <= k; i++) ans[i] = 0;

	for (int i = 1; i <= k; i++) {
		if (ans[i]) continue;
		dv.clear();
		if (!Dfs(i)) {
			for (int j : dv) {
				ans[j] = 0;
			}
			dv.clear();
			if (!Dfs(N(i))) No();
		}
	}

	cout << "POSSIBLE\n";

	for (int i = 1; i <= r; i++) {
		for (int j = 1; j <= c; j++) {
			if (a[i][j] > 0)
				anss[i][j - 1] = (ans[a[i][j]] == 1 ? '-' : '|');
		}
		cout << anss[i] << "\n";
	}

	for (int i = 1; i <= r; i++) {
		for (int j = 1; j <= c; j++) {
			if (a[i][j] <= 0) continue;
			int j2 = j + 1;
			while (a[i][j2] == -3) j2++;
			if ((a[i][j2] > 0) && (ans[a[i][j]] == 1)) abort();
			j2 = j - 1;
			while (a[i][j2] == -3) j2--;
			if ((a[i][j2] > 0) && (ans[a[i][j]] == 1)) abort();
		}
	}

}

int main() {
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	ios_base::sync_with_stdio(false); cout.setf(ios::fixed); cout.precision(20);
	int tests;
	cin >> tests;
	for (int i = 1; i <= tests; i++) {
		cout << "Case #" << i << ": ";
		Solve();
	}		
	return 0;	
}