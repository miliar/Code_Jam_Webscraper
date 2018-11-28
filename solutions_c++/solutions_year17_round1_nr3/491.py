#include <stdio.h>
#include <string.h>
#include <math.h>
#include <queue>
#include <utility>
#include <map>
#include <set>

using namespace std;

const int INF = 500;

int hd, ad, hk, ak, B, D;
int f[2][101][101][101];
int now, old, res;

void csh() {
	int i, j, k;
	for (i = 1; i <= hd; ++i)
		for (j = ad; j <= 100; ++j)
			for (k = 0; k <= ak; ++k)
				f[now][i][j][k] = INF;
}

void init() {
	scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &B, &D);
	now = 0;
	csh();
	f[now][hd][ad][ak] = hk;
}

void work() {
	int round;
	int i, j, k, nj, nk;
	res = -1;
	for (round = 1; round <= (hd + hk) * 2 && round <= 210; ++round) {
		old = now;
		now = 1 - now;
		csh();
		for (i = 1; i <= hd; ++i)
			for (j = ad; j <= 100; ++j)
				for (k = 0; k <= ak; ++k) {
					if (f[old][i][j][k] == INF) continue;					
					// attack
					if (f[old][i][j][k] <= j) {
						res = round;
						return;
					}
					if (i > k && f[old][i][j][k] - j < f[now][i-k][j][k]) f[now][i-k][j][k] = f[old][i][j][k] - j;

					// buff
					nj = j + B;
					if (nj > 100) nj = 100;
					if (i > k && f[old][i][j][k] < f[now][i - k][nj][k]) f[now][i - k][nj][k] = f[old][i][j][k];

					// cure
					if (hd > k && f[old][i][j][k] < f[now][hd - k][j][k]) f[now][hd - k][j][k] = f[old][i][j][k];

					// debuff
					nk = k - D;
					if (nk < 0) nk = 0;
					if (i > nk && f[old][i][j][k] < f[now][i - nk][j][nk]) f[now][i - nk][j][nk] = f[old][i][j][k];
				}
	}
}

void output() {
	if (res == -1) printf("IMPOSSIBLE\n");
	else printf("%d\n", res);
}

int main() {
	int T, t;
	freopen("C.in", "r", stdin);
	FILE *fout = fopen("C.out", "w");
	scanf("%d", &T);
	for (t = 1; t <= T; ++t)
	{
		fprintf(fout, "Case #%d: ", t);
		printf("Case #%d: ", t);
		init();
		work();
		if (res == -1) fprintf(fout, "IMPOSSIBLE\n");
		else fprintf(fout, "%d\n", res);
		if (res == -1) printf("IMPOSSIBLE\n");
		else printf("%d\n", res);
	}
	fclose(fout);

	return 0;
}