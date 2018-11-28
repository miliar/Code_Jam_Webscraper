#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

#define SZ(a) (int)(a).size()
typedef long long ll;

const int nil = -1;
int itc;
int n, n2;
vector<bool> vis;
vector<bool> fix0, fix1;
vector<int> mt0, mt1, mt2, mt3;

bool aug0(int u) {
	if (fix0[u] || vis[u]) {
		return false;
	}
	vis[u] = true;
	for (int v = 0; v < n; v++) {
		if (mt1[v] == nil) {
			mt1[v] = u;
			mt0[u] = v;
			return true;
		}
	}
	for (int v = 0; v < n; v++) {
		if (aug0(mt1[v])) {
			mt1[v] = u;
			mt0[u] = v;
			return true;
		}
	}
	return false;
}

void match0() {
	bool chg;
	do {
		chg = false;
		vis.assign(n, false);
		for (int u = 0; u < n; u++) {
			if (mt0[u] == nil && aug0(u)) {
				chg = true;
			}
		}
	} while (chg);
}

bool aug1(int u) {
	if (fix1[u] || vis[u]) {
		return false;
	}
	vis[u] = true;
	int minx = u < n ? 0 : u-n+1;
	int maxx = u < n ? u : n-1;
	int minv = 2*minx-u+n-1;
	int maxv = 2*maxx-u+n-1;
	for (int v = minv; v <= maxv; v += 2) {
		if (mt3[v] == nil) {
			mt3[v] = u;
			mt2[u] = v;
			return true;
		}
	}
	for (int v = minv; v <= maxv; v += 2) {
		if (aug1(mt3[v])) {
			mt3[v] = u;
			mt2[u] = v;
			return true;
		}
	}
	return false;
}

void match1() {
	bool chg;
	do {
		chg = false;
		vis.assign(n2, false);
		for (int u = 0; u < n2; u++) {
			if (mt2[u] == nil && aug1(u)) {
				chg = true;
			}
		}
	} while (chg);
}

void solve() {
	cin >> n;
	n2 = 2*n-1;
	int m;
	cin >> m;
	vector<vector<char>> b(n, vector<char>(n, 0));
	fix0.assign(n, false);
	fix1.assign(n2, false);
	mt0.assign(n, nil);
	mt1.assign(n, nil);
	mt2.assign(n2, nil);
	mt3.assign(n2, nil);
	for (int i = 0; i < m; i++) {
		char c;
		int x, y;
		cin >> c >> x >> y;
		x--; y--;
		if (c != '+') {
			b[x][y] |= 1;
			fix0[x] = true;
			mt0[x] = y;
			mt1[y] = x;
		}
		if (c != 'x') {
			b[x][y] |= 2;
			int u = x+y;
			int v = x-y+n-1;
			fix1[u] = true;
			mt2[u] = v;
			mt3[v] = u;
		}
	}
	match0();
	match1();
	vector<vector<char>> b2(n, vector<char>(n, 0));
	for (int u = 0; u < n; u++) {
		if (mt0[u] != nil) {
			int x = u;
			int y = mt0[u];
			b2[x][y] |= 1;
		}
	}
	for (int u = 0; u < n2; u++) {
		if (mt2[u] != nil) {
			int x = (u+mt2[u]-n+1)/2;
			int y = (u-mt2[u]+n-1)/2;
			b2[x][y] |= 2;
		}
	}
	int score = 0;
	int nchg = 0;
	for (int x = 0; x < n; x++) {
		for (int y = 0; y < n; y++) {
			if (b2[x][y] & 1) {
				score++;
			}
			if (b2[x][y] & 2) {
				score++;
			}
			if (b2[x][y] != b[x][y]) {
				nchg++;
			}
		}
	}
	printf("%d %d\n", score, nchg);
	for (int x = 0; x < n; x++) {
		for (int y = 0; y < n; y++) {
			if (b2[x][y] != b[x][y]) {
				char c;
				switch (b2[x][y]) {
					case 1:
						c = 'x';
						break;
					case 2:
						c = '+';
						break;
					case 3:
						c = 'o';
						break;
				}
				printf("%c %d %d\n", c, x+1, y+1);
			}
		}
	}
}

int main() {
	cin.sync_with_stdio(false);
	int ntc;
	cin >> ntc;
	for (itc = 1; itc <= ntc; itc++) {
		printf("Case #%d: ", itc);
		solve();
	}
}
