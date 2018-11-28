#include <bits/stdc++.h>
using ll = long long;
using ld = long double;
using namespace std;


int n, p;

int a[4];

const int MAXN = 101;
int f4[MAXN][MAXN][MAXN][MAXN];
int f3[MAXN][MAXN][MAXN];
int f2[MAXN][MAXN];

void Solve2() {
	memset(f2, 0, sizeof(f2));
	for (int i = 0; i <= a[0]; i++) {
		for (int j = 0; j <= a[1]; j++) {
			if ((i == a[0]) && (j == a[1])) continue;
			if ((i * 0 + j * 1) % p == 0)
				f2[i][j]++;
			f2[i + 1][j] = max(f2[i + 1][j], f2[i][j]);
			f2[i][j + 1] = max(f2[i][j + 1], f2[i][j]);
		}
	}
	cout << f2[a[0]][a[1]] << "\n";
}

void Solve3() {
	memset(f3, 0, sizeof(f3));
	for (int i = 0; i <= a[0]; i++) {
		for (int j = 0; j <= a[1]; j++) {
			for (int l = 0; l <= a[2]; l++) {
				if ((i == a[0]) && (j == a[1]) && (l == a[2])) continue;
				if ((i * 0 + j * 1 + l * 2) % p == 0)
					f3[i][j][l]++;
				f3[i + 1][j][l] = max(f3[i + 1][j][l], f3[i][j][l]);
				f3[i][j + 1][l] = max(f3[i][j + 1][l], f3[i][j][l]);
				f3[i][j][l + 1] = max(f3[i][j][l + 1], f3[i][j][l]);
			}
		}
	}
	cout << f3[a[0]][a[1]][a[2]] << "\n";
}

void Solve4() {
	memset(f4, 0, sizeof(f4));
	for (int i = 0; i <= a[0]; i++) {
		for (int j = 0; j <= a[1]; j++) {
			for (int l = 0; l <= a[2]; l++) {
				for (int k = 0; k <= a[3]; k++) {
					if ((i == a[0]) && (j == a[1]) && (l == a[2]) && (k == a[3])) continue;
					if ((i * 0 + j * 1 + l * 2 + k * 3) % p == 0)
						f4[i][j][l][k]++;
					f4[i + 1][j][l][k] = max(f4[i + 1][j][l][k], f4[i][j][l][k]);
					f4[i][j + 1][l][k] = max(f4[i][j + 1][l][k], f4[i][j][l][k]);
					f4[i][j][l + 1][k] = max(f4[i][j][l + 1][k], f4[i][j][l][k]);
					f4[i][j][l][k + 1] = max(f4[i][j][l][k + 1], f4[i][j][l][k]);
				}
			}
		}
	}
	cout << f4[a[0]][a[1]][a[2]][a[3]] << "\n";
}

void Solve() {
	memset(a, 0, sizeof(a));
	cin >> n >> p;
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		a[x % p]++;
	}
	if (p == 2) Solve2();
	if (p == 3) Solve3();
	if (p == 4) Solve4();
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