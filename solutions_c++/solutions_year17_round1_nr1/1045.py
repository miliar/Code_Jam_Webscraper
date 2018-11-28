#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;

int t, r, c;
char s[30][30];
char ans[30][30];

void solve() {
	int n, m, u, d;
	bool flag;
	//printf("%d %d", r, c);
	for (int i = 0;i < r;++i)
		for (int j = 0;j < c;++j)
			ans[i][j] = s[i][j];
	// for (int ii = 0;ii < r;++ii) {
	// 		for (int jj = 0;jj < c;++jj)
	// 			printf("%c", ans[ii][jj]);
	// 		printf("\n");
	// 	}
	// return;
	for (int i = 0;i < r;++i)
		for (int j = 0;j < c;++j)
			if (s[i][j] != '?') {
				n = j;
				m = j;
				while (n > 0 && ans[i][n - 1] == '?') --n;
				while (m < c - 1 && ans[i][m + 1] == '?') ++m;
				u = d = i;
				while (u > 0) {
					flag = true;
					for (int w = n;w <= m;++w)
						if (ans[u - 1][w] != '?') {
							flag = false;
							break;
						}
					if (flag) --u;
					else break;
				}
				while (d < r - 1) {
					flag = true;
					for (int w = n;w <= m;++w)
						if (ans[d + 1][w] != '?') {
							flag = false;
							break;
						}
					if (flag) ++d;
					else break;
				}
				for (int w = u;w <= d;++w)
					for (int p = n;p <= m;++p)
						ans[w][p] = s[i][j];
			}
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d%*c", &t);
	for (int i = 1;i <= t;++i) {
		scanf("%d%d%*c", &r, &c);
		for (int ii = 0;ii < r;++ii) {
			for (int jj = 0;jj < c;++jj) 
				scanf("%c", &s[ii][jj]);
			scanf("%*c");
		}
		solve();
		printf("Case #%d:\n", i);
		for (int ii = 0;ii < r;++ii) {
			for (int jj = 0;jj < c;++jj)
				printf("%c", ans[ii][jj]);
			printf("\n");
		}
	}

	return 0;
}