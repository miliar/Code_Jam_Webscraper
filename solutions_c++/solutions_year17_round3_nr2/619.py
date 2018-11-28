#include<cmath>
#include<cstdio>
#include<string>
#include<cstring>
#include<algorithm>
using namespace std;
int f[2001][2001][2];
struct acti
{
    int s,t;
}a1[101],a2[101];
inline bool cmp(acti x,acti y)
{
    return x.s<y.s;
}
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B1.out", "w", stdout);
    int T,kk=0;
    scanf("%d",&T);
    while(T>0)
    {
        T--;
        kk++;
        int n1,n2;
        scanf("%d%d",&n1,&n2);
        int i,j,k;
        for(i=1;i<=n1;i++)
            scanf("%d%d",&a1[i].s,&a1[i].t);
        for(i=1;i<=n2;i++)
            scanf("%d%d",&a2[i].s,&a2[i].t);
        n1++;
        a1[n1].s=a1[n1].t=1441;
        n2++;
        a2[n2].s=a2[n2].t=1441;
        sort(a1+1,a1+1+n1,cmp);
        sort(a2+1,a2+1+n2,cmp);
        memset(f,127/3,sizeof(f));
        int ans=2100000;
        if(a1[1].s!=0)
            f[0][0][0]=0;
        //if(a2[1].s!=0)
        //	f[0][0][1]=0;
        int d1=1,d2=1;
        for(i=1;i<=1440;i++)
        {
            while(i>=a1[d1].t)
                d1++;
            while(i>=a2[d2].t)
                d2++;
            for(j=0;j<=i;j++)
            {
                if(i<a1[d1].s)
                {
                    f[i][j][0]=f[i-1][j][1]+1;
                    if(j>0)
                        f[i][j][0]=min(f[i][j][0],f[i-1][j-1][0]);
                }
                if(i<a2[d2].s)
                {
                    f[i][j][1]=f[i-1][j][1];
                    if(j>0)
                        f[i][j][1]=min(f[i][j][1],f[i-1][j-1][0]+1);
                }
            }
        }
        ans=min(f[1440][720][0],f[1440][720][1]+1);
        
        memset(f,127/3,sizeof(f));
        if(a2[1].s!=0)
            f[0][0][1]=0;
        d1=1;
        d2=1;
        for(i=1;i<=1440;i++)
        {
            while(i>=a1[d1].t)
                d1++;
            while(i>=a2[d2].t)
                d2++;
            for(j=0;j<=i;j++)
            {
                if(i<a1[d1].s)
                {
                    f[i][j][0]=f[i-1][j][1]+1;
                    if(j>0)
                        f[i][j][0]=min(f[i][j][0],f[i-1][j-1][0]);
                }
                if(i<a2[d2].s)
                {
                    f[i][j][1]=f[i-1][j][1];
                    if(j>0)
                        f[i][j][1]=min(f[i][j][1],f[i-1][j-1][0]+1);
                }
            }
        }
        ans=min(ans,min(f[1440][720][0]+1,f[1440][720][1]));
        printf("Case #%d: %d\n",kk,ans);
    }
    return 0;
}
