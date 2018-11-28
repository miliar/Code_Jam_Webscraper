#include <bits/stdc++.h>
using namespace std;
const int maxn = 2000;
int test, n, n1, n2;
int f[maxn][725][2];
bool fr[2][maxn];

void xl()
{
        for (int i=1;i<=1440;++i)
            for (int j=0;j<=720;++j)
            {
                if (fr[0][i]) f[i][j][0] = 1e9;
                else
                {
                    f[i][j][0]=1e9;
                    if (j>0 && i-j<=720) f[i][j][0]=min(f[i][j][0],f[i-1][j-1][0]);
                    if (j>0 && i-j<=720) f[i][j][0]=min(f[i][j][0],f[i-1][j-1][1] + 1);
                }
                if (fr[1][i]) f[i][j][1]=1e9;
                else
                {
                    f[i][j][1]=1e9;
                    if (i-1 >= j)
                    {
                        if (i-j<=720) f[i][j][1]=min(f[i][j][1],f[i-1][j][0] + 1);
                        if (i-j<=720) f[i][j][1]=min(f[i][j][1],f[i-1][j][1]);
                    }
                }
            }
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d", &test);
    for (int t=1;t<=test;++t)
    {
        memset(fr,false,sizeof(fr));
        scanf("%d%d",&n1,&n2);
        for (int i=1;i<=n1;++i)
        {
            int u,v;
            scanf("%d%d",&u,&v);
            for (int j=u+1;j<=v;++j) fr[0][j]=true;
        }
        for (int i=1;i<=n2;++i)
        {
            int u,v;
            scanf("%d%d",&u,&v);
            for (int j=u+1;j<=v;++j) fr[1][j]=true;
        }
        int ans=1e9;
        f[0][0][0] = 0; f[0][0][1]=1e9;
        xl();
        ans=min(ans,f[1440][720][0]);
        ans=min(ans,f[1440][720][1] + 1);
        f[0][0][0] = 1e9; f[0][0][1]=0;
        xl();
        ans=min(ans,f[1440][720][0]+1);
        ans=min(ans,f[1440][720][1]);
        cout<< "Case #"<<t<<": "<<ans<<"\n";
    }
    return 0;
}
