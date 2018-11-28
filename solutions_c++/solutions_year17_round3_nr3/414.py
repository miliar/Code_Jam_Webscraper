#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<vector>
#include<iostream>
#include<string>
#include<string.h>
using namespace std;
double a[100];
int main()
{
    freopen("C-small-1-attempt2.in","r",stdin);
    freopen("c1.out","w",stdout);
    int t,ca=0;
    scanf("%d",&t);
    while(t--)
    {
        int n,k;
        double u;
        scanf("%d%d",&n,&k);
        scanf("%lf",&u);
        for(int i=0;i<n;++i)
        {
            scanf("%lf",a+i);
        }
        sort(a,a+n);
        a[n]=1e70;
        for(int i=1;i<=n;++i)
        {
            double add;
            if((u+a[i-1]*i)/i<a[i])
                add=u/i;
            else add=a[i]-a[i-1];
            u-=i*add;
            for(int j=0;j<i;++j)
                a[j]+=add;
        }
        double ans=1;
        for(int i=0;i<n;++i)
            ans*=a[i];
        printf("Case #%d: %.10f\n",++ca,ans);

    }
}
