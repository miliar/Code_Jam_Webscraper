#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;

#define MAXN 105
int E[MAXN],S[MAXN],D[MAXN][MAXN];
double mat[MAXN][MAXN];
int st[MAXN],ed[MAXN];
int mark[MAXN];
double dis[MAXN][MAXN];

void calcMat(int n)
{
    for(int i=1;i<=n;++i)
    {
//        memset(mark,0,sizeof(mark));
        queue<pair<int,int>> qu;
        qu.push({i,E[i]});
//        mark[i]=1;
        mat[i][i]=0;
        while(!qu.empty())
        {
            int curi=qu.front().first,cure=qu.front().second;
            qu.pop();
            for(int j=1;j<=n;++j)
                if(~D[curi][j]&&cure>=D[curi][j]&&mat[i][j]>mat[i][curi]+double(D[curi][j])/S[i])
            {
                mat[i][j]=mat[i][curi]+double(D[curi][j])/S[i];
//                mark[j]=1;
                qu.push({j,cure-D[curi][j]});
            }
        }
    }
}

//double spfa(int n,int st,int ed)
//{
//    for(int i=1;i<=n;++i)
//        dis[st][i]=1e12;
//    dis[st][st]=0;
//    queue<int> qu;
//    qu.push(st);
//    while(!qu.empty())
//    {
//        int cur=qu.front();qu.pop();
//        for(int i=1;i<=n;i++)
//        {
//            if(cur!=i&&dis[st][i]>)
//        }
//    }
//}

int main()
{
    ios::sync_with_stdio(false);
    int T,N;
    int cas=0;
    cin >>T;
    while(T--)
    {
        int Q;
        printf("Case #%d:",++cas);
        cin >> N >> Q;
        for(int i=1;i<=N;++i)
            cin >> E[i] >> S[i];
        for(int i=1;i<=N;++i)
            for(int j=1;j<=N;++j)
                cin >> D[i][j];
        for(int i=1;i<=Q;++i)
            cin >> st[i] >> ed[i];
        for(int i=1;i<=N;++i)
            for(int j=1;j<=N;++j)
                mat[i][j]=1e20;
        calcMat(N);

        for(int k=1;k<=N;++k)
            for(int i=1;i<=N;++i)
                for(int j=1;j<=N;++j)
                    if(mat[i][j]>mat[i][k]+mat[k][j])
                        mat[i][j]=mat[i][k]+mat[k][j];
        for(int i=1;i<=Q;i++)
        {
            printf(" %f",mat[st[i]][ed[i]]);
        }
        printf("\n");
    }
    return 0;
}

