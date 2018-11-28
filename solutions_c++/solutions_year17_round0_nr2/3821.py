#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;
LL n;
LL p[20],t[20];

int ok(LL x)
{
    int d[20];
    int tot = 0;
    while(x)
    {
        ++tot;
        d[tot] = x % 10;x = x / 10;
    }

    for(int i = 2;i <= tot;i++)
    {
        if(d[i] > d[i-1]) return 0;
    }
    return 1;
}

int main()
{
    int T;
    p[0] = 1;t[0] = 1;
    for(int i = 1;i <= 17;i++) p[i] = p[i-1]*10 + 9,t[i] = t[i-1] * 10;
    t[18] = t[17] * 10;

    freopen("B-large.txt","r",stdin);
    freopen("Bjjy.txt","w",stdout);

    scanf("%d",&T);
    for(int kase = 1;kase <= T;kase++)
    {
        scanf("%lld",&n);
        printf("Case #%d: ",kase);
        int d[20],cd[20],tot = 0;
        LL ans = 0LL;
        if(ok(n)) ans = n;
        for(int i = 1;i <= 18;i++)
        {
            LL now = n - n % t[i];
           // printf("i = %d now = %I64d n = %I64d n % t[i] = %I64d\n",i,now,n,n % t[i]);
            if(ok(now)) ans = max(ans,now);
            if(ok(now - 1)) ans = max(ans,now-1);

        }

        printf("%lld\n",ans);
    }
    return 0;
}
