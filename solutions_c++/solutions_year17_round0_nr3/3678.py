#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

typedef long long ll;

ll N,K;

int main()
{
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1; cas<=T; cas++)
    {
        scanf("%lld%lld",&N,&K);
        ll cur = 1;
        ll odd, even;
        ll cntodd, cnteven;
        if(N&1) odd = N, even = N+1, cntodd = 1, cnteven = 0;
        else odd = N-1, even = N, cntodd = 0, cnteven = 1;
        while(K > cur)
        {
            K -= cur;
            cur *= 2;
            ll tmpcntodd = 0, tmpcnteven = 0;
            if((odd/2)&1){
                odd = odd/2;
                even = even - 1 - odd;
                tmpcntodd += cntodd*2 + cnteven;
                tmpcnteven += cnteven;
            }
            else
            {
                int neweven = odd/2;
                odd = even - 1 - neweven;
                even = neweven;
                tmpcnteven += cntodd*2 + cnteven;
                tmpcntodd += cnteven;
            }
            cntodd = tmpcntodd;
            cnteven = tmpcnteven;
        }
        printf("Case #%d: ",cas);
        if(odd > even)
        {
            if(K <= cntodd)
            {
                printf("%lld %lld\n",odd/2,odd/2);
            }
            else
            {
                printf("%lld %lld\n",odd/2,odd/2-1);
            }
        }
        else
        {
            if(K <= cnteven)
            {
                printf("%lld %lld\n",odd/2+1,odd/2);
            }
            else
            {
                printf("%lld %lld\n",odd/2,odd/2);
            }
        }

    }
    return 0;
}
