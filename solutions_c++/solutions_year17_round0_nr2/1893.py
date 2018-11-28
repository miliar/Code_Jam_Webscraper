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
int t;
ll n;
bool C(ll x)
{
    int dig[20];
    ll r=1;
    for(int i=0;i<19;i++)
    {
        dig[i]=x/r%10;
        r*=10;
    }
    for(int i=0;i<18;i++)
    {
        if(dig[i]<dig[i+1])return 0;
    }
    return 1;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("2lout.txt","w",stdout);
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        scanf("%lld",&n);
        ll r=1;
        while(!C(n))
        {
            n=n%r+n/(r*10)*r*10-r;
            r*=10;
        }
        printf("Case #%d: %lld\n",cas,n);
    }
    return 0;
}
