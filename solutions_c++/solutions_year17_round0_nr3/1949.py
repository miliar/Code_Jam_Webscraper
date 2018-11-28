#include<iostream>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<set>
#include<bitset>
#include<map>
#include<stack>
#include<queue>
#include<vector>
#include<utility>
#define INF 0x3f3f3f3f
#define inf 2*0x3f3f3f3f
#define llinf 1000000000000000000
#define pi acos(-1)
#define mod 1000000007
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
using namespace std;
typedef long long ll;
typedef pair<int,int>P;
ll n,k,t,res,x,num0,num1,ma,mi;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("c3out.txt","w",stdout);
    scanf("%lld",&t);
    for(int cas=1;cas<=t;cas++)
    {
        res=1;
        scanf("%lld%lld",&n,&k);
        while(k>res*2-1)res*=2;
        n-=res-1;
        x=n/res;
        num1=n-x*res;
        num0=res-num1;
        if(x&1)
        {
            mi=x/2;
            if(k-res+1<=num1)ma=mi+1;
            else ma=mi;
        }
        else
        {
            ma=x/2;
            if(k-res+1>num1)mi=ma-1;
            else mi=ma;
        }
        printf("Case #%d: %lld %lld\n",cas,ma,mi);
    }
    return 0;
}
