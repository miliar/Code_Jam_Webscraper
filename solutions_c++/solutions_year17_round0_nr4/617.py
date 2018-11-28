#include <bits/stdc++.h>

using namespace std;

const int MX = 100;

char f[MX];

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int n, m;
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; i++) f[i] = 0;
		for (int i = 0; i < m; i++) {
			char c;
			int row, col;
			scanf(" %c %d %d", &c, &row, &col);
			assert(row == 1);
			
			f[col - 1] = c;
		}
		
		vector<tuple<char, int, int>> changes;
		int o = -1, ans = n + 1, x = -1;
		for (int i = 0; i < n; i++) {
			if (f[i] == 'o') {
				o = i;
			}
			else if (f[i] == 'x' || (i == n - 1 && o == -1)) {
				f[i] = 'o';
				o = i;
				changes.emplace_back('o', 0, i);
			}
			else if (f[i] == 0) {
				f[i] = '+';
				changes.emplace_back('+', 0, i);
			}
		}
		
		if (o != 0) x = 0;
		if (o != n - 1) x = n - 1;
		
		if (x != -1) {
			ans++;
			changes.emplace_back('x', n - 1, x);
		}
		
		for (int i = 1, j = 0; i < n - 1; i++) {
			ans++;
			changes.emplace_back('+', n - 1, i);
			
			while (j == o || j == x) j++;
			
			ans++;
			changes.emplace_back('x', i, j);
			j++;
		}
		
		printf("Case #%d: %d %d\n", t, ans, (int)changes.size());
		for (auto& ch : changes) {
			char c;
			int row, col;
			tie(c, row, col) = ch;
			printf("%c %d %d\n", c, row + 1, col + 1);
		}
	}
	
	return 0;
}
