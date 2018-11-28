#include<bits/stdc++.h>
using namespace std;
int n,q;
double E[105],S[105];
double pre[105];
double d[105][105];
int come[105];
int fm[105],to[105];
double dist[105][105];
void floyd()
{
    for(int k=0; k<n; k++)
        for(int i=0; i<n; i++)
            for(int j=0; j<n; j++)
                if(i!=j&&dist[i][j]>dist[i][k]+dist[k][j])
                    dist[i][j]=dist[i][k]+dist[k][j];
}
int main()
{
    double INF=1e15;
    freopen("C-small-attempt2.in","r",stdin);
    freopen("C-small-attempt2.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        scanf("%d%d",&n,&q);
        for(int i=1;i<=n;i++)
            scanf("%lf%lf",&E[i],&S[i]);
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=n;j++)
                scanf("%lf",&d[i][j]);
        }
        for(int i=0;i<q;i++)
        {
            scanf("%d%d",&fm[i],&to[i]);
        }
        memset(pre,0,sizeof(pre));
        for(int i=2;i<=n;i++)pre[i]=pre[i-1]+d[i-1][i];
        memset(dist,0,sizeof(dist));
        for(int i=1;i<=n;i++)
        {
            for(int j=i+1;j<=n;j++)
            {
                if(pre[j]-pre[i]>E[i])dist[i-1][j-1]=INF;
                else dist[i-1][j-1]=(pre[j]-pre[i])/S[i];
            }
        }
        floyd();
        printf("Case #%d: %.10f\n",cas,dist[0][n-1]);
    }
    return 0;
}
/*
10 1
17993 663
9473 277
11790 154
16628 764
17293 125
4683 463
16095 728
16388 907
5354 345
20000 1000
-1 785 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 483 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 3775 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 968 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 8880 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 3788 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 9662 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 8487 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 4504
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
1 10
*/
