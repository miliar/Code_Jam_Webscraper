#include<bits/stdc++.h>
using namespace std;

long long repetfactor(long long k)
{
    return pow(2,(long long)floor(log(k)/log(2)));
}

int main()
{
    freopen("D:\C-small-2-attempt0.in","r",stdin);
    freopen("D:\C-small-2-attempt0.out","w",stdout);
    long long int t,n,k,case1=0LL;
    long long x;
    scanf("%lld",&t);
    while(case1++<t)
    {
        scanf("%lld%lld",&n,&k);
        long long r=repetfactor(k);
        long long pairno=n-k+1,num;
        num=ceil((float)pairno/r);
        long long a,b=1;
        a=num;
        //printf("%lld %lld %lld %lld\n",a,b,r,pairno);
        printf("Case #%lld: ",case1);
        if(a%2)
        {
            cout<<a/2<<" "<<a/2<<endl;
        }
        else
        {
            x=a/2LL;
            long long y=x-1;
            cout<<x<<" "<<y<<endl;
        }
    }
    return 0;
}
