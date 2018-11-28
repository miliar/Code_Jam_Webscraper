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
char s[N];
int n,a[N];
int c[8]{};
char m[8]{};
void mswap(int x,int y){
    int z = 7-x-y;
    std::swap(c[x  ],c[y  ]);
    std::swap(c[x+z],c[y+z]);
    std::swap(m[x  ],m[y  ]);
    std::swap(m[x+z],m[y+z]);
} 
bool sol(int){
    RI(n); std::fill_n(s,n+1,0);
    RII(c[1],c[1+2]);
    RII(c[2],c[2+4]);
    RII(c[4],c[4+1]);
    fprintf(stderr,"%d %d %d\n",c[1  ],c[2  ],c[4  ]);
    fprintf(stderr,"%d %d %d\n\n",c[1+2],c[2+4],c[4+1]);
    m[1  ] = 'R';
    m[1+2] = 'O';
    m[2  ] = 'Y';
    m[2+4] = 'G';
    m[4  ] = 'B';
    m[4+1] = 'V';
    int ecnt(0),zcnt(0);
    FZU(i,3){
        int j(1<<i);
        ecnt+= c[j]==c[7-j] && c[j]!=0;
        zcnt+= c[j]==0;
        if( c[j] < c[7-j] ){
            return 0;
        }else{
            c[j]-= c[7-j];
        }
    }
    if(ecnt==3 || ecnt==2){
        return 0;
    }else if(ecnt==1 && zcnt!=2){
        return 0;
    }
    if(c[1]>c[2])mswap(1,2);
    if(c[1]>c[4])mswap(1,4);
    if(c[2]>c[4])mswap(2,4);
    if(c[1]<c[4]-c[2]){
        return 0;
    }
    const int b[]{1,4,2,4,1,2,4};
    auto st(a);
    FZ(i,c[4]-c[2]){
        st = std::copy_n(b+0,4,st);
    }
    FZ(i,c[1]-(c[4]-c[2])){
        st = std::copy_n(b+4,3,st);
    }
    FZ(i,c[2]-c[1]){
        st = std::copy_n(b+2,2,st);
    }
    FZ(i,3){
        int j(1<<i),k(7-j);
        auto it(std::find(a,st,j));
        std::copy_backward(it,st,st+c[k]*2);
        st+= c[k]*2;
        FZ(t,c[k]){
            *(it++) = j;
            *(it++) = k;
        }
    }
    std::transform(a,a+n,s,[](int x){
        return m[x];
    });
    return 1;
}
int main(){
	int t; RI(t);
	FZ(i,t){
	    bool ok(sol(i+1));
	    if(!ok){
	       printf("Case #%d: %s\n",i+1,"IMPOSSIBLE");
	       continue;
        }
        printf("Case #%d: %s\n",i+1,s);
        FZU(i,3){
            int j(1<<i);
            c[j]+= c[7-j];
        }
        fprintf(stderr,"%d %d %d\n",c[1  ],c[2  ],c[4  ]);
        fprintf(stderr,"%d %d %d\n\n",c[1+2],c[2+4],c[4+1]);
        FV(i,1,n)assert((a[i]&a[i-1])==0);
        FZ(j,8)assert(std::count(a,a+n,j)==c[j]);
    }
}

