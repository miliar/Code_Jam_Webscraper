#include<bits/stdc++.h>
using namespace std;
long long int Hd, Ad, Hk, Ak, B, D, nHd;
long long int atsolve()
{
    long long int Adc = Ad;
    long long int minv = (Hk+Adc-1)/Adc;
    for(int i=1; i<1e6; ++i)
    {
        Adc += B;
        minv = min( minv, i+(Hk+Adc-1)/Adc);
    }
    return minv;
}
long long int attacknow(long long int v)
{
    int nHd = ::nHd;
    for(int i=1; i<=1e6; ++i)
    {
        if(nHd>Ak || v==1) v--;
        else nHd = Hd;
        if(v==0) return i;
        nHd -= Ak;
        if(nHd<=0) return 1e9;
    }
    return 1e9;
}
int tmain()
{
    scanf("%lld%lld%lld%lld%lld%lld", &Hd, &Ad, &Hk, &Ak, &B, &D);
    nHd = Hd;
    long long int attackturn = atsolve();
    //printf("%lld\n",attackturn);
    long long int ans = 1e9;
    ans = min(ans, attacknow(attackturn));
    for(int i=1; i<=1e6; ++i)
    {
        bool flag = false;
        if(nHd>Ak-D && Ak != 0)
        {
            Ak -= D;
            flag = true;
            if (Ak < 0) Ak = 0;
        }
        else nHd = Hd;
        nHd -= Ak;
        if(nHd <= 0)
        {
            return ans;
        }
        if(flag) ans = min(ans, attacknow(attackturn)+i);
    }
    return ans;
}
int main()
{
    int T;
    scanf("%d",&T);
    for(int i=1; i<=T; ++i)
    {
        printf("Case #%d: ", i);
        long long int v = tmain();
        if(v>5e5) puts("IMPOSSIBLE");
        else printf("%lld\n",v);
    }
    return 0;
    
}