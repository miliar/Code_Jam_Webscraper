#include <bits/stdc++.h>
using namespace std;
#define MAXN 1500
#define N 1440
#define MAXA 109
#define INF (1<<30)
#define s first
#define t second

int T, Ac, Aj;
typedef pair<int, int> ii;
ii vc[MAXA], vj[MAXA];

int dp[2][2][MAXN][MAXN];

int DP(int i, int j, int k, int t) {
	if (dp[i][j][k][t] >= 0) return dp[i][j][k][t];
	if (k == N){
		if (t != N/2) return dp[i][j][k][t] = INF;
		return dp[i][j][k][t] = (i == j ? 0 : 1);
	}
	if (j == 1) {
		for(int it=0; it<Ac; it++) {
			if (vc[it].t >= k && k > vc[it].s) return dp[i][j][k][t] = INF;
		}
	}
	else {
		for(int it=0; it<Aj; it++) {
			if (vj[it].t >= k && k > vj[it].s) return dp[i][j][k][t] = INF;
		}
	}
	return dp[i][j][k][t] = min(DP(i, j, k+1, (j==0?t+1:t)), 1+DP(i, 1-j, k+1, (j==1?t+1:t)));
}

int main(){
	scanf("%d", &T);
	for(int caseNo = 1; caseNo <= T; caseNo++) {
		scanf("%d %d", &Ac, &Aj);
		for(int i=0; i<2; i++){
			for(int j=0; j<2; j++){
				for(int k=0; k<=N; k++){
					for(int t=0; t<=N; t++){
						dp[i][j][k][t] = -1;
					}
				}
			}
		}
		for(int i=0; i<Ac; i++){
			scanf("%d %d", &vc[i].s, &vc[i].t);
		}
		for(int i=0; i<Aj; i++){
			scanf("%d %d", &vj[i].s, &vj[i].t);
		}
		printf("Case #%d: %d\n", caseNo, min(DP(0,0,0,0), DP(1,1,0,0)));
	}
	return 0;
}