#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
using namespace std;
const double PI = acos(-1.0);
struct bing
{
    int r,h,w;
    double ce;
}b[1010],c[1010];


bool cmp(bing a,bing d)
{
    if(a.ce==d.ce)
        return a.r>d.r;
    return a.ce>d.ce;
}
bool cmp1(bing a,bing d)
{
    if( a.r==d.r)
        return a.ce>d.ce;
    return a.r>d.r;
}
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t,icase=0;
    scanf("%d",&t);
    while(t--)
    {
        int n,k;
        scanf("%d%d",&n,&k);
        for(int i = 0 ; i < n; i++)
        {
            scanf("%d%d",&b[i].r,&b[i].h);
            c[i].w=b[i].w=i;
            b[i].ce=b[i].h*2.0*b[i].r*PI;
            c[i].r=b[i].r;c[i].h=b[i].h;
            c[i].ce=b[i].ce;
        }
        sort(b,b+n,cmp);
        sort(c,c+n,cmp1);
        double mans=0;

        for(int i = 0; i < n; i++)
        {
            double ans=0;
            ans+=c[i].r*1.0*c[i].r*PI;
            ans+=c[i].ce;
            int cal=1;
            for(int j = 0; j < n; j++)
            {
                if(cal==k)break;
                if(b[j].r>c[i].r||b[j].w==c[i].w)continue;
                ans+=b[j].ce;
                cal++;
            }
            if(cal==k)
            {
                if(mans<ans)mans=ans;
            }
        }

        printf("Case #%d: %.9lf\n",++icase,mans);
    }
    return 0;
}
