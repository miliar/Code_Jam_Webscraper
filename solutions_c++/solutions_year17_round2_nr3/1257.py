#include <iostream>
#include<cstdio>
#include<cstring>
using namespace std;
long long mat[105][105];
long long E[105],S[105];
int QU[105],QV[105];
double dp[105];
int main()
{
    freopen("data.out","w",stdout);
    int T,N,Q;
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++)
    {
        scanf("%d%d",&N,&Q);
        for(int i=1;i<=N;i++){
            scanf("%lld%lld",&E[i],&S[i]);
        }
        for(int i=1;i<=N;i++)
            for(int j=1;j<=N;j++){
                scanf("%lld",&mat[i][j]);
                if(mat[i][j]==-1) mat[i][j]=INT_MAX;
            }
        for(int i=1;i<=Q;i++){
            scanf("%d%d",&QU[i],&QV[i]);
        }
        for(int i=1;i<=N;i++)
            for(int j=1;j<=N;j++)
                for(int k=1;k<=N;k++)
                    mat[i][j]=min(mat[i][j],mat[i][k]+mat[k][j]);
        for(int i=1;i<=N;i++) dp[i]=(1LL<<40);
        dp[1]=0;
        for(int i=1;i<=N;i++){
            for(int j=i+1;j<=N;j++){
                if(mat[i][j]>E[i]) break;
                dp[j]=min(dp[j],dp[i]+1.0*mat[i][j]/S[i]);
            }
        }
        printf("Case #%d: %.10lf\n",kase,dp[N]);
        /*
        for(int i=1;i<=N;i++,printf("\n"))
            for(int j=1;j<=N;j++)
                printf("%d ",mat[i][j]);
        */
    }
    return 0;
}
