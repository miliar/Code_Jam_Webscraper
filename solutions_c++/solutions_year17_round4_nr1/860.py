#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef pair<int , int> P2;
typedef pair<pair<int , int> , int> P3;
typedef pair<pair<int , int> , pair<int , int> > P4;
#define PB(a) push_back(a)
#define MP(a , b) make_pair((a) , (b))
#define M3P(a , b , c) make_pair(make_pair((a) , (b)) , (c))
#define M4P(a , b , c , d) make_pair(make_pair((a) , (b)) , make_pair((c) , (d)))
#define repp(i,a,b) for(int i = (int)(a) ; i < (int)(b) ; ++i)
#define repm(i,a,b) for(int i = (int)(a) ; i > (int)(b) ; --i)

int T;
int N,P;
int G[4];
int dp[102][102][102];

int solve(){
	if(P==2) return (G[1]+1)/2;
	repp(i,0,G[1]+1){
		repp(j,0,G[2]+1){
			repp(k,0,G[3]+1){
				dp[i][j][k] = -1;
			}
		}
	}
	dp[G[1]][G[2]][G[3]] = 0;
	repm(i,G[1],-1){
		repm(j,G[2],-1){
			repm(k,G[3],-1){
				if(P==3){
					if(i>=3) dp[i-3][j][k] = max(dp[i-3][j][k],dp[i][j][k]+1);
					if(i>=1&&j>=1) dp[i-1][j-1][k] = max(dp[i-1][j-1][k],dp[i][j][k]+1);
					if(j>=3) dp[i][j-3][k] = max(dp[i][j-3][k],dp[i][j][k]+1);
				} else {
					if(i>=4) dp[i-4][j][k] = max(dp[i-4][j][k],dp[i][j][k]+1);
					if(i>=2&&j>=1) dp[i-2][j-1][k] = max(dp[i-2][j-1][k],dp[i][j][k]+1);
					if(i>=1&&k>=1) dp[i-1][j][k-1] = max(dp[i-1][j][k-1],dp[i][j][k]+1);
					if(j>=2) dp[i][j-2][k] = max(dp[i][j-2][k],dp[i][j][k]+1);
					if(j>=1&&k>=2) dp[i][j-1][k-2] = max(dp[i][j-1][k-2],dp[i][j][k]+1);
					if(k>=4) dp[i][j][k-4] = max(dp[i][j][k-4],dp[i][j][k]+1);
				}
				if(i+j+k>0) ++dp[i][j][k];
				dp[0][0][0] = max(dp[i][j][k],dp[0][0][0]);
			}
		}
	}
	return dp[0][0][0];
}

int main(){
	scanf("%d" , &T);
	repp(tt,0,T){
		printf("Case #%d: " , tt + 1);
		scanf("%d%d" , &N , &P);
		repp(i,0,4) G[i] = 0;
		repp(i,0,N){
			int x;
			scanf("%d" , &x);
			++G[x%P];
		}
		printf("%d\n" , G[0] + solve());
	}
	return 0;
}
