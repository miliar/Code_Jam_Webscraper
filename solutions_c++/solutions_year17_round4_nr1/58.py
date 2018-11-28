#include<bits/stdc++.h>
using namespace std;
const int N(105);
int dp[N][N], f[N][N][N], cnt[N];
int main() {
	int tests;
	scanf("%d", &tests);
	for(int qq(1); qq <= tests; qq++) {
		int n, p;
		scanf("%d%d", &n, &p);
		fill(cnt, cnt + p, 0);
		for(int i(1); i <= n; i++) {
			int x;
			scanf("%d", &x);
			cnt[x % p]++;
		}
		int ans;
		if(p == 2) {
			ans = cnt[0] + (cnt[1] + 1) / 2;
		}else if(p == 3) {
			for(int i(0); i <= cnt[1]; i++)
				for(int j(0); j <= cnt[2]; j++)
					dp[i][j] = 0;
			for(int i(0); i <= cnt[1]; i++) {
				for(int j(0); j <= cnt[2]; j++) {
					if(i < cnt[1])
						dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + ((i + j * 2) % 3 == 0));
					if(j < cnt[2])
						dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + ((i + j * 2) % 3 == 0));
					
				}
			}
			ans = dp[cnt[1]][cnt[2]] + cnt[0];
		}else {
			for(int i(0); i <= cnt[1]; i++)
				for(int j(0); j <= cnt[2]; j++)
					for(int k(0); k <= cnt[3]; k++)
						f[i][j][k] = 0;
			for(int i(0); i <= cnt[1]; i++) {
				for(int j(0); j <= cnt[2]; j++) {
					for(int k(0); k <= cnt[3]; k++) {
						if(i < cnt[1])
							f[i + 1][j][k] = max(f[i + 1][j][k], f[i][j][k] + ((i + j * 2 + k * 3) % 4 == 0));
						if(j < cnt[2])
							f[i][j + 1][k] = max(f[i][j + 1][k], f[i][j][k] + ((i + j * 2 + k * 3) % 4 == 0));
						if(k < cnt[3])
							f[i][j][k + 1] = max(f[i][j][k + 1], f[i][j][k] + ((i + j * 2 + k * 3) % 4 == 0));
					}
				}
			}
			ans = f[cnt[1]][cnt[2]][cnt[3]] + cnt[0];
		}
		printf("Case #%d: %d\n", qq, ans);
	}
}
