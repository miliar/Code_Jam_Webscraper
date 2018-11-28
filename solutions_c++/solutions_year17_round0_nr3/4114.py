#include <iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
typedef long long ll;
using namespace std;

int init(ll x)
{
    int ret = 0;
    while(x)
    {
        ret ++;
        x/=2;
    }
    return ret;
}

int main()
{
    int T, Case = 1;
    scanf("%d", &T);
    while(T--)
    {
        ll N, K;
        ll tmp = 0;
        scanf("%lld %lld", &N, &K);
        int len = init(K);
        len --;
        for(int i=0; i<len;i++)
            tmp += (1<<i);
        int t = len;
        N-=tmp;
        ll Min = N/(1<<t);
        ll Mincnt = (1<<t)*(Min+1) - N;
        ll Maxcnt = (1<<t)-Mincnt;
        ll Left = K - tmp; // 剩余的人
        int Max = Min;
        if(Maxcnt > 0) Max++;
        ll MAX, MIN;
//        printf("Left: %lld, Min: %lld Mincnt: %lld\n", Left, Min, Mincnt);
        if(Left <= Maxcnt)
        {
            MAX = (Max)/2;
            MIN = (Max-1)/2;
        }
        else
        {
            MAX = (Min)/2;
            MIN = (Min-1)/2;
        }
        printf("Case #%d: %lld %lld\n", Case++, MAX, MIN);
    }
    return 0;
}
