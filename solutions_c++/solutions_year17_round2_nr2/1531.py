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
#define pi acos(-1.0)
#define mod 1000000007
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
#define lrt rt<<1
#define rrt rt<<1|1
#define rep(i,a,b) for(int i=(a);i<(b);i++)
#define per(i,a,b) for(int i=(b)-1;i>=(a);i--)
#define mem(a,b) memset(a,b,sizeof(a))
#define lowbit(x) (x&-x)
#define gi(x) scanf("%d",&x)
#define gll(x) scanf("%lld",&x)
#define gc(x) scanf("%c",&x)
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int>P;
/***********************************************/
int t,n,x[10];
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("0b2ut.txt","w",stdout);
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        string s;char c[3]={'R','Y','B'};
        scanf("%d%d%d%d%d%d%d",&n,&x[0],&x[3],&x[1],&x[4],&x[2],&x[5]);
        int ma=0,num=0;
        if(x[0]>ma)ma=x[0],num=0;
        if(x[1]>ma)ma=x[1],num=1;
        if(x[2]>ma)ma=x[2],num=2;
        if(x[num]>x[(num+1)%3]+x[(num+2)%3]){
                printf("Case #%d: IMPOSSIBLE\n",cas);
                continue;
        }
        int x1=x[(num+1)%3],x2=x[(num+2)%3];
        for(int i=0;i<(x1+x2+1-x[num])/2;i++)
        {
            s+=c[(num+1)%3];s+=c[(num+2)%3];
            x[(num+1)%3]--;x[(num+2)%3]--;
        }
        if((x[(num+1)%3]+x[(num+2)%3]+1-x[num])&1)
        {
            if(x[(num+1)%3]!=0)
            {
                s+=c[(num+1)%3];x[(num+1)%3]--;
            }
            else
            {
                s+=c[(num+2)%3];x[(num+2)%3]--;
            }
        }
        for(int i=0;i<x[(num+1)%3];i++)
        {
            s+=c[num];s+=c[(num+1)%3];
        }
        for(int i=0;i<x[(num+2)%3];i++)
        {
            s+=c[num];s+=c[(num+2)%3];
        }
        s+=c[num];
        printf("Case #%d: ",cas);
        cout<<s<<endl;
    }
    return 0;
}
