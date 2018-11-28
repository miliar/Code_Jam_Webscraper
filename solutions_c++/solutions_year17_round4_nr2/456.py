#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cmath>
#include <string>
#include <vector>
#include <cstdio>
#include <cctype>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#pragma comment(linker,"/STACK:102400000,102400000")

using namespace std;
#define   MAX           100005
#define   MAXN          1000005
#define   maxnode       105
#define   sigma_size    30
#define   lson          l,m,rt<<1
#define   rson          m+1,r,rt<<1|1
#define   lrt           rt<<1
#define   rrt           rt<<1|1
#define   middle        int m=(r+l)>>1
#define   LL            long long
#define   ull           unsigned long long
#define   mem(x,v)      memset(x,v,sizeof(x))
#define   lowbit(x)     (x&-x)
#define   pii           pair<int,int>
#define   bits(a)       __builtin_popcount(a)
#define   mk            make_pair
#define   limit         10000

//const int    prime = 999983;
const int    INF   = 0x3f3f3f3f;
const LL     INFF  = 0x3f3f;
const double pi    = acos(-1.0);
const double inf   = 1e18;
const double eps   = 1e-8;
const LL     mod   = 1e9+7;
const ull    mx    = 133333331;

/*****************************************************/
inline void RI(int &x) {
      char c;
      while((c=getchar())<'0' || c>'9');
      x=c-'0';
      while((c=getchar())>='0' && c<='9') x=(x<<3)+(x<<1)+c-'0';
 }
/*****************************************************/

int a[1005],b[1005];

int x[1005],y[1005];
int main(){
    int t;
    freopen("B-large.in","r",stdin);
    freopen("out.out","w",stdout);
    cin>>t;
    int kase=0;
    while(t--){
        kase++;
        printf("Case #%d: ",kase);
        int n,c,m;
        cin>>n>>c>>m;
        mem(x,0);
        mem(y,0);
        int ans=0,ret=0;
        for(int i=0;i<m;i++) scanf("%d%d",&a[i],&b[i]),x[a[i]]++,y[b[i]]++,ans=max(ans,y[b[i]]);
        int tmp=0;
        for(int i=1;i<=n;i++){
            tmp+=x[i];
            int temp=tmp+i;
            temp--;
            temp/=i;
            ans=max(ans,temp);
        }
        for(int i=1;i<=n;i++){
            if(x[i]>=ans) ret+=x[i]-ans;
        }
        cout<<ans<<" "<<ret<<endl;
    }
    return 0;
}
