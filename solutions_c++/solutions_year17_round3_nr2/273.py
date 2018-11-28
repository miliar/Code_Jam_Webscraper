#include <bits/stdc++.h>
using namespace std;

const int INF = 1000000000;
const int maxn = 24*60;
int dp[maxn+10][2][730];
bool no[2][maxn+10];

void init_dp() {
	for (int i = 0; i <= maxn; i++)
			for (int j = 0; j <= maxn/2; j++)
				dp[i][0][j] = dp[i][1][j] = INF;
}

int main() {
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T, kase = 0;
	scanf("%d",&T);
	while (T--) {
		memset(no,0,sizeof(no));
		int ac, aj;
		scanf("%d%d",&ac,&aj);
		for (int i = 1; i <= ac; i++) {
			int c, d;
			scanf("%d%d",&c,&d);
			for (int j = c; j < d; j++) no[0][j] = 1;
		}
		for (int i = 1; i <= aj; i++) {
			int c, d;
			scanf("%d%d",&c,&d);
			for (int j = c; j < d; j++) no[1][j] = 1;
		}
		int ans = INF;
		for (int id = 0; id <= 1; id++) {
			if (!no[id][0]) {
				init_dp();
				dp[0][id][0] = 0;
				for (int i = 0; i < maxn; i++) {
					for (int j = 0; j <= 1; j++) {
						for (int k = 0; k <= i; k++) {
							if (!no[j][i+1]) {
								dp[i+1][j][k+1] = min(dp[i+1][j][k+1],dp[i][j][k]);	
							}
							if (!no[1-j][i+1]) {
								dp[i+1][1-j][i-k+1] = min(dp[i+1][1-j][i-k+1],dp[i][j][k]+1);	
							}
						}
					}
				}
				ans = min(ans,dp[maxn][id][720]);
				ans = min(ans,dp[maxn][1-id][720]+1);
			}
		}
		printf("Case #%d: %d\n",++kase,ans);
	}
	return 0;
}
