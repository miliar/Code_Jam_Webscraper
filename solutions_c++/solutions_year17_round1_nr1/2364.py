#include <bits/stdc++.h>
using namespace std;

int r, c;

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		cout << "Case #" << test << ":\n";
		cin >> r >> c;
		bool used[30];
		string b[30];
		memset(used, false, sizeof(used));
		for (int i = 0; i < r; i++) {
			cin >> b[i];
		}
		for (int j = 0; j < c; j++) {
			for (int i = 0; i < r; i++) if (b[i][j] != '?' && ! used[b[i][j] - 'A']) {
				char ch = b[i][j];
				used[ch-'A'] = true;
				int up = i - 1, down = i + 1, left = j - 1, right = j + 1;
				
				while (up >= 0 && b[up][j] == '?') {
					up--;
				}

				while (down < r && b[down][j] == '?') {
					down++;
				}

				while (left >= 0) {
					bool ok = true;
					for (int k = up + 1; k < down; k++) if (b[k][left] != '?') {
						ok = false;
						break;
					}
					if (!ok) break;
					left--;
				}

				while (right < c) {
					bool ok = true;
					for (int k = up + 1; k < down; k++) if (b[k][right] != '?') {
						ok = false;
						break;
					}
					if (!ok) break;
					right++;
				}

				for (int k = up + 1; k < down; k++)
					for (int l = left + 1; l < right; l++) b[k][l] = ch;
			}
		}
		for (int i = 0; i < r; i++) cout << b[i] << '\n';
	}
	return 0;
}