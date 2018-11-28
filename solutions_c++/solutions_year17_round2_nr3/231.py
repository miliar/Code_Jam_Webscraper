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
constexpr ust N = 128;
int n,q;
lnt e[N],s[N],d[N][N];
dou ee[N][N];
void sol(int uuu){
    RII(n,q);
    FZ(i,n)RII64(e[i],s[i]);
    FZ(i,n){
        FZ(j,n){
            lnt x;
            RI64(x);
            if(x==-1)x = 1ll<<50;
            d[i][j] = x;
        }
        d[i][i] = 0;
    }
    FZ(k,n)FZ(i,n)FZ(j,n){
        d[i][j] = std::min(d[i][j],d[i][k]+d[k][j]);
    }
    FZ(i,n)FZ(j,n)ee[i][j] = 1ll<<50;
    FZ(i,n){
        FZ(j,n)if(d[i][j]<=e[i]){
            ee[i][j] = std::min(ee[i][j],dou(d[i][j])/s[i]);
        }
        ee[i][i] = 0;
    }
    /*
    FZ(i,n){
        FZ(j,n){
            fprintf(stderr,"%.6lf ",ee[i][j]);
        }fputs("\n",stderr);
        fputs("\n",stderr);
    }
    */
    FZ(k,n)FZ(i,n)FZ(j,n){
        ee[i][j] = std::min(ee[i][j],ee[i][k]+ee[k][j]);
    }
    vector<P>qq;
    FZ(i,q){
        int v,u;
        RII(v,u);
        qq.emplace_back(v-1,u-1);
    }
    pritnf("Case #%d:",uuu);
    FZ(i,q){
        printf(" %.10lf",ee[qq[i].FIR][qq[i].SEC]);
    }
    puts("");
}
int main(){
	int t; RI(t);
	FZ(i,t)sol(i+1);
}

