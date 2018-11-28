#include <iostream>
using namespace std;
#define ll long long

int main()
{   ll t,i;
    scanf("%lld",&t);
    for(i=1;i<=t;i++)
    {   printf("Case #%lld: ",i);
        double a,n,m=0.0;
        scanf("%lf%lf",&a,&n);
        while(n--)
        {   double x,y,q;
            scanf("%lf%lf",&x,&y);
            q=(a-x)/y;
            if(m<q)
                m=q;
        }
        a/=m;
        printf("%lf\n",a);
    }
    return 0;
}

