#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int CountBit(long long n)
{
    int ret=0;
    for (;n!=0;n/=10) ++ret;
    return ret;
}

long long calc(long long n)
{
    if (n<10) return n;
    long long m=1;
    while (n/m!=0&&m<1e18) m*=10;
    if (n<m) m/=10;
    long long tmp=calc(n%m);
    if (n/m<=tmp/(m/10)) return n/m*m+tmp;
    return m-1+(n/m-1)*m;
}

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int t;
    long long n;
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas)
    {
        cin>>n;
        printf("Case #%d: %I64d\n",cas,calc(n));
    }
    return 0;
}
