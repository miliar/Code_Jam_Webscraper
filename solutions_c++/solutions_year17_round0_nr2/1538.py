#include <bits/stdc++.h>
using namespace std;

#define TRACE
#ifdef TRACE
#define TR(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
  cerr << name << " : " << arg1 << std::endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
  const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
}
#else
#define TR(...)
#endif

typedef long long                LL;
typedef vector < int >           VI;
typedef pair < int,int >         II;
typedef vector < II >            VII;

#define MOD                      1000000007
#define EPS                      1e-12
#define N                        200100
#define PB                       push_back
#define MP                       make_pair
#define F                        first 
#define S                        second
#define ALL(v)                   v.begin(),v.end()
#define SZ(a)                    (int)a.size()
#define FILL(a,b)                memset(a,b,sizeof(a))
#define SI(n)                    scanf("%d",&n)
#define SLL(n)                   scanf("%lld",&n)
#define PLLN(n)                  printf("%lld\n",n)
#define PIN(n)                   printf("%d\n",n)
#define REP(i,j,n)               for(LL i=j;i<n;i++)
#define PER(i,j,n)               for(LL i=n-1;i>=j;i--)
#define endl                     '\n'
#define fast_io                  ios_base::sync_with_stdio(false);cin.tie(NULL)

#define FILEIO(name) \
  freopen(name".in", "r", stdin); \
freopen(name".out", "w", stdout);

inline int mult(int a , int b) { LL x = a; x *= LL(b); if(x >= MOD) x %= MOD; return x; }
inline int add(int a , int b) { return a + b >= MOD ? a + b - MOD : a + b; }
inline int sub(int a , int b) { return a - b < 0 ? MOD - b + a : a - b; }
LL powmod(LL a,LL b) { if(b==0)return 1; LL x=powmod(a,b/2); LL y=(x*x)%MOD; if(b%2) return (a*y)%MOD; return y%MOD; }

VI x;
const LL neg = -(LL(1e18));
LL dp[20][10][2];
LL pw[20];
LL go(int n, int last,int eq) {
  if(n==18) {
    if(eq) {
      if(x[n] >= last)
        return x[n];
      return neg;
    }
    else return 9;
  }
  if(dp[n][last][eq] != -1)
    return dp[n][last][eq];
  LL ret = neg;
  if(eq) {
    for(LL i = last; i < x[n]; i ++) 
      ret = max(ret, i*pw[n] + go(n+1, i, 0));
    if(x[n] >= last)
      ret = max(ret, x[n]*pw[n] + go(n+1, x[n], 1));
  }
  else 
    for(LL i = last; i < 10; i ++)
      ret = max(ret, i*pw[n] + go(n+1, i, 0));
  return dp[n][last][eq] = ret;
}

int main() {
  FILEIO("B")
  int t; cin >> t;
  pw[18] = 1LL;
  for(int i = 1; i <= 18; i ++)
    pw[18-i] = pw[18-i+1] * 10LL;
  REP(z,1,t+1) {
    x.clear();
    FILL(dp,-1LL);
    LL n; cin >> n;
    while(n > 0) {
      x.PB(n%10); n/=10;
    }
    while(SZ(x)<19)
      x.PB(0);
    reverse(ALL(x));
    for(int i : x)
      cerr<<i;
    cerr<<endl;
    cout << "Case #" << z << ": " << go(0,0,1) << endl;
  }
  return 0;
}
