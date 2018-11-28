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
 *  Date : 2017年5月13日 下午10:00:08
 *  Copyright : fateud.com
 *  Anti-Mage : The magic ends here.
 */

const int N = 110;

int f[N][N];
int dfs1(int x, int y) {
	if (~f[x][y]) return f[x][y];
	int& res = f[x][y] = 0;
	if (x >= 3) umax(res, dfs1(x - 3, y));
	if (y >= 3) umax(res, dfs1(x, y - 3));
	if (x >= 1 && y >= 1) umax(res, dfs1(x - 1, y - 1));
	if (x > 0 || y > 0) ++res;
	return res;
}

int g[N][N][N];
int dfs2(int x, int y, int z) {
	if (~g[x][y][z]) return g[x][y][z];
	int& res = g[x][y][z] = 0;
	if (x >= 4) umax(res, dfs2(x - 4, y, z));
	if (y >= 2) umax(res, dfs2(x, y - 2, z));
	if (z >= 4) umax(res, dfs2(x, y, z - 4));
	if (x >= 2 && y >= 1) umax(res, dfs2(x - 2, y - 1, z));
	if (x >= 1 && z >= 1) umax(res, dfs2(x - 1, y, z - 1));
	if (y >= 1 && z >= 2) umax(res, dfs2(x, y - 1, z - 2));
	if (x > 0 || y > 0 || z > 0) ++res;
	return res;
}

//@ Main Function
int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);

  memset(f, 0xff, sizeof f);
  memset(g, 0xff, sizeof g);

  int _, __ = 1;
  for(std::cin >> _; _; --_, ++__) {
    std::cout << "Case #" << __ << ": ";
  	int n, p; cin >> n >> p;
  	vi v(p, 0);
  	rep(i, 0, n) {
  		int x; cin >> x;
  		++v[x % p];
  	}
  	if (p == 2) {
  		cout << v[0] + v[1] / 2 + v[1] % 2 << endl;
  	} else if (p == 3) {
  		cout << dfs1(v[1], v[2]) + v[0] << endl;
  	} else {
  		cout << dfs2(v[1], v[2], v[3]) + v[0] << endl;
  	}
  }
  return 0;
}
