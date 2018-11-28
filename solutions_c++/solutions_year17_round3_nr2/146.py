#include <bits/stdc++.h>

using namespace std;

const int INF = 1e9;

int t,i,j,n,m,k,ppl[1500],dp[800][800][2][2];


//0 = ppl1 1 = ppl2;

int main(){
	scanf("%d", &t);
	int tc = 0;
	while(t--){
		tc++;
		
		scanf("%d%d", &n, &m);
		
		memset(ppl, 0, sizeof(ppl));
		
		for(i = 0; i < n; i++){
			int x,y;
			scanf("%d%d", &x, &y);
			for(j = x; j < y; j++)
			ppl[j] = 1;
		}
		
		for(i = 0; i < m; i++){		
			int x,y;
			scanf("%d%d", &x, &y);
			for(j = x; j < y; j++)
			ppl[j] = 2;
		}
		
		for(i = 0; i <= 720; i++){
			for(j = 0; j <= 720; j++){
				dp[i][j][0][0] = INF;
				dp[i][j][1][0] = INF;
				dp[i][j][0][1] = INF;
				dp[i][j][1][1] = INF;
			}
		}
		
		dp[0][0][0][0] = 0;
		dp[0][0][1][1] = 0;
		
		for(i = 0; i <= 720; i++){
			for(j = 0; j <= 720; j++){
				if(ppl[i + j] == 2 || ppl[i + j] == 0){
					dp[i + 1][j][0][0] = min(dp[i + 1][j][0][0], dp[i][j][0][0]);
					dp[i + 1][j][0][0] = min(dp[i + 1][j][0][0], dp[i][j][1][0] + 1);
					dp[i + 1][j][0][1] = min(dp[i + 1][j][0][1], dp[i][j][0][1]);
					dp[i + 1][j][0][1] = min(dp[i + 1][j][0][1], dp[i][j][1][1] + 1);
				}
				if(ppl[i + j] == 1 || ppl[i + j] == 0){
					dp[i][j + 1][1][0] = min(dp[i][j + 1][1][0], dp[i][j][0][0] + 1);
					dp[i][j + 1][1][0] = min(dp[i][j + 1][1][0], dp[i][j][1][0]);
					dp[i][j + 1][1][1] = min(dp[i][j + 1][1][1], dp[i][j][0][1] + 1);
					dp[i][j + 1][1][1] = min(dp[i][j + 1][1][1], dp[i][j][1][1]);
					
				}
			}
		}
		
		int res = min(dp[720][720][0][0], dp[720][720][0][1] + 1);
		int res1 = min(dp[720][720][1][0] + 1, dp[720][720][1][1]);
		
		printf("Case #%d: %d\n", tc, min(res, res1));
	}
}
