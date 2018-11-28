#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <vector>
#include <queue>

#define eps 1e-8
#define MOD 10009
#define MAXN 25
#define INF 99999999
using namespace std;
int equ,var;
int a[MAXN][MAXN];
int x[MAXN];
typedef long long ll;
char str[MAXN];
int main()
{
//    freopen("A-small-attempt0.in","r",stdin);
//    freopen("A-small-attempt0.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++)
    {
        ll n,k;
        scanf("%lld%lld",&n,&k);
        ll sum=0,cur=1;
        for(;sum+cur<k;sum+=cur,cur<<=1);
        long long ord=k-sum;
        long long ans=(n-sum)/cur;
        long long cnt=(n-sum)%cur;
        printf("Case #%d: ",kase);
        if(ord<=cnt)
            ans++;
       // printf("%lld\n",ans);
        printf("%lld %lld\n",ans/2,ans/2-((ans+1)&1));
    }
    return 0;
}
