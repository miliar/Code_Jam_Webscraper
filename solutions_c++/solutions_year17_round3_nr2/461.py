#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <vector>
#include <queue>

#define MEM(a,x) memset(a,x,sizeof a)
#define eps 1e-8
#define MOD 10009
#define MAXN 10010
#define MAXM 100010
#define INF 99999999
#define ll long long
#define bug cout<<"here"<<endl
#define fread freopen("B-large.in","r",stdin)
#define fwrite freopen("out.txt","w",stdout)

using namespace std;

const int mx=24*60;

int a[mx+10];
int f[mx+10][mx/2+10][5][5];

int main()
{
//    fread;
//    fwrite;
    int tc;
    cin>>tc;
    for(int t=1;t<=tc;t++)
    {
        int n,m;
        cin>>n>>m;
        for(int i=0;i<mx;i++)
            a[i]=-1;
        for(int i=1;i<=n;i++)
        {
            int x,y;
            cin>>x>>y;
            for(int j=x;j<y;j++)
                a[j%mx]=1;
        }
        for(int i=1;i<=m;i++)
        {
            int x,y;
            cin>>x>>y;
            for(int j=x;j<y;j++)
                a[j%mx]=0;
        }
        for(int i=0;i<mx;i++)
            for(int j=0;j<=mx/2;j++)
                for(int k=0;k<4;k++)
                    f[i][j][k/2][k%2]=2*mx;
        f[0][0][0][0]=0;
        f[0][1][1][1]=0;
        for(int i=1;i<mx;i++)
            for(int j=0;j<=mx/2;j++)
                for(int k=0;k<2;k++)
                {
                    for(int l=0;l<2;l++)
                    {
                        if(a[i]==-1||a[i]==0)
                            f[i][j][0][k]=min(f[i][j][0][k],f[i-1][j][l][k]+(l!=0));
                        if(j!=0)
                            if(a[i]==-1||a[i]==1)
                                f[i][j][1][k]=min(f[i][j][1][k],f[i-1][j-1][l][k]+(l!=1));
                    }
                }
        int ans=2*mx;
        for(int i=0;i<2;i++)
            for(int j=0;j<2;j++)
                ans=min(ans,f[mx-1][mx/2][i][j]+(i!=j));
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
