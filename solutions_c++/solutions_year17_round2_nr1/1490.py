#include <bits/stdc++.h>
#define LL long long
#define FOR(i,c) for(__typeof(c.begin()) i = c.begin(); i != c.end(); i++)
#define F first
#define S second
using namespace std;

const LL mod = 1e9 + 7;

template<typename T> T gcd(T a, T b) { return b == 0?a: gcd(b, a % b); }
template<typename T> T LCM(T a, T b) { return a*(b/gcd(a, b)); }
template<typename T> T expo(T base, T e, T mod) { T res = 1;
  while(e > 0) { if(e&1) res = res * base % mod; base = base * base % mod; e >>= 1; }
  return res;
}
template<typename T, typename S> T expo(T b, S e){if(e <= 1)return e == 0?1: b;\
	return (e&1) == 0?expo((b*b), e>>1): (b*expo((b*b), e>>1));}
template<typename T, typename S> T modinv(T a, S mod) { return expo(a, mod-2, mod); }
template<class T, class S> std::ostream& operator<<(std::ostream &os, const std::pair<T, S> &t) {
	os<<"("<<t.first<<", "<<t.second<<")";
	return os;
}
template<class T> std::ostream& operator<<(std::ostream &os, const std::vector<T> &t) {
	os<<"["; FOR(it,t) { if(it != t.begin()) os<<", "; os<<*it; } os<<"]";
	return os;
}
int main() {
  ios_base::sync_with_stdio(false);
  int t;
  cin >> t;
  for(int tc = 1; tc <= t; tc++) {
    LL n;
    double d;
    cin >> d >> n;
    double k, s;
    double res = -1.0l;
    for(int i = 0; i < n; i++) {
      cin >> k >> s;
      if(i == 0) {
        res = s/(1.0 - (k/d));
      } else {
        res = min(res, s/(1.0 - (k/d)));
      }
    }
    cout << "Case #" << tc << ": " << setprecision(6) << fixed << res << '\n';
  }
  return 0;
}
