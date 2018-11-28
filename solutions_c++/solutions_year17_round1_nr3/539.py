#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int hk,ak,hd,ad,b,d,ans;

void Work(int x,int y)
{
    int hh=hd,aa=ad,h=hk,a=ak;
    for (int p=1; p<=ans; p++)
    {
        if (h-aa<=0)
        {
            ans=min(ans,p);
            return;
        }
        if (x>0)
        {
            int aa=max(a-d,0);
            if (hh-aa<=0) hh=hd; else
            {
                a=aa,x--;
            }
        } else
        if (hh-a<=0) hh=hd; else
        if (y>0) aa+=b,y--; else h-=aa;
        hh-=a;
        //printf("%d %d %d %d\n",hh,h,a,p);
    }
    //ans=min(ans,p);
    //printf("%d\n",ans);
}

int main()
{
    //freopen("c.in","r",stdin);
    //freopen("c.out","w",stdout);
    int T,w=0;
    for (scanf("%d",&T); T--; )
    {
        scanf("%d%d%d%d%d%d",&hd,&ad,&hk,&ak,&b,&d);
        ans=500;
        for (int i=0; i<=101; i++)
        for (int j=0; j<=101; j++) Work(i,j);
        printf("Case #%d: ",++w);
        if (ans==500) printf("IMPOSSIBLE\n"); else printf("%d\n",ans);
    }
    return 0;
}
