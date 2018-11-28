#include <bits/stdc++.h>
using namespace std;
int T, n, p, a;
int f[120][120][120];
int lo[5];
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for(int i=1; i<=T; i++) {
		memset(lo, 0, sizeof lo);
		memset(f, 0, sizeof f);
		scanf("%d%d", &n, &p);
		for(int i=0; i<n; i++) {
			scanf("%d", &a);
			lo[a % p]++;
		}
		f[0][0][0] = lo[0];
		for(int i=0; i<=lo[1]; i++) {
			for(int j=0; j<=lo[2]; j++) {
				for(int k=0; k<=lo[3]; k++) {
					if (i>0)
					f[i][j][k] = max(f[i][j][k], f[i-1][j][k] + (((i-1) + j*2 + k*3) % p == 0));
					if (j>0)
					f[i][j][k] = max(f[i][j][k], f[i][j-1][k] + ((i + (j-1)*2 + k*3) % p == 0));
					if (k>0)
					f[i][j][k] = max(f[i][j][k], f[i][j][k-1] + ((i + j*2 + (k-1)*3) % p == 0));
					//printf("f[%d][%d][%d]=%d\n", i,j,k, f[i][j][k]);
				}
			}
		}
		printf("Case #%d: %d\n", i, f[lo[1]][lo[2]][lo[3]]);
	}
}
