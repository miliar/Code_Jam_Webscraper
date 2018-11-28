#include <bits/stdc++.h>

#define rep(i, n) for(int i = 0; i < n; i ++)
const int N = 30;
char mat[N][N];

int main() {
	int R, C, T;
	scanf("%d", &T);
	rep(cas, T) {
		scanf("%d%d", &R, &C);
		rep(i, R) {
			scanf("%s", mat[i]);
			char pre = '?';
			rep(j, C) {
				if (pre != '?') {
					if (mat[i][j] == '?') {
						mat[i][j] = pre;
					}
				}
				pre = mat[i][j];
			}
			pre = '?';
			for (int j = C - 1; ~j; j --) {
				if (pre != '?') {
					if (mat[i][j] == '?') {
						mat[i][j] = pre;
					}
				}
				pre = mat[i][j];
			}
		}
		rep(j, C) {
			char pre = '?';
			rep(i, R) {
				if (pre != '?') {
					if (mat[i][j] == '?') {
						mat[i][j] = pre;
					}
				}
				pre = mat[i][j];
			}
			pre = '?';
			for (int i = R - 1; ~i; i --) {
				if (pre != '?') {
					if (mat[i][j] == '?') {
						mat[i][j] = pre;
					}
				}
				pre = mat[i][j];
			}
		}
		printf("Case #%d:\n", cas + 1);
		rep(i, R) {
			printf("%s\n", mat[i]);
		}
	}

	return 0;
}
