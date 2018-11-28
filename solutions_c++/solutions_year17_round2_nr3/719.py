#include <bits/stdc++.h>

using namespace std;

double timeG[105][105];
const long long INF = 1e18;
struct Horse
{
    int len,speed;
} horses[105];
long long G[105][105];
long long minDis[105][105];
double minTime[105][105];

int main()
{
    freopen("out.txt","w+",stdout);
    int T,N,Q;
    scanf("%d",&T);
    for(int caseNum = 1;caseNum <= T;caseNum++)
    {
        scanf("%d%d",&N,&Q);

        for(int i = 1;i <= N;i++)
        {
            for(int j = 1;j <= N;j++)
                timeG[i][j] = INF,G[i][j] = INF;
        }

        for(int i = 1;i <= N;i++)
            scanf("%d%d",&horses[i].len,&horses[i].speed);
        int temp;
        for(int i = 1;i <= N;i++)
        {
            for(int j = 1;j <= N;j++)
            {
                scanf("%d",&temp);
                if(temp != -1)
                    G[i][j] = temp;
            }
        }

        memcpy(minDis,G,sizeof(G));
        for(int i = 1;i <= N;i++)
        {
            for(int j = 1;j <= N;j++)
            {
                for(int k = 1;k <= N;k++)
                    minDis[j][k] = min(minDis[j][k],minDis[j][i] + minDis[i][k]);
            }
        }

        for(int i = 1;i <= N;i++)
        {
            for(int j = 1;j <= N;j++)
            {
                if(minDis[i][j] <= horses[i].len)
                    timeG[i][j] = minDis[i][j] / (double)horses[i].speed;
            }
        }

        memcpy(minTime,timeG,sizeof(timeG));
        for(int i = 1;i <= N;i++)
        {
            for(int j = 1;j <= N;j++)
            {
                for(int k = 1;k <= N;k++)
                    minTime[j][k] = min(minTime[j][k],minTime[j][i] + minTime[i][k]);
            }
        }

        printf("Case #%d:",caseNum);
        for(int i = 1;i <= Q;i++)
        {
            int u,v;
            scanf("%d%d",&u,&v);
            printf(" %.7f",minTime[u][v]);
        }
        putchar('\n');

    }
    return 0;
}
