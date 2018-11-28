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
  int t;
  LL n, k;
  cin >> t;
  REP1(test, t){
    cin >> n >> k;
    priority_queue<LL, vector<LL> >pq;
    pq.push(n);
    cout << "Case #" << test << ": ";
    while(1){
      LL aux = pq.top();
      if(k == 1){
        aux--;
        LL n1 = max(aux/2, aux - aux/2);
        LL n2 = min(aux/2, aux - aux/2);
        cout << n1 << " " << n2;
        break;
      }
      if(aux == 0){
        cout << "0";
        break;
      }
      aux--;
      LL temp = aux/2;
      pq.push(temp);
      pq.push(aux - temp);
      pq.pop();
      k--;
    }
    cout << "\n";
  }
  return 0;
}
/** remove file IO***/





