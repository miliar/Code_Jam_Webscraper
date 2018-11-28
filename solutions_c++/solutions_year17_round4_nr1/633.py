#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <cstdlib>
#include <queue>
#include <map>
#include <stack>
#define maxn 109
#define maxm 100000
using namespace std;
int n, P;
int cnt[10];
int dp[maxn][maxn][maxn];
int f[maxn][maxn];
int main(){
	freopen("/Users/fengweiming/ProgramContest/GoogleCodeJam2017/Round2/A.in", "r", stdin);
	freopen("/Users/fengweiming/ProgramContest/GoogleCodeJam2017/Round2/A.out", "w", stdout);
	int tt, cot = 1;
	scanf("%d", &tt);
	while(tt--){
		cin >> n >> P;
		memset(cnt, 0, sizeof(cnt));
		for(int i = 1; i <= n ;i++){
			int x;
			cin >> x;
			cnt[x % P]++;
		}
		int ans = 0 ;
		if(P == 2){
			ans = cnt[0] + (cnt[1] + 1) / 2;
		}
		else if(P == 3){
			memset(f, 0, sizeof(f));
			f[0][0] = 0;
			for(int i = 0; i <= cnt[1]; i++){
				for(int j = 0; j <= cnt[2]; j++){
					if(i > 0){
						int sum = (i - 1) * 1 + j * 2;
						sum %= P;
						if(sum == 0)
							f[i][j] = max(f[i][j], f[i - 1][j] + 1);
						else
							f[i][j]= max(f[i][j], f[i - 1][j]);
					}
					if(j > 0){
						int sum = i * 1 + (j - 1) * 2;
						sum %= P;
						if(sum == 0)
							f[i][j] = max(f[i][j],f[i][j - 1] + 1);
						else
							f[i][j]= max(f[i][j], f[i][j - 1]);
					}
				}
			}
			ans = f[cnt[1]][cnt[2]] + cnt[0];
		}
		else{
			memset(dp, 0, sizeof(dp));
			dp[0][0][0] = 0;
			for(int i = 0; i <= cnt[1]; i++){
				for(int j = 0; j <= cnt[2]; j++){
					for(int k = 0; k <= cnt[3]; k++){
						int sum = 0;
						if(i > 0){
							sum = (i - 1) * 1 + j * 2 + k * 3;
							sum %= P;
							if(sum == 0)
								dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k] + 1);
							else
								dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k]);
						}
						if(j > 0){
							sum = i * 1 + (j - 1) * 2 + k * 3;
							sum %= P;
							if(sum == 0)
								dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k] + 1);
							else
								dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k]);
						}
						if(k > 0){
							sum = i * 1 + j * 2 + (k - 1)* 3;
							sum %= P;
							if(sum == 0)
								dp[i][j][k] = max(dp[i][j][k], dp[i][j][k - 1] + 1);
							else
								dp[i][j][k] = max(dp[i][j][k], dp[i][j][k - 1]);
						}
					}
				}
			}
			ans = dp[cnt[1]][cnt[2]][cnt[3]] + cnt[0];
		}
		printf("Case #%d: %d\n", cot++, ans);
	}
	return 0;
}