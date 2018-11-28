#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
const double pi = acos(-1.0);
const double e = exp(1.0);
int T,n;
double x,a[55];
double calc()
{
    double ans=0;
    while(x)
    {
        int i;
        for(i=2;i<=n;++i)
            if(a[i]!=a[i-1])
                break;
        if(i>n)
        {
            for(int i=1;i<=n;++i)
                a[i]+=x/n;
            break;
        }
        if(x>=(a[i]-a[i-1])*(i-1))
        {
            x-=(a[i]-a[i-1])*(i-1);
            for(int j=1;j<i;++j)
                a[j]=a[i];
        }
        else
        {
            for(int j=1;j<i;++j)
                a[j]+=x/(i-1);
            break;
        }
    }
    ans=1.0;
    for(int i=1;i<=n;++i)
        ans*=a[i];
    return ans;
}
int main()
{
    scanf("%d",&T);
    for(int t=1;t<=T;++t)
    {
        scanf("%d%*d%lf",&n,&x);
        for(int i=1;i<=n;++i)
            scanf("%lf",a+i);
        sort(a+1,a+1+n);
        printf("Case #%d: %.10f\n",t,calc());
    }
    return 0;
}
