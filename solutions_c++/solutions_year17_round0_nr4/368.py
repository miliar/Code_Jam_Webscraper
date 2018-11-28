#include <map>
#include <cstdio>
#include <cstring>
#include <iostream>

#define MaxN 110

using namespace std;

int T;

bool matp[MaxN][MaxN], matx[MaxN][MaxN];
char st[MaxN * MaxN][5], inp[MaxN][MaxN];
int x[MaxN * MaxN], y[MaxN * MaxN], n, m;
bool existx[MaxN * 2], existy[MaxN * 2];

int main() {
	scanf("%d", &T);
	int T0 = 0;
	for ( ; T; --T) {
		scanf("%d%d", &n, &m);
		memset(inp, 0, sizeof(inp));
		int ans = 0, anstot = 0;
		for (int i = 0; i < m; ++i) {
			scanf("%s%d%d", st[i], &x[i], &y[i]);
			if (st[i][0] == 'o') {
				ans += 2;
			}
			else {
				ans += 1;
			}
			inp[x[i] - 1][y[i] - 1] = st[i][0];
		}
		memset(existx, 0, sizeof(existx));
		memset(existy, 0, sizeof(existy));
		memset(matp, 0, sizeof(matp));
		memset(matx, 0, sizeof(matx));
		for (int i = 0; i < m; ++i) {
			if (st[i][0] == 'o' || st[i][0] == 'x') {
				existx[x[i] - 1] = 1;
				existy[y[i] - 1] = 1;
				matx[x[i] - 1][y[i] - 1] = 1;
			}
		}
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (existx[i] == 0 && existy[j] == 0) {
					existx[i] = existy[j] = 1;
					matx[i][j] = 1;
					++ans;
				}
			}
		}
		memset(existx, 0, sizeof(existx));
		memset(existy, 0, sizeof(existy));
		for (int i = 0; i < m; ++i) {
			if (st[i][0] == 'o' || st[i][0] == '+') {
				existx[x[i] - 1 + y[i] - 1] = 1;
				existy[x[i] - y[i] + n] = 1;
				matp[x[i] - 1][y[i] - 1] = 1;
			}
		}
		for (int k = 0; k < n; ++k) {
			for (int i = 0; i < n; ++i) {
				for (int j = 0; j < n; ++j) {
					if (i + j == k || i - j == n - 1 - k || j - i == n - 1 - k || i + j == 2 * n - 2 - k) {
						int nx = i + j, ny = i - j + n;
						if (existx[nx] == 0 && existy[ny] == 0) {
							existx[nx] = existy[ny] = 1;
							matp[i][j] = 1;
							++ans;
						}
					}
				}
			}
		}
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				char outc = 0;
				if (matx[i][j] == 1 && matp[i][j] == 0) {
					outc = 'x';
					//printf("x %d %d\n", i + 1, j + 1);
				}
				if (matx[i][j] == 0 && matp[i][j] == 1) {
					outc = '+';
					//printf("+ %d %d\n", i + 1, j + 1);
				}
				if (matx[i][j] == 1 && matp[i][j] == 1) {
					outc = 'o';
					//printf("o %d %d\n", i + 1, j + 1);
				}
				if (outc != inp[i][j]) {
					++anstot;
				}
			}
		}
		printf("Case #%d: %d %d\n", ++T0, ans, anstot);
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				char outc = 0;
				if (matx[i][j] == 1 && matp[i][j] == 0) {
					outc = 'x';
					//printf("x %d %d\n", i + 1, j + 1);
				}
				if (matx[i][j] == 0 && matp[i][j] == 1) {
					outc = '+';
					//printf("+ %d %d\n", i + 1, j + 1);
				}
				if (matx[i][j] == 1 && matp[i][j] == 1) {
					outc = 'o';
					//printf("o %d %d\n", i + 1, j + 1);
				}
				if (outc != inp[i][j]) {
					++anstot;
					printf("%c %d %d\n", outc, i + 1, j + 1);
				}
			}
		}
	}
}