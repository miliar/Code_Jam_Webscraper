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
 *  Name : B.cpp
 *  Date : 2017年5月13日 下午10:52:45
 *  Copyright : fateud.com
 *  Anti-Mage : The magic ends here.
 */

const int M = 1010;
int p[M], b[M];

//@ Main Function
int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  int _, __ = 1;
  for(std::cin >> _; _; --_, ++__) {
    std::cout << "Case #" << __ << ": ";
  	int n, c, m; cin >> n >> c >> m;
  	rep(i, 0, m) cin >> p[i] >> b[i];

  	vi u, v;
  	rep(i, 0, m) (b[i] == 1 ? u : v).push_back(p[i]);
  	int x = count(u.begin(), u.end(), 1);
  	int y = count(v.begin(), v.end(), 1);
  	int ans = max(max((int)u.size(), (int)v.size()), x + y);
  	cout << ans << " ";

  	int cnt = 0;
  	rep(i, 2, n + 1) {
  		int x = count(p, p + m, i);
  		cnt += max(0, x - ans);
  	}
  	cout << cnt << endl;

  	/*
    sort(u.begin(), u.end(), greater<int>());
    sort(v.begin(), v.end(), greater<int>());
  	u.resize(u.size() - x);
  	v.resize(v.size() - y);
  	reverse(u.begin(), u.end());
  	reverse(v.begin(), v.end());
  	vi w;
  	std::set_intersection(u.begin(), u.end(), v.begin(), v.end(), back_inserter(w));
  	cout << w.size() << endl;
  	*/
  }
  return 0;
}
