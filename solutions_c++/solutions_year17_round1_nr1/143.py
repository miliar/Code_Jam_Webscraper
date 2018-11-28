#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 30;

char grid[MAX_N][MAX_N];
int n, m;

void input() {
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++) {
		scanf("%s", grid[i]);
	}
}

bool all_same(int u, int d, int l, int r) {
	for (int i = u; i <= d; i++) {
		for (int j = l; j <= r; j++) {
			if (grid[i][j] != '?') {
				return false;
			}
		}
	}
	return true;
}

void fill_it(int u, int d, int l, int r) {
	for (int i = l; i < r; i++) {
		if (all_same(u, d, l, i) || all_same(u, d, i + 1, r)) {
			continue;
		}
		fill_it(u, d, l, i);
		fill_it(u, d, i + 1, r);
		return;
	}
	for (int i = u; i < d; i++) {
		if (all_same(u, i, l, r) || all_same(i + 1, d, l, r)) {
			continue;
		}
		fill_it(u, i, l, r);
		fill_it(i + 1, d, l, r);
		return;
	}
	char x;
	for (int i = u; i <= d; i++) {
		for (int j = l; j <= r; j++) {
			if (grid[i][j] != '?') {
				x = grid[i][j];
			}
		}
	}
	for (int i = u; i <= d; i++) {
		for (int j = l; j <= r; j++) {
			grid[i][j] = x;
		}
	}
}

int main()
{
	int t;
	scanf("%d", &t);
	int case_num = 0;
	while (t--)
	{
		case_num++;
		printf("Case #%d:\n", case_num);
		input();
		fill_it(0, n - 1, 0, m - 1);
		for (int i = 0; i < n; i++) {
			puts(grid[i]);
		}
	}
	return 0;
}
