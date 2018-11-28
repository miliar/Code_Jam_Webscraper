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
 *  Name : A.cpp
 *  Date : 2017年4月23日 上午12:11:21
 *  Copyright : fateud.com
 *  Anti-Mage : The magic ends here.
 */

const int N = 1010;
double a[N];

//@ Main Function
int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  int _, __ = 1;
  for(std::cin >> _; _; --_, ++__) {
    std::cout << "Case #" << __ << ": ";
  	ll d; cin >> d;
  	int n; cin >> n;
  	rep(i, 0, n) {
  		ll k, s; cin >> k >> s;
  		a[i] = d / (((double)d - k) / s);
  	}
  	cout << fixed << setprecision(7) << *min_element(a, a + n) << endl;
  }
  return 0;
}
