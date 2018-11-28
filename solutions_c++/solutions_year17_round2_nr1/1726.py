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
int t,d,n,k[1005],s[1005];
double mat;
int main()
{
    freopen("A-large (2).in","r",stdin);
    freopen("0alut.txt","w",stdout);
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        mat=0;
        scanf("%d%d",&d,&n);
        for(int i=0;i<n;i++){
                scanf("%d%d",&k[i],&s[i]);
                mat=max(mat,(d-k[i])/(1.0*s[i]));
        }
        printf("Case #%d: %.6lf\n",cas,d/mat);
    }
    return 0;
}
