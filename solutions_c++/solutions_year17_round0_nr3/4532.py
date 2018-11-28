#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
ll maxlen(ll n,ll k)
{
    if(k==1) return n>>1;
    if(n&1) return maxlen(n>>1,k>>1);
    if(k&1) return maxlen((n-2)>>1,k>>1);
    return maxlen(n>>1,k>>1);
}
ll minlen(ll n,ll k)
{
    if(k==1) return (n-1)>>1;
    if(n&1) return minlen(n>>1,k>>1);
    if(k&1) return minlen((n-2)>>1,k>>1);
    return minlen(n>>1,k>>1);
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,caseno = 0;
    scanf("%d",&T);
    while (T--)
    {
        ll n,k;
        scanf("%I64d%I64d",&n,&k);
        printf("Case #%d: ",++caseno);
        printf("%I64d %I64d\n",maxlen(n,k),minlen(n,k));
    }
    return 0;
}
