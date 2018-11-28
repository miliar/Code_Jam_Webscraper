#include<bits/stdc++.h>

using namespace std;
int f[2][24*70][2][2];
int v[24*70];
struct node{int l,r;} a[310];
int n,m;

void up(int &a,int b)
{
    a=min(a,b);
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("b.out","w",stdout);
    int cas;
    scanf("%d",&cas);
    for (int tt=1; tt<=cas; tt++)
    {
        scanf("%d%d",&n,&m);
        memset(v,255,sizeof(v));
        for (int i=1; i<=n; i++)
        {
            scanf("%d%d",&a[i].l,&a[i].r);
            for (int j=a[i].l; j<a[i].r; j++)
                v[j]=1;
         //   a[i].id=1;
        }
        for (int i=1; i<=m; i++)
        {
            scanf("%d%d",&a[n+i].l,&a[n+i].r);
             for (int j=a[i+n].l; j<a[i+n].r; j++)
                v[j]=0;
         //   a[n+i].id=-1;
        }
        int p=1;
        memset(f[0],127,sizeof(f[0]));
        memset(f[1],127,sizeof(f[1]));
        if (v[1]==1)
            f[1][1][1][1]=0;
        else if (v[1]==0) f[1][0][0][0]=0;
        else {
            f[1][1][1][1]=0;
            f[1][0][0][0]=0;
        }
        for (int i=2; i<=24*60; i++)
        {
            p^=1;
            memset(f[p],127,sizeof(f[p]));
            if (v[i]==1||v[i]==-1)
            {
                for (int j=0; j<min(i,721); j++)
                {
                    up(f[p][j+1][1][0],f[p^1][j][0][0]+1);
                    up(f[p][j+1][1][0],f[p^1][j][1][0]);
                    up(f[p][j+1][1][1],f[p^1][j][0][1]+1);
                    up(f[p][j+1][1][1],f[p^1][j][1][1]);
                }
            }
            if (v[i]==0||v[i]==-1)
            {
                for (int j=0; j<min(i,721); j++)
                {
                    up(f[p][j][0][0],f[p^1][j][0][0]);
                    up(f[p][j][0][0],f[p^1][j][1][0]+1);
                    up(f[p][j][0][1],f[p^1][j][0][1]);
                    up(f[p][j][0][1],f[p^1][j][1][1]+1);
                }
            }
        }

        printf("Case #%d: %d\n",tt,min(min(f[p][720][1][0]+1,f[p][720][0][1]+1),min(f[p][720][1][1],f[p][720][0][0])));
       // sort(a+1,a+1+n+m,cmp);
    }
}
