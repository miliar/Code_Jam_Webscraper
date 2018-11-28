#include <bits/stdc++.h>
using namespace std;


int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("3.txt", "w", stdout);
    int t,ti=1;scanf("%d",&t);
    while(t--)
    {
        printf("Case #%d: ",ti++);
        long long n,k;
        scanf("%lld%lld",&n,&k);
        long long a=1,b=0,c=n;
        long long l,r;
        while(1)
        {
            n--;
            if(a>=k)
            {
                k=0;
                l=n/2;
                r=(n+1)/2;
                break;
            }
            else if(a+b>=k)
            {
                k=0;
                l=(n-1)/2;
                r=n/2;
                break;
            }
            else
            {
                long long a1,b1;
                k-=a+b;
                if(n&1)
                    a1=a,b1=a+b+b;
                else
                    a1=a+a+b,b1=b;
                a=a1;
                b=b1;
                n=(n+1)/2;
            }
        }
        if(l<r)swap(l,r);
        printf("%lld %lld\n",l,r);
    }
    return 0;
}
