#include <bits/stdc++.h>

using namespace std;

const int maxn = 53;
const int inf = 0x3f3f3f3f;

int n, p, r[maxn], pt[maxn], q[maxn][maxn];

int fuckingMatch(int a, int b) {
	int s(0);
	for (int i = 1; i * r[0] * 9 <= a * 10 && i * r[1] * 9 <= b * 10; ++ i) {
		if (i * r[0] * 11 >= a * 10 && i * r[1] * 11 >= b * 10) {
			++ s;
		}
	}
	return s >= 1;
}

int fuckingSingle(int a) {
	int s(0);
	for (int i = 1; i * r[0] * 9 <= a * 10; ++ i) {
		if (i * r[0] * 11 >= a * 10) {
			++ s;
		}
	}
	return s >= 1;
}

int fm[maxn][maxn];

int sovB() {
	cin >> n >> p;
	for (int i = 0; i < n; ++ i) {
		cin >> r[i];
	}
	for (int i = 0; i < n; ++ i) {
		for (int j = 0; j < p; ++ j) {
			cin >> q[i][j];
		}
		pt[i] = 0;
	}
	int ans(0), pm[maxn], fac(1);
	for (int i = 0; i < p; ++ i) {
		pm[i] = i;
		fac *= i + 1;
	}
	if (n == 2) {
		for (int i = 0; i < p; ++ i) {
			for (int j = 0; j < p; ++ j) {
				fm[i][j] = fuckingMatch(q[0][i], q[1][j]);
			}
		}
		for (int i = 0; i < fac; ++ i) {
			int s(0);
			for (int j = 0; j < p; ++ j) {
				if (fm[j][pm[j]]) {
					++ s;
				}
			}
			ans = max(ans, s);
			next_permutation(pm, pm + p);
		}
	} else if (n == 1) {
		for (int i = 0; i < p; ++ i) {
			if (fuckingSingle(q[0][i])) {
				++ ans;
			}
		}
	}
	return ans;
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++ i) {
		cout << "Case #" << i << ": " << sovB() << endl;
	}
}
