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

char s[30][30];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.out","w",stdout);
    int t;
    cin>>t;
    int kase=0;
    while(t--){
        int r,c;
        scanf("%d%d",&r,&c);
        for(int i=0;i<r;i++) scanf("%s",s[i]);
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                if(s[i][j]!='?'){
                    for(int k=j+1;k<c;k++){
                        if(s[i][k]=='?') s[i][k]=s[i][j];
                        else break;
                    }
                    for(int k=j-1;k>=0;k--){
                        if(s[i][k]=='?') s[i][k]=s[i][j];
                        else break;
                    }
                }
            }
        }
        for(int i=0;i<r;i++){
            if(s[i][0]!='?'){
                for(int k=i-1;k>=0;k--){
                    if(s[k][0]=='?'){
                        for(int j=0;j<c;j++) s[k][j]=s[i][j];
                    }
                    else break;
                }
                for(int k=i+1;k<r;k++){
                     if(s[k][0]=='?'){
                        for(int j=0;j<c;j++) s[k][j]=s[i][j];
                    }
                    else break;
                }
            }
        }
        kase++;
        printf("Case #%d:\n",kase);
        for(int i=0;i<r;i++) printf("%s\n",s[i]);
    }
    return 0;
}
