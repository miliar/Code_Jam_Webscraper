#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N=5e2+1;
const double pi=acos(-1);
double a[N];
int main()
{
    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("C-small-1-attempt0.out","w",stdout);
    int t,T;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        printf("Case #%d: ",t);
        int n,k,i;
        double u;
        cin>>n>>k>>u;
        for(i=0;i<n;i++)
        {
            scanf("%lf",a+i);
            u+=a[i];
        }
        sort(a,a+n);
        double ans=1.0;
        for(i=0;i<n;i++)
        if(u<(n-i)*a[n-i-1])
        {
            ans*=a[n-i-1];
            u-=a[n-i-1];
        }else break;
        double x=n-i;
        for(;i<n;i++)ans*=(u/x);
        printf("%.10f\n",ans);
     }
	return 0;
}
