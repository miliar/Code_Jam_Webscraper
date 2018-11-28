#include <cstdio>
#include <algorithm>

using namespace std;

struct punct
{
    int x,y;
};

punct v[55][55];
int val[55],poz[55];

int cmp(punct a,punct b)
{
    if(a.x==b.x) return a.y<b.y;
    else return a.x<b.x;
}

int main()
{
    freopen("file.in","r",stdin);
    freopen("file.out","w",stdout);
    int t,n,p,x1;
    scanf("%d",&t);
    for(int test=1;test<=t;test++)
    {
        scanf("%d%d",&n,&p);
        for(int i=1;i<=n;i++) scanf("%d",&val[i]);
        for(int i=1;i<=n;i++)
            for(int j=1;j<=p;j++)
            {
                scanf("%d",&x1);
                double vall=(x1*10.0)/(11.0*val[i]);
                v[i][j].x=vall;
                if(vall>v[i][j].x) v[i][j].x++;
                v[i][j].y=(x1*10.0)/(9.0*val[i]);
                if(v[i][j].x>v[i][j].y) v[i][j]={0,0};
            }
        for(int i=1;i<=n;i++)
            sort(v[i]+1,v[i]+p+1,cmp);
        for(int i=1;i<=n;i++)
        {
            poz[i]=1;
            while(v[i][poz[i]].x==0 && poz[i]<=p) poz[i]++;
        }
        int sol=0;
        while(1)
        {
            int c=0;
            for(int i=1;i<=n;i++) if(poz[i]>p) {c=1;break;}
            if(c==1) break;
            int x=v[1][poz[1]].x,y=v[1][poz[1]].y,p=0,pozi=0,minn=1e9;
            for(int i=1;i<=n;i++)
            {
                if(v[i][poz[i]].x<minn) {minn=v[i][poz[i]].x;pozi=i;}
                if((v[i][poz[i]].y>=x && v[i][poz[i]].y<=y) or (v[i][poz[i]].x>=x && v[i][poz[i]].x<=y)) {x=max(x,v[i][poz[i]].x);y=min(y,v[i][poz[i]].y);}
                else p=1;
            }
            if(p==1) poz[pozi]++;
            else {sol++;for(int i=1;i<=n;i++) poz[i]++;}
        }
        for(int i=1;i<=n;i++)
            for(int j=1;j<=p;j++) v[i][j]={0,0};
        printf("Case #%d: %d\n",test,sol);
    }
    return 0;
}
