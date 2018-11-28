#include <bits/stdc++.h>

using namespace std;

char a[32][32];
int R, C;

void solve() {
	cin >> R >> C;
	for (int i = 0; i < R; i++) 
		cin >> a[i];
	for	(int i = 0; i < R; i++) {
		int l = 0, r = 0;
		while (l < C) {
			while (l < C && a[i][l] != '?') l += 1;
			r = l;
			while (r < C && a[i][r] == '?') r += 1;
			if (l > 0) {
				for (int j = l; j < r; j++)
					a[i][j] = a[i][l-1];
			}else if (r < C) {
				for (int j = l; j < r; j++)
					a[i][j] = a[i][r];
			}
			l = r;
		}
	}

	int l = 0, r = 0;
	while (l < R) {
		while (l < R && a[l][0] != '?') l += 1;
		r = l;
		while (r < R && a[r][0] == '?') r += 1;
		if (l > 0) {
			for (int i = l; i < r; i++)
				for (int j = 0; j < C; j++)
					a[i][j] = a[l-1][j];
		}else if (r < R) {
			for (int i = l; i < r; i++)
				for (int j = 0; j < C; j++)
					a[i][j] = a[r][j];
		}
		l = r;
	}

	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++)
			cout << a[i][j];
		cout << endl;
	}
			
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": " << endl;
		solve();
	}
	return 0;
}

