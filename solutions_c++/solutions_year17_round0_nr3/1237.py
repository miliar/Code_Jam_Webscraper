#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <queue>
using namespace std;
#define INF 0x3f3f3f3f
#define LL long long
#define fi first
#define se second
#define mem(a,b) memset((a),(b),sizeof(a))

LL N,K;

int main()
{
    freopen("/Users/xuehao/Documents/s1/in", "r", stdin);
    freopen("/Users/xuehao/Documents/s1/out", "w", stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;++cas)
    {
        printf("Case #%d: ",cas);
        scanf("%lld%lld",&N,&K);
        LL num1=0,num2=1,l1=N-1,l2=N;
        while(true)
        {
//            cout<<"K: "<<K<<" num1: "<<num1<<" num2: "<<num2<<" l1: "<<l1<<" l2: "<<l2<<endl;
            if(K<=num1+num2)
            {
                LL ans1,ans2;
                if(K<=num2)
                {
                    ans1=(l2-1)/2;
                    ans2=(l2-1-(l2-1)/2);
                }
                else
                {
                    ans1=(l1-1)/2;
                    ans2=(l1-1-(l1-1)/2);
                }
                printf("%lld %lld\n",max(ans1,ans2),min(ans1,ans2));
                break;
            }
            K-=(num1+num2);
            if(l2&1)
            {
                l2=(l2-1)/2;
                l1=(l1-1)/2;
                num2=2*num2+num1;
            }
            else
            {
                l2=(l2-1)/2+1;
                l1=(l1-1)/2;
                num1=2*num1+num2;
            }
        }
    }
    
    return 0;
}
