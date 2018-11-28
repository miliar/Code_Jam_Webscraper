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

int r[100];
int q[100][100];
int num[100];
int n,p;

bool check(int i,int j){
    //cout<<r[j]*i*0.9<<" "<<q[j][num[j]]<<" "<<r[j]*i*1.1<<endl;
    if(num[j]<p&&(LL)r[j]*i*9<=(LL)q[j][num[j]]*10&&(LL)r[j]*i*11>=(LL)q[j][num[j]]*10) return true;
    //cout<<1<<endl;
    return false;
}
int main(){
    int t;
    freopen("B-large.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&t);
    int kase=0;
    while(t--){
        cin>>n>>p;
        mem(num,0);
        for(int i=0;i<n;i++) scanf("%d",&r[i]);
        int maxn=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<p;j++) scanf("%d",&q[i][j]),maxn=max(maxn,q[i][j]);
            sort(q[i],q[i]+p);
        }
        int ans=0;
        for(int i=1;i<=maxn;i++){
            int flag=0;
            for(int j=0;j<n;j++){
                LL tmp=(LL)r[j]*i*9;
                while(num[j]<p&&(LL)q[j][num[j]]*10<tmp) num[j]++;
                if((LL)q[j][num[j]]*10>(LL)r[j]*i*11||num[j]>=p) flag=1;
            }
            if(!flag){
                ans++;
                i--;
                for(int j=0;j<n;j++) num[j]++;
            }
        }
        kase++;
        printf("Case #%d: %d\n",kase,ans);
    }
    return 0;
}
