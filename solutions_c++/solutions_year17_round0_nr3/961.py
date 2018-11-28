//@ Including Header
// Name : ChouUn's Standard Library 纸农の标准库
// Copyright : fateud.com
#ifndef CSL_STD_H_
#define CSL_STD_H_ 20151122L
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef std::pair< int, int > pii;
typedef std::vector< int > vi;
typedef std::vector< vi > vvi;
typedef std::vector< pii > vpii;

#define rep(i,a,b) for(auto i=a,i##_n=b;i<i##_n;++i)
#define per(i,a,b) for(auto i=b,i##_n=a;i-->i##_n;)
#define endl '\n'

template <class T> void umax(T& a, const T& b) { if (b > a) a = b; }
template <class T> void umin(T& a, const T& b) { if (b < a) a = b; }

#endif /* CSL_STD_H_ */

/**
 *  Name : std.cpp
 *  Date : 2017年4月8日 下午2:21:03
 *  Copyright : fateud.com
 *  Anti-Mage : The magic ends here.
 */

//@ Main Function
int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  int _, __ = 1;
  for(std::cin >> _; _; --_, ++__) {
    std::cout << "Case #" << __ << ": ";
  	ll n; ll k; cin >> n >> k;
  	map<ll, ll> m; m[n + 1] = 1;
  	for (--k; k; ) {
  		auto it = --m.end();
  		ll a = it->first;
  		ll b = min(k, it->second);

  		m[a / 2] += b, m[a - a / 2] += b;
  		k -= b, it->second -= b;
  		if (it->second == 0) m.erase(it);
  	}
  	ll ans = (--m.end())->first;
  	cout << (ans + 1) / 2 - 1 << " " << ans / 2 - 1 << endl;
  }
  return 0;
}
