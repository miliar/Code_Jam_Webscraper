#include<bits/stdc++.h>
using namespace std;
#define mx 109
int dist[mx][mx];
int src[mx],spd[mx];
int cdist[mx][mx];
int n;
double dp[mx][mx];
double func(int i, int j)
{
    if(i==n-1)
        return 0.0;
    else if(dp[i][j]>-0.5){
        return dp[i][j];
    }
    dp[i][j]=10e28;
    if(cdist[j][i]+dist[i][i+1]<=src[j]){
        dp[i][j]=(dist[i][i+1]+0.0)/spd[j]+func(i+1,j);
    }
    if(src[i]>=dist[i][i+1])
        dp[i][j]=min(dp[i][j],(dist[i][i+1]+0.0)/spd[i]+func(i+1,i));
    return dp[i][j];
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("a.out","w",stdout);

    int t,cs=1,q,s,d,i,j;
    double r,ln;
    scanf("%d",&t);
    while(t--){
        scanf("%d %d",&n,&q);
        for(i=0;i<n;i++)
            scanf("%d %d",&src[i],&spd[i]);
        for(i=0;i<n;i++){
            for(j=0;j<n;j++){
                scanf("%d",&dist[i][j]);
            }
        }
        for(i=0;i<n-1;i++){
            cdist[i][i]=0;
            for(j=i+1;j<n;j++){
                cdist[i][j]=cdist[i][j-1]+dist[j-1][j];
            }
        }
        scanf("%d %d",&s,&d);
        printf("Case #%d:",cs++);
        for(i=0;i<n;i++){
            for(j=0;j<n;j++)
                dp[i][j]=-1.0;
        }
        r=func(0,0);
        printf(" %.8lf\n",r+10e-12);
    }
    return 0;
}
