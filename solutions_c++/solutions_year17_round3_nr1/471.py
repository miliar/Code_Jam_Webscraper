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
// Name : Mathematical Computation 数学计算
// Copyright : fateud.com

#ifndef CSL_MATH_H_
#define CSL_MATH_H_ 20160313L

#include <cmath>
#include <functional>
#include <vector>

#ifndef M_PI
#define M_E        2.71828182845904523536     // - e
#define M_LOG2E    1.44269504088896340736     // - log2(e)
#define M_LOG10E   0.434294481903251827651    // - log10(e)
#define M_LN2      0.693147180559945309417    // - ln(2)
#define M_LN10     2.30258509299404568402     // - ln(10)
#define M_PI       3.14159265358979323846     // - pi
#define M_1_PI     0.318309886183790671538    // - 1/pi
#define M_SQRT2    1.41421356237309504880     // - sqrt(2)
#define M_SQRT1_2  0.707106781186547524401    // - 1/sqrt(2)
#endif /* M_PI */

namespace csl {
  /*
   * greatest common divisor
   */
  template <class T>
  inline T gcd(T a, T b) {
    for (T c = T(); !!b;)
      c = a % b, a = std::move(b), b = std::move(c);
    return a;
  }
  /*
   * extended Euclidean algorithm
   * solve ax + by = gcd(a,b)
   */
  template <class T>
  T gcd(const T& a, const T& b, T& x, T& y) {
    if (!b) return x = 1, y = 0, a;
    T r = gcd(b, a % b, y, x);
    return y = y - a / b * x, r;
  }

  /**
   * least common multiple
   */
  template <class T>
  inline T lcm(const T& a, const T& b) {
    return a / gcd(a, b) * b;
  }

  /**
   * return a * b (mod m)
   */
  template <class V, class E>
  inline V mul(V a, E b, const V m) {
  	V res = V();
  	if (!a || !b) return res;
  	for (; b; b >>= 1, a = (a + a) % m) if (b & 1) res = (res + a) % m;
  	return res;
  }

  /**
   * return c * n ^ k
   */
  template <class V, class K>
  inline V pow(V c, V n, K k) {
  	for (; k; k >>= 1, n = n * n) if (k & 1) c = c * n;
  	return c;
  }

  /**
   * return c * n ^ k (mod m)
   */
  template <class V, class E>
  inline V pow(V c, V n, E k, const V m) {
  	for (c %= m; k; k >>= 1, n = (n * n) % m) if (k & 1) c = (c * n) % m;
  	return c;
  }

  /**
   * return 1 / x (mod m)
   */
  template <class V>
  inline V inv(const V& x, const V& m) {
    V p, q;
    return gcd(x, m, p, q), (p % m + m) % m;
  }

  template <class V>
  inline std::vector< V > divide(V x) {
    std::vector< V > res;
    if (x % 2 == 0) {
      res.push_back(2);
      while (x % 2 == 0)
        x >>= 1;
    }
    for (V i(3); i * i <= x; i += 2) {
      if (x % i) continue;
      res.push_back(i);
      while (x % i == 0)
        x /= i;
    }
    if (x != V(1)) res.push_back(x);
    return res;
  }

  /**
   * return Primitive Root of x about m
   */
  template <class V>
  inline V root(const V& P) {
    std::vector< V > p = csl::divide(P - 1);
    for (V g = 2; g < P; ++g) {
      bool flag = true;
      for (auto i = p.begin(); i != p.end(); ++i)
        if (csl::pow(V(1), g, (P - 1) / *i, P) == 1) {
          flag = false;
          break;
        }
      if (flag) return g;
    }
    return -1;
  }

} // namespace csl

#endif /* CSL_MATH_H_ */

/**
 *  Name : A.cpp
 *  Date : 2017年4月30日 下午4:57:11
 *  Copyright : fateud.com
 *  Anti-Mage : The magic ends here.
 */

const int N = 1010;
typedef pair<ll, ll> pll;
pll p[N];

//@ Main Function
int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  int _, __ = 1;
  for(std::cin >> _; _; --_, ++__) {
    std::cout << "Case #" << __ << ": ";
  	int n, k; cin >> n >> k;
  	rep(i, 0, n) cin >> p[i].first >> p[i].second;

  	sort(p, p + n, [](const pll& a, const pll& b) {
  		return a.first * a.second > b.first * b.second;
  	});

  	double ans = 0;
  	double R = 0;
  	rep(i, 0, k - 1) umax(R, (double)p[i].first);
  	rep(i, k - 1, n) {
    	double r = max(R, (double)p[i].first);
    	double cnt = r * r + 2. * p[i].first * p[i].second;
    	umax(ans, cnt);
  	}
  	rep(i, 0, k - 1) ans += 2. * p[i].first * p[i].second;
  	cout << fixed << setprecision(10) << ans * M_PI << endl;
  }
  return 0;
}
