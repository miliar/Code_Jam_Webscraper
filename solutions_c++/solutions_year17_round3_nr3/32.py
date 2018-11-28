#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<algorithm>
using namespace std;
typedef double db;
db p[55];
int main()
{
    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("C.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++)
    {
        int n,k;
        scanf("%d%d",&n,&k);
        db u;
        scanf("%lf",&u);
        for(int i=1;i<=n;i++)
            scanf("%lf",&p[i]);
        p[n+1]=1;
        sort(p+1,p+n+1);
        for(int i=1;i<=n;i++)
        {
            db add=min(u/i,p[i+1]-p[i]);
            u-=add*i;
            for(int j=1;j<=i;j++)
                p[j]+=add;
        }
        db res=1;
        for(int i=1;i<=n;i++)
            res*=p[i];
        printf("Case #%d: %.12f\n",ca,res);
    }
    return 0;
}
