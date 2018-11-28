#include <bits/stdc++.h>
using namespace std;
int main()
{
    long long n,k,c,p,l,o;
    int t;
    scanf("%d",&t);
    for(int i=1; i<=t; ++i)
    {
        printf("Case #%d: ",i);
        scanf("%lld %lld",&n,&k);
        c=k/2;
        p=1;
        l=0;
        o=1;
        while(c)
        {
            c/=2;
            p*=2;
            if(n%2)
            {
                o=o*2+l;
            }
            else
            {
                l=l*2+o;
                --n;
            }
            n/=2;
        }
        if(k<p+l)
        {
            ++n;
        }
        if(n%2)
        {
            printf("%lld %lld\n",n/2,n/2);
        }
        else
        {
            printf("%lld %lld\n",n/2,(n/2)-1);
        }
    }
    return 0;
}
