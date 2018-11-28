#include <bits/stdc++.h>

using namespace std;

char a[30][30];
int r, c;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int nTests;
	scanf("%d", &nTests);
	for (int test = 1; test <= nTests; ++test) {
		scanf("%d %d", &r, &c);
		for (int i = 0; i < r; ++i)
			scanf(" %s", a[i]);
		for (int i = 0; i < r; ++i)
			for (int j = 0; j < c; ++j) 
				if (a[i][j] != '?') {
					for (int jj = j+1; jj < c && a[i][jj] == '?'; ++jj)
						a[i][jj] = a[i][j];
					for (int jj = j-1; jj >= 0 && a[i][jj] == '?'; --jj)
						a[i][jj] = a[i][j];
				}
		for (int i = 1; i < r; ++i)
			for (int j = 0; j < c; ++j)
				if (a[i][j] == '?')
					a[i][j] = a[i-1][j];
		for (int i = r-2; i >= 0; --i)
			for (int j = 0; j < c; ++j)
				if (a[i][j] == '?')
					a[i][j] = a[i+1][j];
		printf("Case #%d:\n", test);
		for (int i = 0; i < r; ++i) 
			puts(a[i]);
	}
	return 0;
}