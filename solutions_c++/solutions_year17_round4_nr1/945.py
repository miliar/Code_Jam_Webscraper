#include <cstdio>
#include <cstdlib>
#include <algorithm>

const int MAXN = 107;
const int INF = 1e9;

int a[7];
int f[103][103][103][4];

int main() {
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; ++Case) {
		int n, p;
		scanf("%d%d", &n, &p);
		for (int i = 0; i < 4; ++i)
			a[i] = 0;
		for (int i = 0; i < n; ++i) {
			int k;
			scanf("%d", &k);
			++a[k % p];
		}

		for (int i = 0; i <= a[1]; ++i)
			for (int j = 0; j <= a[2]; ++j)
				for (int k = 0; k <= a[3]; ++k)
					for (int l = 0; l < p; ++l)
						f[i][j][k][l] = -INF;
		f[0][0][0][(p - (a[1] + 2 * a[2] + 3 * a[3]) % p) % p] = a[0];
		for (int i = 0; i <= a[1]; ++i)
			for (int j = 0; j <= a[2]; ++j)
				for (int k = 0; k <= a[3]; ++k)
					for (int l = 0; l < p; ++l) {
						if (f[i][j][k][l] < 0) continue;
						if (i < a[1])
							f[i + 1][j][k][(l + 1) % p] = std::max(f[i + 1][j][k][(l + 1) % p], f[i][j][k][l] + ((l + 1) % p == 0));
						if (j < a[2])
							f[i][j + 1][k][(l + 2) % p] = std::max(f[i][j + 1][k][(l + 2) % p], f[i][j][k][l] + ((l + 2) % p == 0));
						if (k < a[3])
							f[i][j][k + 1][(l + 3) % p] = std::max(f[i][j][k + 1][(l + 3) % p], f[i][j][k][l] + ((l + 3) % p == 0));
					}
		printf("Case #%d: %d\n", Case, f[a[1]][a[2]][a[3]][0]);
	}
	return 0;
}
