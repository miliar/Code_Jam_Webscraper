#include<bits/stdc++.h>
using namespace std;

typedef long long       LL;

#define all(c) (c).begin(), (c).end()
#define REP(i,n) for(__typeof(n) i = 0; i < n; i++)
#define REP1(i,n) for(__typeof(n) i = 1; i <= n; i++)
#define REPn(i,j,n) for(__typeof(n) i = j; i < n; i++)
#define tr(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define SZ(c) (int)(c).size()
#define iOS ios_base::sync_with_stdio(false)
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define MT make_tuple
template<typename T> T gcd(T a, T b) { return b == 0?a: gcd(b, a % b); }
template<typename T> T LCM(T a, T b) { return a*(b/gcd(a, b)); }
template<typename T> T expo(T base, T e, T mod) { T res = 1;
  while(e > 0) { if(e&1) res = res * base % mod; base = base * base % mod; e >>= 1; }
  return res;
}
template<typename T, typename S> T expo(T b, S e){if(e <= 1)return e == 0?1: b;\
  return (e&1) == 0?expo((b*b), e>>1): (b*expo((b*b), e>>1));}
template<typename T, typename S> T modinv(T a, S mod) { return expo(a, mod-2, mod); }
#define TRACE

#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
  cerr << name << " : " << arg1 << std::endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
  const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<"  ";__f(comma+1, args...);
}
#else
#define trace(...)
#endif

#define mod 1000000007ll
#define what_is(x) cout<<#x<<" is "<<x<<'\n'



int main(){
  freopen("E:\\input.txt", "r", stdin);
  freopen("E:\\output.txt", "w", stdout);
  int t, k, n;
  string s;
  cin >> t;
  REP1(test, t){
    cin >> s >> k;
    cout << "Case #" << test << ": ";
    n = SZ(s);
    int no = 0,  ans = 0,  i =  0, si, f, oi;
    while(i < n){
      while(i < n && s[i] == '+') i++;
      si = i, f = 1, oi = i + k;
      if(i < n) ans++;
      if(i < n && si + k > n)  {no = 1;
      break;
      }
      while(i < si + k && i < n){
        if(s[i] == '+'){
          s[i] = '-';
          if(f) f = 0, oi = i;
        }
        else s[i] = '+';
        i++;
      }
      i = min(oi, si + k);
    }
    //REP(i, n) trace(s[i]);
    if(no) cout << "IMPOSSIBLE\n";
    else cout << ans << "\n";

  }
  return 0;
}
/** remove file IO***/





