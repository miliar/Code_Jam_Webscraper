#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 105, MAXP = 4;
int N, P, G[MAXN], c[MAXP], f3[MAXN][MAXN], f4[MAXN][MAXN][MAXN];

void DP() {
	for (int i = 0; i < MAXN; ++i) {
		for (int j = 0; j < MAXN; ++j) {
			if (0 == i && 0 == j) f3[i][j] = 0;
			else {
				f3[i][j] = 0;
				if (i) f3[i][j] = max(f3[i][j], f3[i - 1][j] + (((i - 1) + j * 2) % 3 == 0));
				if (j) f3[i][j] = max(f3[i][j], f3[i][j - 1] + ((i + (j - 1) * 2) % 3 == 0));
			}
		}
	}
	for (int i = 0; i < MAXN; ++i) {
		for (int j = 0; j < MAXN; ++j) {
			for (int k = 0; k < MAXN; ++k) {
				if (0 == i && 0 == j && 0 == k) f4[i][j][k] = 0;
				else {
					f4[i][j][k] = 0;
					if (i) f4[i][j][k] = max(f4[i][j][k], f4[i - 1][j][k] + (((i - 1) + j * 2 + k * 3) % 4 == 0));
					if (j) f4[i][j][k] = max(f4[i][j][k], f4[i][j - 1][k] + ((i + (j - 1) * 2 + k * 3) % 4 == 0));
					if (k) f4[i][j][k] = max(f4[i][j][k], f4[i][j][k - 1] + ((i + j * 2 + (k - 1) * 3) % 4 == 0));
				}
			}
		}
	}
}

int main() {
	int T, g;
	scanf("%d", &T);
	DP();
	for (int t = 1; t <= T; ++t) {
		scanf("%d%d", &N, &P);
		for (int i = 0; i < P; ++i) c[i] = 0;
		for (int i = 0; i < N; ++i) scanf("%d", &g), ++c[g % P];
		printf("Case #%d: ", t);
		if (P == 2) printf("%d\n", c[0] + (c[1] + 1) / 2);
		else if (P == 3) printf("%d\n", c[0] + f3[c[1]][c[2]]);
		else printf("%d\n", c[0] + f4[c[1]][c[2]][c[3]]);
	}
	return 0;
}
