#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int testcase;
    scanf("%d",&testcase);
    for (int test=1;test<=testcase;test++)
    {
        long long n,k;
        scanf("%lld%lld",&n,&k);
        long long base=1;
        for (;base<=k;base<<=1);
        base>>=1;
        //long long pp=((long long)floor(log2(k)));
        //long long base=1LL<<pp;
        long long t=(n-k)/base;
        cout<<"Case #"<<test<<": "<<(t+1)/2<<" "<<t/2<<endl;
    }
    return 0;
}
