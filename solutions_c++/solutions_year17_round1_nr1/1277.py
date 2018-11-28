#include <bits/stdc++.h>

using namespace std;

const int maxn = 27;

char a[maxn][maxn], b[maxn][maxn];
int n, m;

int check(int u, int d, int l, int r) {
	if (u < 0 || d >= n || l < 0 || r >= m) {
		return 0;
	}
	int s(0);
	for (int i = u; i <= d; ++ i) {
		for (int j = l; j <= r; ++ j) {
			if (a[i][j] != '?') {
				++ s;
			}
		}
	}
	return s == 1;
}

void grow(int xo, int yo) {
	int u(xo), d(xo), l(yo), r(yo);
	for (; check(u - 1, d, l, r); -- u);
	for (; check(u, d, l - 1, r); -- l);
	for (; check(u, d, l, r + 1); ++ r);
	for (; check(u, d + 1, l, r); ++ d);
	for (int i = u; i <= d; ++ i) {
		for (int j = l; j <= r; ++ j) {
			a[i][j] = a[xo][yo];
		}
	}
}

void sovA() {
	cin >> n >> m;
	for (int i = 0; i < n; ++ i) {
		cin >> a[i];
		strcpy(b[i], a[i]);
	}
	for (int i = 0; i < n; ++ i) {
		for (int j = 0; j < m; ++ j) {
			if (b[i][j] != '?') {
				grow(i, j);
			}
		}
	}
	for (int i = 0; i < n; ++ i) {
		cout << a[i] << endl;
	}
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++ i) {
		cout << "Case #" << i << ": " << endl;
		sovA();
	}
}
