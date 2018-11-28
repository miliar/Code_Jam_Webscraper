#include <bits/stdc++.h>
using namespace std;

int T, n, m;
char grid[30][30];

int main() {
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++) scanf("%s", grid[i]);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (grid[i][j] == '?' && j > 0) grid[i][j] = grid[i][j - 1]; 
			}
			for (int j = m - 1; j >= 0; j--) {
				if (grid[i][j] == '?' && j + 1 < m) grid[i][j] = grid[i][j + 1];
			}
		}
		for (int i = 0; i < n; i++) {
			if (grid[i][0] == '?' && i > 0) {
				for (int j = 0; j < m; j++) grid[i][j] = grid[i - 1][j];
			}
		}
		for (int i = n - 1; i >= 0; i--) {
			if (grid[i][0] == '?' && i + 1 < n) {
				for (int j = 0; j < m; j++) grid[i][j] = grid[i + 1][j];
			}
		}
//		printf("Case #%d: \n", tc + 1);
		cout << "Case #" << tc + 1 << ":" << endl;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) putchar(grid[i][j]);
			putchar('\n');
		}
	}
	return 0;
}