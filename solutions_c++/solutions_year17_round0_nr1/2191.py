/**************Powered by Graphene Richards**************/
extern"C++"{
#define FLOAT_PRECISION     2

#ifdef _MSC_VER
#define _SECURE_SCL 0
#pragma comment(linker,"/STACK:102400000,102400000")
#else
#pragma GCC optimize("O3")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx")
#endif
#if defined(_MSC_VER)||__cplusplus>199711L
#define IT(x) decltype((x).begin())
#define DIT(x) decltype((x).begin())
#else
#define IT(x) __typeof((x).begin())
#define DIT(x) __typeof((x).rbegin())
#endif

#  inc\
lude<cmath>
#  inc\
lude<cstdio>
#  inc\
lude<cstdlib>
#  inc\
lude<cstring>
#  inc\
lude<algorithm>
#  inc\
lude<bitset>
#  inc\
lude<complex>
#  inc\
lude<vector>
#  inc\
lude<iomanip>
#  inc\
lude<iostream>
#  inc\
lude<list>
#  inc\
lude<map>
#  inc\
lude<queue>
#  inc\
lude<set>
#  inc\
lude<stack>
#  inc\
lude<string>
#define FAST_RW ios_base::sync_with_stdio(0),cin.tie(0);
#define FS(i,a) for(ll i=0;a[i];i++)
#define FE(it,x) for(IT(x) it=(x).begin(),_en=(x).end();it!=_en;it++)
#define EF(it,x) for(DIT(x) it=(x).rbegin(),_en=(x).rend();it!=_en;it++)
#define FR(i,en) for(ll i=0,_en=(en);i<_en;i++)
#define FOR(i,en) for(ll i=1,_en=(en);i<=_en;i++)
#define RF(i,en) for(ll i=(en)-1;i>=0;i--)
#define ROF(i,en) for(ll i=(en);i>0;i--)
#define FFR(i,x,y) for(ll i=(x),_en=(y);i<=_en;i++)
#define RFF(i,x,y) for(ll i=(x),_en=(y);i>=_en;i--)
#define ptf printf
#define scf scanf
#define pc putchar
#define pb push_back
#define ppb pop_back
#define pq priority_queue
#define fi first
#define se second
#define mp make_pair
#define pii pair<int,int>
#define pll pair<ll,ll>
#define sqr(x) ((x)*(x))
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
#define clr(x) memset((x),0,sizeof(x))
#define ms(x,v) memset((x),(v),sizeof(x))
#define mc(x,y) memcpy((x),(y),sizeof(y))
#define NL puts("");
#define LB lower_bound
#define UB upper_bound
#define rand() ((rand()<<16)^(rand()<<15)^(rand()))
#ifdef _WIN32
#define _i64_ "%I\
64d"
#define _u64_ "%I\
64u"
#else
#define _i64_ "%l\
ld"
#define _u64_ "%l\
lu"
#endif
typedef unsigned ui;
typedef long long ll;
typedef unsigned long long ull;
typedef long double lf;
using namespace std;

ll gcd(ll a,ll b){if(!b)return a;while(b^=a^=b^=a%=b);return a;}

extern const ll MOD;
ll ksm(ll a,ll b){
ll res=1;a%=MOD;
for(;b;b>>=1){if(b&1)res=res*a%MOD;a=a*a%MOD;}
return res;
}

#ifdef wmx16835
#include"wmx16835.h"
#else
#define LOG
#define TEL
#define test(...) 0
#define TEST(...) 0
#define DE if(0)
#define AS(...)
#define SF(...)
#define SC
#define PF
#define PC
#define PP
#define SHOW_TIME
#define BR
#endif
#define y0 NKwKGuBI
#define y1 KFJssmlK
#define yn XypGISMR
#define j1 kQDCYYWX
#define tm BdKIQNcs
#define lr UsCPcJvt

template<class T1,class T2,class T3>bool In(T1 x,T2 y,T3 z){return x<=y&&x>=z||x<=z&&x>=y;}
template<class T1,class T2>T1 max(const T1&a,const T2&b){return a<b?b:a;}
template<class T1,class T2,class T3>T1 max3(const T1&a,const T2&b,const T3&c){return a<b?(b<c?c:b):(a<c?c:a);}
template<class T1,class T2>T1 min(const T1&a,const T2&b){return a<b?a:b;}
template<class T1,class T2,class T3>T1 min3(const T1&a,const T2&b,const T3&c){return a<b?(a<c?a:c):(b<c?b:c);}

bool S(char*a){return scf("%s",a)==1;}
bool S(int&a){return scf("%d",&a)==1;}
bool S(bool&a){return scf("%d",&a)==1;}
bool S(ui&a){return scf("%u",&a)==1;}
bool S(float&a){return scf("%f",&a)==1;}
bool S(double&a){return scf("%lf",&a)==1;}
bool S(ll&a){return scf(_i64_,&a)==1;}
bool S(ull&a){return scf(_u64_,&a)==1;}
bool S(lf&a){double b;if(scf("%lf",&b)==-1)return 0;a=b;return 1;}
bool S(char&a){char b[2];if(scf("%1s",b)==-1)return 0;a=*b;return 1;}
bool SL(char*a){a[0]=0;while(gets(a)&&!a[0]);return a[0];}
template<class T1,class T2>bool S(pair<T1,T2>&a){return S(a.fi, a.se);}
template<class T>void S(T&a){a.in();}

void _P(const int&x){ptf("%d",x);}
void _P(const bool&x){ptf("%d",x);}
void _P(const ui&x){ptf("%u",x);}
void _P(const char&x){ptf("%c",x);}
void _P(const char*x){ptf("%s",x);}
void _P(const string&x){ptf("%s",x.c_str());}
void _P(const ll&x){ptf(_i64_,x);}
void _P(const ull&x){ptf(_u64_,x);}
void _P(const float&x){ptf("%.*f",FLOAT_PRECISION,x);}
void _P(const double&x){ptf("%.*f",FLOAT_PRECISION,x);}
void _P(const lf&x){ptf("%.*f",FLOAT_PRECISION,(double)x);}
template<class T1,class T2>void _P(const pair<T1,T2>&x){_P(x.fi);pc(' ');_P(x.se);}
template<class T>void _P(const T&a){a.out();}
template<class T1>void P(const T1&a){_P(a);pc(' ');}
template<class T1>void PN(const T1&a){_P(a);NL}
void PS(int a){ptf("%*s",a,"");}
template<class T>void SA(T*a,int n){FR(i,n)S(a[i]);}
template<class T>void PA(T*a,int n){FR(i,n){if(i)pc(' ');_P(a[i]);}NL}
template<class T>void PA(const T&x){FE(it,x){if(it!=x.begin())pc(' ');_P(*it);}NL}
#if defined(_MSC_VER)||__cplusplus>199711L
template<class T,class...U>bool S(T&t,U&...u){return S(t)&&S(u...);}
template<class T,class...U>void P(const T&t,const U&...u){P(t);P(u...);}
template<class T,class...U>void PN(const T&t,const U&...u){P(t);PN(u...);}
#else
template<class T1,class T2>bool S(T1&a,T2&b){return S(a)&S(b);}
template<class T1,class T2,class T3>bool S(T1&a,T2&b,T3&c){return S(a)&S(b)&S(c);}
template<class T1,class T2>void P(const T1&a,const T2&b){P(a);P(b);}
template<class T1,class T2>void PN(const T1&a,const T2&b){P(a);PN(b);}
template<class T1,class T2,class T3>void PN(const T1&a,const T2&b,const T3&c){P(a,b);PN(c);}
#endif

int kase;
const double pi=acos(-1);
const double ep=1e-9;
const int INF=0x3f3f3f3f;
const ll INFL=0x3f3f3f3f3f3f3f3fll;
const ll MOD=1000000007;
}

char s[1005];

int solve(int k) {
  int res = 0, n = strlen(s);
  for (int i = 0; i <= n - k; ++i) {
    if (s[i] == '-') {
      ++res;
      for (int j = 0; j < k; ++j) {
        s[i + j] = (s[i + j] == '+' ? '-' : '+');
      }
    }
  }
  for (int i = n - k + 1; i < n; ++i) {
    if (s[i] == '-') {
      return INF;
    }
  }
  return res;
}

int main() {
  SF(OUT/A-large.in);
  PF
  int T;
  S(T);
  while (T--) {
    int k;
    S(s, k);
    int res = solve(k);
    printf("Case #%d: ", ++kase);
    if (res == INF) {
      puts("IMPOSSIBLE");
    } else {
      printf("%d\n", res);
    }
  }
}

/*********Risoft corporation all rights reserved*********/
/**************Template V2.35 build 20160703*************/
