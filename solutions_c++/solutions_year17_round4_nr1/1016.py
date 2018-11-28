#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <map>
#include <utility>
#include <vector>
#include <ctime>
#include <queue>
#include <set>
#include <cmath>
#include <iostream>
#include <string>

using namespace std;

const int maxp = 4;
const int maxn = 105;

int dp[2][maxn][maxn][maxn][maxp];
int n, mod;

void solve(int tst) {
	// printf("heyn\n");
	scanf("%d%d", &n, &mod);
	int tmp[4] = {0,0,0,0};
	// printf("hi\n");
	for (int i = 1; i <= n; i ++) {
		int g;
		scanf("%d", &g);
		tmp[g % mod] ++;
	}
	//printf("n=%d,mod=%d\n",n,mod);
	memset(dp, 0, sizeof dp);
	for (int sum = 0; sum <= n; sum ++) {
		// reset current
		memset(dp[sum&1], 0, sizeof dp[sum&1]);
		for (int a0 = 0; a0 <= sum; a0 ++)
			for (int a1 = 0; a0 + a1 <= sum; a1 ++) 
				for (int a2 = 0; a0 + a1 + a2 <= sum; a2 ++) 
					for (int m = 0; m < mod; m ++) {
						int a3 = sum - a0 - a1 - a2;
						// printf("dp[%d,%d,%d,%d,%d]=%d\n", a0,a1,a2,a3,m,
							// dp[sum&1][a0][a1][a2][m]);

						int arr[4] = {a0, a1, a2, a3};
						for (int k = 0; k < mod; k ++) {
							int pure = 1;
							if (m != 0) pure = 0;
							int nextm = (m + k) % mod;
							arr[k] --;

							if (arr[k] >= 0) dp[sum&1][a0][a1][a2][m] = max(dp[sum&1][a0][a1][a2][m], 
								dp[(sum+1)&1][arr[0]][arr[1]][arr[2]][nextm] + pure);
							arr[k] ++;
						}

				}
	}
	int ans = dp[n&1][tmp[0]][tmp[1]][tmp[2]][0];
	printf("Case #%d: %d\n", tst, ans);
}

int main() {
    int tst;
    // printf("1\n");
    scanf("%d", &tst);
    for (int t = 1; t <= tst; t ++) {
        solve(t);
    }
    return 0;
}
