#include <cstdio>
#include <algorithm>

using namespace std;

const int INF=1e9;

char vaz1[2000],vaz2[2000];
int d1[1000][1000],d2[1000][1000];

int solve(char vaz1[],char vaz2[])
{
    for(int i=0;i<=720;i++)
        for(int j=0;j<=720;j++) d1[i][j]=d2[i][j]=INF;
    if(vaz1[1]==1) return INF;
    d1[0][0]=0;
    for(int i=1;i<=720;i++)
        for(int j=0;j<=720;j++)
        {
            if(vaz1[i+j]==0) d1[i][j]=min(d1[i-1][j],d2[i-1][j]+1);
            if(j>0 && vaz2[i+j]==0) d2[i][j]=min(d2[i][j-1],d1[i][j-1]+1);
        }
    return min(d1[720][720],d2[720][720]+1);
}

int main()
{
    freopen("file.in","r",stdin);
    freopen("file.out","w",stdout);
    int t,ac,aj,x,y;
    scanf("%d",&t);
    for(int test=1;test<=t;test++)
    {
        scanf("%d%d",&ac,&aj);
        for(int i=0;i<=1440;i++) vaz1[i]=vaz2[i]=0;
        for(int i=1;i<=ac;i++)
        {
            scanf("%d%d",&x,&y);
            for(int j=x+1;j<=y;j++) vaz1[j]=1;
        }
        for(int i=1;i<=aj;i++)
        {
            scanf("%d%d",&x,&y);
            for(int j=x+1;j<=y;j++) vaz2[j]=1;
        }
        int sol=min(solve(vaz1,vaz2),solve(vaz2,vaz1));
        printf("Case #%d: %d\n",test,sol);
    }
    return 0;
}
