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
  LL t, n, i;
  cin >> t;
  REP1(test, t){
    cin >> n;
    vector<int> dig;
    while(n){
      dig.PB(n%10);
      n /= 10;
    }
    reverse(all(dig));
    while(1){
      i = 0, n = SZ(dig);
      while(i < n - 1){
        if(dig[i] > dig[i + 1]) break;
        else i++;
      }
      if(i < n - 1){
        if(dig[i] == 1 && i == 0){
          dig.erase(dig.begin());
          i = 0;
          while(i < n - 1)  dig[i++] = 9;
        }
        else{
          dig[i]--;
          i++;
          while( i < n) dig[i++] = 9;
        }
      }
      else break;
    }
    cout << "Case #" << test << ": ";
    for(auto it : dig)  cout << it;
    cout << "\n";
  }
  return 0;
}
/** remove file IO***/





