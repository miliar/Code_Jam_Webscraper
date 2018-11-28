#include <bits/stdc++.h>

using namespace std;

const int N = 27;

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	
	for (int test = 1; test <= t; ++test) {
		int r, c;
		char grid[N][N];
		scanf("%d %d\n", &r, &c);
		for (int i = 0; i < r; ++i)
			scanf(" %s", grid[i]);
		
		for (int i = 0; i < r; ++i) {
			char prev = '?';
			for (int j = 0; j < c; ++j) {
				if (grid[i][j] == '?' && prev != '?') {
					grid[i][j] = prev;
				} else {
					prev = grid[i][j];
				}
			}
			prev = '?';
			for (int j = c - 1; j >= 0; --j) {
				if (grid[i][j] == '?' && prev != '?') {
					grid[i][j] = prev;
				} else {
					prev = grid[i][j];
				}
			}
		}
		for (int j = 0; j < c; ++j) {
			char prev = '?';
			for (int i = 0; i < r; ++i) {
				if (grid[i][j] == '?' && prev != '?') {
					grid[i][j] = prev;
				} else {
					prev = grid[i][j];
				}
			}
			prev = '?';
			for (int i = r - 1; i >= 0; --i) {
				if (grid[i][j] == '?' && prev != '?') {
					grid[i][j] = prev;
				} else {
					prev = grid[i][j];
				}
			}
		}
		printf("Case #%d:\n", test);
		for (int i = 0; i < r; ++i)
			printf("%s\n", grid[i]);
	}
	return 0;
}