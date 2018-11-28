#include <cstdio>
#include <algorithm>

using namespace std;

int P[4];
int DP[111][111][111],Dp[111][111];
int n,p;

int Solve()
{
	int i,j,k,a;

	scanf("%d %d",&n,&p);

	for(i=0;i<p;i++) P[i] = 0;

	for(i=0;i<n;i++){
		scanf("%d",&a);
		P[a%p]++;
	}

	if(p==2) return P[0] + (P[1]+1)/2;
	if(p==3){
		for(i=0;i<=P[1];i++){
			for(j=0;j<=P[2];j++){
				if(i) Dp[i][j] = max(Dp[i][j],Dp[i-1][j]+((i-1+j*2)%3 == 0));
				if(j) Dp[i][j] = max(Dp[i][j],Dp[i][j-1]+((i+j*2-2)%3 == 0));
			}
		}
		return P[0] + Dp[P[1]][P[2]];
	}
	if(p==4){
		for(i=0;i<=P[1];i++){
			for(j=0;j<=P[2];j++){
				for(k=0;k<=P[3];k++){
					if(i) DP[i][j][k] = max(DP[i][j][k],DP[i-1][j][k]+((i-1+j*2+k*3)%4 == 0));
					if(j) DP[i][j][k] = max(DP[i][j][k],DP[i][j-1][k]+((i+j*2-2+k*3)%4 == 0));
					if(k) DP[i][j][k] = max(DP[i][j][k],DP[i][j][k-1]+((i+j*2+k*3-3)%4 == 0));
				}
			}
		}
		return P[0] + DP[P[1]][P[2]][P[3]];
	}
	return 0;
}

int main()
{
	//freopen("output.txt","w",stdout);

	int i,t;

	scanf("%d",&t);

	for(i=1;i<=t;i++){
		printf("Case #%d: %d\n",i,Solve());
	}

	return 0;
}