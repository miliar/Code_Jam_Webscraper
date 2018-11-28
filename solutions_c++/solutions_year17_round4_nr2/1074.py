#include <cstdio>
#include <algorithm>

using namespace std;

int v[4][1010];

int main()
{
    freopen("file.in","r",stdin);
    freopen("file.out","w",stdout);
    int t,n,c,m,a,b;
    scanf("%d",&t);
    for(int test=1;test<=t;test++)
    {
        scanf("%d%d%d",&n,&c,&m);
        int p=0,sol=0;
        for(int i=1;i<=n;i++) v[1][i]=v[2][i]=0;
        for(int i=1;i<=m;i++)
        {
            scanf("%d%d",&a,&b);
            v[b][a]++;
        }
        for(int i=1;i<=n;i++)
            if(v[1][i]>0 && v[2][i]>0)
            {
                while(v[1][i]>0)
                {
                    int ok=0;
                    for(int j=1;j<=n;j++)
                        if(i!=j && v[1][j]>0 && v[2][j]>0)
                        {
                            ok=1;v[1][i]--;v[2][j]--;sol++;break;
                        }
                    if(ok==0) for(int j=1;j<=n;j++)
                                if(i!=j && v[2][j]>0)
                                {
                                    ok=1;v[1][i]--;v[2][j]--;sol++;break;
                                }
                    if(ok==0) break;
                }
                if(v[1][i]>0)
                while(v[2][i]>0)
                {
                    int ok=0;
                    for(int j=1;j<=n;j++)
                        if(i!=j && v[1][j]>0 && v[2][j]>0)
                        {
                            ok=1;v[2][i]--;v[1][j]--;sol++;break;
                        }
                    if(ok==0) for(int j=1;j<=n;j++)
                                if(i!=j && v[1][j]>0)
                                {
                                    ok=1;v[2][i]--;v[1][j]--;sol++;break;
                                }
                    if(ok==0) break;
                }
            }
        m-=sol*2;a=0;b=0;
        for(int i=1;i<=n;i++)
        {
            if(v[1][i]>0 && v[2][i]>0)
            {
                int x=min(v[1][i],v[2][i]);
                v[1][i]-=x;v[2][i]-=x;
                if(i==1) {sol+=x*2;}
                else {sol+=x;p+=x;}
            }
            a+=v[1][i];
            b+=v[2][i];
        }
        int x=min(a,b);
        sol+=x;
        a-=x;b-=x;
        sol+=a+b;
        printf("Case #%d: %d %d\n",test,sol,p);
    }
    return 0;
}
