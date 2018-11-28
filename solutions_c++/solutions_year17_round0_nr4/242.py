#include <cstdio>
#include <vector>
#include <cstring>
#include <bitset>

using namespace std;

const int adun=101;
vector<int> g[300];
int cup1[300],cup2[300],sol[110][110],init[110][110];
char vazd1[300],vazd2[300],vazl[300],vazc[300];
bitset<300> vaz;

int cupleaza(int nod)
{
    if(vaz[nod]) return 0;
    vaz[nod]=1;
    for(vector<int>::iterator it=g[nod].begin();it!=g[nod].end();it++)
        if(!cup2[*it] || cupleaza(cup2[*it]))
        {
            cup1[nod]=*it;
            cup2[*it]=nod;
            return 1;
        }
    return 0;
}

int main()
{
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);
    int test;
    scanf("%d",&test);
    for(int t=1;t<=test;t++)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        memset(vazd1,0,sizeof(vazd1));
        memset(vazd2,0,sizeof(vazd2));
        memset(vazl,0,sizeof(vazl));
        memset(vazc,0,sizeof(vazc));
        memset(cup1,0,sizeof(cup1));
        memset(cup2,0,sizeof(cup2));
        memset(sol,0,sizeof(sol));
        memset(init,0,sizeof(init));
        for(int i=0;i<=2*n;i++)
            g[i].clear();
        for(int i=1;i<=m;i++)
        {
            char c;
            int x,y;
            scanf("\n%c%d%d",&c,&x,&y);
            if(c=='+' || c=='o') vazd1[x+y]=vazd2[x-y+adun]=1, sol[x][y]|=1, init[x][y]|=1;
            if(c=='x' || c=='o') vazl[x]=vazc[y]=1, sol[x][y]|=2, init[x][y]|=2;
        }
        vector<int> lin,col;
        for(int i=1;i<=n;i++)
        {
            if(!vazl[i]) lin.push_back(i);
            if(!vazc[i]) col.push_back(i);
        }
        for(int i=0;i<lin.size();i++)
            sol[lin[i]][col[i]]|=2;
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++)
                if(!vazd1[i+j] && !vazd2[i-j+adun])
                    g[i+j].push_back(i-j+adun);
        int ok=1;
        while(ok)
        {
            ok=0;
            vaz&=0;
            for(int i=1;i<=2*n;i++)
                if(!cup1[i]) ok|=cupleaza(i);
        }
        for(int i=1;i<=2*n;i++)
            if(cup1[i])
            {
                int x=(i+cup1[i]-adun)/2,y=(i-cup1[i]+adun)/2;
                sol[x][y]|=1;
            }
        int sum=0,nr=0;
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++)
            {
                if(sol[i][j]==1 || sol[i][j]==2) sum++;
                if(sol[i][j]==3) sum+=2;
                if(sol[i][j]!=init[i][j]) nr++;
            }
        printf("Case #%d: %d %d\n",t,sum,nr);
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++)
                if(sol[i][j]!=init[i][j])
                {
                    if(sol[i][j]==1) printf("+ %d %d\n",i,j);
                    else if(sol[i][j]==2) printf("x %d %d\n",i,j);
                    else printf("o %d %d\n",i,j);
                }
    }
    return 0;
}
