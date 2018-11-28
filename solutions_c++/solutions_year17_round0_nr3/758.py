//created by missever

#include<bits/stdc++.h>
#define MAX 1000000007
using namespace std;
typedef long long LL;

LL f1,f2;

void ff(LL n,LL k,LL a,LL b)
{
    LL c,d,m;
    if(n & 1)
    {
        m = n >> 1;
        c = a;
        d = b * 2 + a;
    }
    else
    {
        m = (n >> 1) - 1;
        c = a * 2 + b;
        d = b;
    }
    if(c + d > k)
    {
        k -= a + b - 1;
        if(k <= a)
        {
            f1 = (n + 1) >> 1;
            f2 = n >> 1;
        }
        else
        {
            f1 = n >> 1;
            f2 = (n - 1) >> 1;
        }
    }
    else ff(m,k,c,d);
}

int main(){
    //freopen("C-large.in","r",stdin);
    //freopen("C-large.out","w",stdout);
    int t;
    LL n,k;
    scanf("%d",&t);
    for(int cas = 1; cas <= t; cas++)
    {
        scanf("%lld%lld",&n,&k);
        ff(n,k,0,1);
        printf("Case #%d: %lld %lld\n",cas,f1,f2);
    }
    return 0;
}
