#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
using namespace std;
string st[110];
string a[110];

int n, m;
inline bool check1(int x, int xx, int y, int yy) {
	for (int i = x; i <= xx; i++) {
		for (int j = y; j <= yy; j++) {
			if (a[i][j] != '?') {
				return false;
			}
		}
	}
	return true;
}
bool can1() {
	set <char> used;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (a[i][j] != '?' && !used.count(a[i][j])) {
				int l = j, r = j;
				used.insert(a[i][j]);
				while (l - 1 >= 0 && a[i][l-1] == '?') {
					l--;
				}
				while (r + 1 < m && a[i][r + 1] == '?') {
					r++;
				}
				int u = i;
				while (u - 1 >= 0 && check1(u - 1, i - 1, l, r)) {
				 u--;
				}
				int d = i;
				while (d + 1 < n && check1(i + 1, d+ 1, l, r)) {
					d++;
				}
				for (int ii = u; ii <= d; ii++) {
					for (int jj = l; jj <= r; jj++ ) {
						a[ii][jj] = a[i][j];
					}
				}
			}
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (a[i][j] == '?') {
				return false;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		cout << a[i] << '\n';
	}
	return true;
}
inline bool can2(){
	return true;
}
inline void solve() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> st[i];
		a[i] = st[i];
	}
	if (can1()) {
		return;
	}
	assert(0);
}
int main() {
	int T;
	scanf("%d", &T);
	for (int test = 1; test <= T; test++) {
		printf("Case #%d:\n", test);
		solve();
	}
}
