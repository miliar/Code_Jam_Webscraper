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
typedef pair<LL,LL> II;
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

pair<LL,LL> ans;

bool cmp(II a, II b) {
  LL x1 = (a.F-1)/2LL;
  LL y1 = a.F/2LL;
  LL x2 = (b.F-1)/2LL;
  LL y2 = b.F/2LL;
  if(x1 == x2)
    return y1 >= x2;
  return x1 > x2;
}

void go(VII a, LL n) {
  map <LL,LL> b;
  sort(ALL(a), cmp);
  for(auto i : a) {
    LL x = (i.F-1)/2LL;
    LL y = i.F/2LL;
    LL cnt = i.S;
    if(cnt < n) {
      if(x)
        b[x] += cnt;
      if(y)
        b[y] += cnt;
      n -= cnt;
    }
    else {
      ans = MP(y,x);
      return;
    }
  }
  VII pp;
  for(auto i : b) {
    pp.PB(MP(i.F,i.S));
  }
  go(pp,n);
}


int main() {
  FILEIO("C")
  int t; cin >> t;
  REP(z,1,t+1) {
    LL n,k; cin >> n >> k;
    VII a;
    a.PB(MP(n,1));
    go(a,k);
    cout << "Case #" << z << ": " << ans.F << " " << ans.S << endl;
  }
  return 0;
}
