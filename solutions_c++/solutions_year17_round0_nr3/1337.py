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
constexpr ust N = 1<<20;
void sol(int uuu){
    unt n,k;
    scanf("%llu %llu",&n,&k);
    std::map<unt,unt>c;
    c.insert(make_pair(n,1));
    unt l(0),r(0);
    static int mxk = 0; 
    int kkk=0;
    for(;k && !c.empty();){
        auto it(c.rbegin());
        unt d = min(k,it->SEC);
        unt i = it->FIR;
        l = (i-1)-(i-1)/2;
        r = (i-1)/2;
        c[l]+= d;
        c[r]+= d;
        k-= d;
        c.erase(i);
        ++kkk;
    }
    mxk = max(mxk,kkk);
    fprintf(stderr,"%10d %10d\n",kkk,mxk);
    printf("Case #%d: %llu %llu\n",uuu,l,r);
}
int main(){
	int t; RI(t);
	FZ(i,t)sol(i+1);
}

