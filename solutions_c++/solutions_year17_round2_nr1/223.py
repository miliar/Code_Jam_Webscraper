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
constexpr ust N = 100514u;

lnt k[N],s[N];
void sol(int uuu){
    lnt d,n;
    RII64(d,n);
    FZ(i,n){
        RII64(k[i],s[i]);
    }
    dou ans(dou(d*s[0])/(d-k[0]));
    FV(i,1,n){
        auto tmp = dou(d*s[i])/(d-k[i]);
        ans = std::min(ans,tmp);
    }
    printf("Case #%d: %.16lf\n",uuu,ans);
}
int main(){
	int t; RI(t);
	FZ(i,t)sol(i+1);
}

