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
using std::vector;
#include<string>
using std::string;
#include<set>
using std::set;
#include<map>
using std::map;
#include<unordered_map>
#include<queue>
#include<tuple>
using lnt = long long int;
using unt = unsigned long long int;
using ust = unsigned;
using dou = double;
using P = std::pair<int,int>;
#define FZ(i,n)       for(int i=0;i<(n);++i)
#define FB(i,n)       for(int i=(n)-1;i>=0;--i)
#define FV(i,st,ed)   for(int i=st;i<(ed);++i)
#define FC(i,n)       for(int i=n;i;--i)
#define FZU(i,n)      for(ust i=0;i!=(n);++i)
#define FVU(i,st,ed)  for(ust i=st;i<(ed);++i)
#define FCU(i,n)      for(ust i=n;i;--i)
#define ALL(x)        std::begin(x),std::end(x)

#define RI(x) scanf("%d",&(x))
#define RII(x,y) scanf("%d %d",&(x),&(y))
#define RS(x) scanf("%s",x)
#define RI64(x) scanf("%lld",&(x))
#define RII64(x,y) scanf("%lld%lld",&(x),&(y))

#define FIR first
#define SEC second
#define pritnf printf
constexpr ust N = 100514u;
int g[N];
int dp[128][128][128]{};
int sol(int){
    int n,p;
    RII(n,p);
    int c[4]{};
    FZ(i,n){
        RI(g[i]);
        ++c[g[i]%p];
    }
    if(p==2){
        return c[0] + c[1]/2 + c[1]%2;
    }else if(p==3){
        int a = c[0];
        int mx(std::max(c[1],c[2]));
        int mn(std::min(c[1],c[2]));
        return a + mn + (mx-mn)/3 + ((mx-mn)%3!=0);
    }
    int mx(dp[c[1]][c[2]][c[3]]);
    FZ(i,c[1]+1)FZ(j,c[2]+1)FZ(k,c[3]+1)if(i!=c[1]||j!=c[2]||k!=c[3]){
        mx = std::max(mx,dp[i][j][k]+1);
    }
    return c[0]+mx;
}
struct ele{
    int di,dj,dk;
};
vector<ele>dd;
int main(){
    FZ(i,5)FZ(j,5)FZ(k,5){
        if((i+j+k) && (i*1+j*2+k*3)%4==0){
            dd.push_back(ele{i,j,k});
        }
    }
    FZ(i,128)FZ(j,128)FZ(k,128){
        for(auto e:dd){
            if(i>=e.di && j>=e.dj && k>=e.dk){
                dp[i][j][k] = std::max(dp[i][j][k],dp[i-e.di][j-e.dj][k-e.dk]+1);
            }
        }
    }
	int t; RI(t);
	FZ(i,t){
        int a = sol(i+1);
        printf("Case #%d: %u\n",i+1,a);
    }
}

