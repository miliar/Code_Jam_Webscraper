#include <bits/stdc++.h>
using namespace std;
void code() {
	int R, C;
	cin >> R >> C;
	vector<string> M(R);
	for (int i = 0; i < R; i++) {
		cin >> M[i];
	}

	for (int i = 0; i < R; i++) {
		char c = '?';
		for (int j = 0; j < C; j++) {
			if (M[i][j] != '?') {
				c = M[i][j];
			}
			M[i][j] = c;
		}
		c = '?';
		for (int j = C-1; j >= 0; j--) {
			if (M[i][j] != '?') {
				c = M[i][j];
			}
			M[i][j] = c;
		}
		if (M[i][0] == '?' && i != 0) {
			M[i] = M[i-1];
		}
	}
	for (int i = R-1; i >= 0; i--) {
		if (M[i][0] == '?' && i != R-1) {
			M[i] = M[i+1];
		}
	}
	for (int i = 0; i < R; i++) {
		cout << M[i] << endl;
	}
}
int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ":\n";
		code();
	}
}
