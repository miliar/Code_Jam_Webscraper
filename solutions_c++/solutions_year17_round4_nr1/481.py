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

int a[105];

int main(){
    int t;
    freopen("A-large.in","r",stdin);
    freopen("out.out","w",stdout);
    cin>>t;
    int kase=0;
    while(t--){
        int n,p;
        cin>>n>>p;
        kase++;
        printf("Case #%d: ",kase);
        for(int i=0;i<n;i++) scanf("%d",&a[i]);
        if(p==2){
            int ans1=0;
            int ans2=0;
            for(int i=0;i<n;i++){
                if(a[i]%2==0) ans1++;
                else ans2++;
            }
            cout<<ans1+(ans2+1)/2<<endl;
        }
        else if(p==3){
            int ans1=0;
            int ans2=0;
            int ans3=0;
            for(int i=0;i<n;i++){
                if(a[i]%3==0) ans1++;
                else if(a[i]%3==1) ans2++;
                else ans3++;
            }
            cout<<ans1+min(ans2,ans3)+(max(ans2,ans3)-min(ans2,ans3)+2)/3<<endl;
        }
        else if(p==4){
            int ans1=0,ans2=0,ans3=0,ans4=0;
            for(int i=0;i<n;i++){
                if(a[i]%4==0) ans1++;
                else if(a[i]%4==1) ans2++;
                else if(a[i]%4==2) ans3++;
                else ans4++;
            }
            int ans=ans1+min(ans2,ans4)+ans3/2;
            if(ans3%2==0){
                ans+=(max(ans2,ans4)-min(ans2,ans4)+3)/4;
            }
            else{
                int tmp=max(ans2,ans4)-min(ans2,ans4);
                if(tmp>=2) ans=ans+1+(tmp-2+3)/4;
                else ans++;

            }
            cout<<ans<<endl;
        }
    }
    return 0;
}
