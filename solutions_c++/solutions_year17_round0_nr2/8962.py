#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long ll;
char buf[32];
int n;
ll dp[32][10][2];
ll pow10[32];

int main() {
	pow10[0] = 1;
	for (int i = 1; i < 32; ++ i) {
		pow10[i] = pow10[i - 1] * 10;
	}
	int T;
	scanf("%d", &T);
	for (int kase = 1; kase <= T; ++ kase) {
		scanf("%s", buf);
		n = strlen(buf);
		memset(dp, -1, sizeof(dp));
		dp[0][0][1] = 0;
		for (int i = 0; i < n; ++ i) {
			for (int j = 0; j <= 9; ++ j) {
				for (int k = 0; k < 2; ++ k) if (dp[i][j][k] != -1) {
					int low = j;
					int up = (k == 1 ? (buf[i] - '0') : 9);
					for (int l = low; l <= up; ++ l) {
						dp[i + 1][l][(k == 1) && (l == up)] = max(dp[i + 1][l][(k == 1) && (l == up)], dp[i][j][k] + pow10[n - i - 1] * l);
					}
				}
			}
		}
		ll res = 0;
		for (int j = 0; j <= 9; ++ j) res = max(res, max(dp[n][j][0], dp[n][j][1]));
		printf("Case #%d: %lld\n", kase, res);
	}
	return 0;
}
