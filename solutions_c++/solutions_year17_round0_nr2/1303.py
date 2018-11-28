#include<cctype>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<cmath>
#include<cassert>
#include<algorithm>
#include<numeric>
#include<vector>
#include<string>
#include<map>
#include<unordered_map>
#include<queue>
#include<tuple>
using namespace std;
typedef long long int lnt;
typedef unsigned long long int unt;
typedef unsigned ust;
typedef double dou;
typedef pair<int,int> P;
#define FZ(i,n)       for(int i=0;i<(n);++i)
#define FB(i,n)       for(int i=(n)-1;i>=0;--i)
#define FV(i,st,ed)   for(int i=st;i<(ed);++i)
#define FC(i,n)       for(int i=n;i;--i)
#define FZU(i,n)      for(ust i=0;i!=(n);++i)
#define FVU(i,st,ed)  for(ust i=st;i<(ed);++i)
#define FCU(i,n)      for(ust i=n;i;--i)
#define SZ(x)         ((int)x.size())
#define ALL(x)        std::begin(x),std::end(x)
#define likely(x)     __builtin_expect(!!(x), 1)
#define unlikely(x)   __builtin_expect(!!(x), 0)

#define RI(x) scanf("%d",&(x))
#define RII(x,y) scanf("%d %d",&(x),&(y))
#define RS(x) scanf("%s",x)
#define RI64(x) scanf("%lld",&(x))
#define RII64(x,y) scanf("%lld%lld",&(x),&(y))

#define FIR first
#define SEC second
#define pritnf printf
constexpr ust N = 100514u;
unt dp[64][2][16];

//dp[i][0][k] = dp[i-1][0][p]*(p<=k) + dp[i-1][1][p]*(p<=k)*(k<n[i])
//dp[i][1][k] = dp[i-1][1][p]*(p<=k)*(k==n[i])
void sol(int uuu){
    unt n[64]{},n_;
    scanf("%llu",&n_);
    ust l(0);
    for(;n_;++l){
        n[l] = n_%10; n_/=10;
    }
    std::reverse(n,n+l);
    memset(dp,0,sizeof(dp));
    FZU(p,10){
        dp[0][0][p] = (p <n[0])*p;
        dp[0][1][p] = (p==n[0])*p;
    }
    FVU(i,1,l){
        FZU(k,10){
            FZU(p,k+1){
                dp[i][0][k] = max(dp[i][0][k],dp[i-1][0][p]);
                if(k <n[i]){
                    dp[i][0][k] = max(dp[i][0][k],dp[i-1][1][p]);
                }else if(k==n[i]){
                    dp[i][1][k] = max(dp[i][1][k],dp[i-1][1][p]);
                }
            }
            dp[i][0][k] = dp[i][0][k]*10+k;
            dp[i][1][k] = dp[i][1][k]*10+k;
        }
    }
    /*
    FZU(j,2){
        FZU(i,l){
            FZU(p,10){
                printf("%10llu ",dp[i][j][p]);
            }puts("");
        }puts("");
    }
    */
    unt sum(max(*max_element(ALL(dp[l-1][0])),*max_element(ALL(dp[l-1][1]))));
    printf("Case #%d: %llu\n",uuu,sum);
}
int main(){
	int t; RI(t);
	FZ(i,t)sol(i+1);
}

