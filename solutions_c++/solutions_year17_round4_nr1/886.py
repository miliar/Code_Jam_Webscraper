#include<bits/stdc++.h>
using namespace std;
int mod[4];
int dp[101][101][101][4];
int main(){
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		int n,p;
		scanf("%d %d", &n, &p);
		mod[0] = mod[1] = mod[2] = mod[3] = 0;
		for(int j=0;j<n;j++){
			int su;
			scanf("%d", &su);
			mod[su%p]++;
		}
		printf("Case #%d: ", i);
		for(int j=0;j<=mod[1];j++){
			for(int k=0;k<=mod[2];k++){
				for(int l=0;l<=mod[3];l++){
					for(int m=0;m<4;m++) dp[j][k][l][m] = 0;
				}
			}
		}
		for(int j=0;j<=mod[1];j++){
			for(int k=0;k<=mod[2];k++){
				for(int l=0;l<=mod[3];l++){
					for(int m=0;m<p;m++){
						if(j>0){
							dp[j][k][l][m] = max(dp[j][k][l][m], dp[j-1][k][l][(m+((2*p)-1))%p] + (m == (1%p)));
						}
						if(k>0){
							dp[j][k][l][m] = max(dp[j][k][l][m], dp[j][k-1][l][(m+((2*p)-2))%p] + (m == (2%p)));
						}
						if(l>0){
							dp[j][k][l][m] = max(dp[j][k][l][m], dp[j][k][l-1][(m+((2*p)-3))%p] + (m == (3%p)));
						}
					}
				}
			}
		}
		int ans = 0;
		for(int m=0;m<p;m++){
			ans = max(ans, dp[mod[1]][mod[2]][mod[3]][m]);
		}
		printf("%d\n", ans + mod[0]);
	}
}
