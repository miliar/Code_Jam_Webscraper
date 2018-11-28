/*AMETHYSTS*/
#pragma comment(linker, "/STACK:1000000000")
#include <cstdio>
#include <iostream>
#include <ctime>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <set>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <bitset>
#include <deque>
#include <stack>
#include <climits>
#include <string>
#include <queue>
#include <memory.h>
#include <map>            
#define ll long long
#define ld double
#define mp make_pair

using namespace std;

const double PI = 3.14159265358979323846;
const int maxn = (int)401;
const int maxlog = (int)13;
const ll mod = (ll)1e9 + 7;
const ll inf = (ll)1e9 + 7;
const ld eps = 1e-7;

int n, m, l[maxn], r[maxn], u[maxn], d[maxn], s[maxn][maxn], s1[maxn][maxn], was[maxn];
char a[maxn][maxn];
int t;

void fill(int b1, int a1, int b2, int a2, int c) {
	for (int i = a1; i <= a2; i++) {
		for (int j = b1; j <= b2; j++) {
			a[i][j] = c + 'A';
		}
	}
	return;
}

int getsum(int a1, int b, int ro) {
	int tans = 0;
	for (int i = a1; i <= b; i++) {
		if (a[ro][i] == '?') {
			tans++;
		}
	}
	return tans;
}

int getsum1(int a1, int b, int c) {
	int tans = 0;
	for (int i = a1; i <= b; i++) {
		if (a[i][c] == '?') {
			tans++;
		}
	}
	return tans;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> t;
	for (int ii = 0; ii < t; ii++) {
		cin >> n >> m;
		memset(l, -1, sizeof l);
		memset(r, -1, sizeof r);
		memset(u, -1, sizeof u);
		memset(d, -1, sizeof d);
		memset(was, 0, sizeof was);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cin >> a[i][j];
				if (a[i][j] == '?') {
					continue;
				}
				int c = a[i][j] - 'A';
				u[c] = (u[c] == -1 ? i : min(u[c], i));
				d[c] = (d[c] == -1 ? i : max(d[c], i));
				l[c] = (l[c] == -1 ? j : min(l[c], j));
				r[c] = (r[c] == -1 ? j : max(r[c], j));
			}
		}
		for (int c = 0; c < 26; c++) {
			if (l[c] == -1) {
				continue;
			}
			for (int i = u[c]; i <= d[c]; i++) {
				for (int j = l[c]; j <= r[c]; j++) {
					a[i][j] = c + 'A';
				}
			}
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (a[i][j] == '?') {
					continue;
				}
				int c = a[i][j] - 'A';
				if (was[c] || l[c] == -1) {
					continue;
				}
				was[c] = 1;
				while (u[c] > 0 && getsum(l[c], r[c], u[c] - 1) == r[c] - l[c] + 1) {
					fill(l[c], u[c] - 1, r[c], u[c] - 1, c);
					u[c]--;
				}
				while (r[c] < m - 1 && getsum1(u[c], d[c], r[c] + 1) == d[c] - u[c] + 1) {
					fill(r[c] + 1, u[c], r[c] + 1, d[c], c);
					r[c]++;
				}
				while (l[c] > 0 && getsum1(u[c], d[c], l[c] - 1) == d[c] - u[c] + 1) {
					fill(l[c] - 1, u[c], l[c] - 1, d[c], c);
					l[c]--;
				}
				while (d[c] < n - 1 && getsum(l[c], r[c], d[c] + 1) == r[c] - l[c] + 1) {
					fill(l[c], d[c] + 1, r[c], d[c] + 1, c);
					d[c]++;
				}
			}
		}
		printf("Case #%d:\n", ii + 1);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cout << a[i][j];
			}
			cout << endl;
		}
	}
	return 0;
}