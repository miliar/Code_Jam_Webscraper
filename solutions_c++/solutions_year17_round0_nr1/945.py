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
 *  Date : 2017年4月8日 下午12:36:50
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
  	string s; cin >> s;
  	int k; cin >> k;
  	int n = s.size();

  	int ans = 0;
  	rep(i, 0, n - k + 1) {
  		if (s[i] == '+') continue;
  		rep(j, i, i + k) s[j] = s[j] == '-' ? '+' : '-';
  		++ans;
  	}
  	rep(i, n - k + 1, n) if (s[i] == '-') ans = -1;
  	if (ans == -1) cout << "IMPOSSIBLE" << endl;
  	else cout << ans << endl;
  }
  return 0;
}
