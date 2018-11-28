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
 *  Name : C.cpp
 *  Date : 2017年4月30日 下午5:51:00
 *  Copyright : fateud.com
 *  Anti-Mage : The magic ends here.
 */

const int N = 100;
int a[N];

int read() {
	double x; cin >> x;
	return int(round(x * 10000) + 1e-6);
}

//@ Main Function
int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  int _, __ = 1;
  for(std::cin >> _; _; --_, ++__) {
    std::cout << "Case #" << __ << ": ";
  	int n, k; cin >> n >> k;
  	int s = read();
  	rep(i, 0, n) a[i] = read();

  	if (n == k) {
  		while (s--) *min_element(a, a + n) += 1;
  		double ans = 1;
  		rep(i, 0, n) ans *= a[i] / 10000.;
  		cout << fixed << setprecision(8) << ans << endl;
  	}
  }
  return 0;
}
