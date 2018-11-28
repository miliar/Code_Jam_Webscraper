#include <iostream> 
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

int f[105][105][105];
int S[5];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		int n, P;
		scanf("%d %d", &n, &P);
		memset(S, 0, sizeof(S));
		for (int i = 1; i <= n; ++i) {
			int x;
			scanf("%d", &x);
			++S[x % P];
		}
		for (int i = 0; i <= S[1]; ++i) {
			for (int j = 0; j <= S[2]; ++j) {
				for (int k = 0; k <= S[3]; ++k) {
					f[i][j][k] = 0;
					if (i > 0) f[i][j][k] = max(f[i][j][k], f[i - 1][j][k]);
					if (j > 0) f[i][j][k] = max(f[i][j][k], f[i][j - 1][k]);
					if (k > 0) f[i][j][k] = max(f[i][j][k], f[i][j][k - 1]);
					f[i][j][k] += ((i * 1 + j * 2 + k * 3) % P == 0) ? 1 : 0;
				}
			}
		}
		int ans = f[S[1]][S[2]][S[3]] + S[0];
		if ((S[1] * 1 + S[2] * 2 + S[3] * 3) % P == 0) --ans;
		printf("Case #%d: %d\n", cas, ans);
	}
}
