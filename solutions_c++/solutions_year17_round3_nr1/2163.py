#include <stdio.h>
#include <math.h>
#include <vector>
#include <algorithm> // sort
#include <map> // pair
using namespace std;
#define PI 3.14159265258979

int main(){
	int T;
	scanf("%d",&T);
	for(int t=0; t<T; t++){
        int N,K;
        scanf("%d%d",&N,&K);
        long long int r[N],h[N];
        for(int i=0; i<N; i++)
            scanf("%lld%lld",&r[i],&h[i]);
        vector<pair<long long int, long long int> > cake;
        for (int i=0; i<N; i++){
            cake.push_back(make_pair(r[i],h[i]));
        }
        sort(cake.begin(),cake.end());
        for (int i=0; i<N; i++){
            r[i] = cake[i].first;
            h[i] = cake[i].second;
        }
        long long int dp[N+1][N+1],dp2[N+1][N+1],maxR[N+1][N+1];
        for (int i=0; i<=N; i++){
            for (int j=0; j<=N; j++){
                dp[i][j] = 0;
                dp2[i][j] = 0;
                maxR[i][j] = 0;
            }
        }
        dp[1][1] = r[0]*r[0]+2*r[0]*h[0];
        dp2[1][1] = 2*r[0]*h[0];
        maxR[1][1] = r[0];
        for (int i=2; i<=N; i++){
            dp[i][i] = dp[i-1][i-1]-r[i-2]*r[i-2]+r[i-1]*r[i-1]+2*r[i-1]*h[i-1];
            dp2[i][i] = dp2[i-1][i-1]+2*r[i-1]*h[i-1];
            maxR[i][i] = r[i-1];
        }
        for (int i=1; i<=N; i++){
            for (int j=1; j<i; j++){
//                if(dp[i-1][j] > dp[i-1][j-1]-maxR[i-1][j-1]*maxR[i-1][j-1]+r[i-1]*r[i-1]+2*r[i-1]*h[i-1]){
                if(dp[i-1][j] > dp2[i-1][j-1]+r[i-1]*r[i-1]+2*r[i-1]*h[i-1]){
                    dp[i][j] = dp[i-1][j];
                    maxR[i][j] = maxR[i-1][j];
                }else{
                    dp[i][j] = dp2[i-1][j-1]+r[i-1]*r[i-1]+2*r[i-1]*h[i-1];
                    maxR[i][j] = r[i-1];
                }
                if(dp2[i-1][j] > 2*r[i-1]*h[i-1]+dp2[i-1][j-1])
                    dp2[i][j] = dp2[i-1][j];
                else
                    dp2[i][j] = 2*r[i-1]*h[i-1]+dp2[i-1][j-1];
            }
        }
        for (int i=0; i<=N; i++){
            for (int j=0; j<=N; j++){
//                printf("%lld,",dp[i][j]);
            }
//            printf("\n");
        }
        double ans=dp[N][K]*M_PI;
		printf("Case #%d: %.7f\n",t+1,ans);
	}
	return 0;
}
