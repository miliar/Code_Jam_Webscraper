#include <cstdio>

int N,P,T;
int dp[103][103][103][3];
int INF=1000000007;
int main() {
	scanf("%d",&T);
	for(int cases=1;cases<=T;cases++) {
		scanf("%d%d",&N,&P);
		int r[4];
		for(int i=0;i<4;i++) r[i]=0;
		for(int i=0;i<N;i++) {
			int vl;
			scanf("%d",&vl);
			r[vl%P]++;
		}
		for(int i=0;i<=r[1];i++) for(int j=0;j<=r[2];j++) for(int k=0;k<=r[3];k++) for(int l=0;l<3;l++) {
			dp[i][j][k][l]=-INF;
		}
		dp[r[1]][r[2]][r[3]][0]=r[0];
		for(int i=r[1];i>=0;i--) for(int j=r[2];j>=0;j--) for(int k=r[3];k>=0;k--) for(int l=0;l<3;l++) {
			if(l) {
				if(i) if(dp[i-1][j][k][(l+1)%P]<dp[i][j][k][l]) dp[i-1][j][k][(l+1)%P]=dp[i][j][k][l];
				if(j) if(dp[i][j-1][k][(l+2)%P]<dp[i][j][k][l]) dp[i][j-1][k][(l+2)%P]=dp[i][j][k][l];
				if(k) if(dp[i][j][k-1][(l+3)%P]<dp[i][j][k][l]) dp[i][j][k-1][(l+3)%P]=dp[i][j][k][l];
			} else {
				if(i) if(dp[i-1][j][k][(l+1)%P]<dp[i][j][k][l]+1) dp[i-1][j][k][(l+1)%P]=dp[i][j][k][l]+1;
				if(j) if(dp[i][j-1][k][(l+2)%P]<dp[i][j][k][l]+1) dp[i][j-1][k][(l+2)%P]=dp[i][j][k][l]+1;
				if(k) if(dp[i][j][k-1][(l+3)%P]<dp[i][j][k][l]+1) dp[i][j][k-1][(l+3)%P]=dp[i][j][k][l]+1;
			}
		}
		int sol=0;
		for(int l=0;l<3;l++) if(sol<dp[0][0][0][l]) sol=dp[0][0][0][l];
		printf("Case #%d: %d\n",cases,sol);
	}
	return 0;
}
