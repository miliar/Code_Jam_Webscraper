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
 *  Date : 2017年4月30日 下午6:09:22
 *  Copyright : fateud.com
 *  Anti-Mage : The magic ends here.
 */

const int N = 1500;
const int M = 1440;
int n, m;
bool a[N][2];
int dp[N / 2][N / 2][2];

void update(int &a, int b) {
	if (b == -1) return;
	if (a != -1) umin(a, b); else a = b;
}

int solve(int who) {
	memset(dp, 0xff, sizeof dp);
	dp[0][0][who] = 0;

	rep(k, 0, M) {
		rep(i, 0, k + 1) {
			int j = k - i;
			if (i > M / 2) continue;
			if (j > M / 2) continue;

			if (~dp[i][j][0]) umin(dp[i][j][1], dp[i][j][0] + 1);
			if (~dp[i][j][1]) umin(dp[i][j][0], dp[i][j][1] + 1);

			if (a[k][0] && ~dp[i][j][0]) {
				update(dp[i + 1][j][0], dp[i][j][0]);
				update(dp[i + 1][j][1], dp[i][j][0] + 1);
			}
			if (a[k][1] && ~dp[i][j][1]) {
				update(dp[i][j + 1][0], dp[i][j][1] + 1);
				update(dp[i][j + 1][1], dp[i][j][1]);
			}
		}
	}

//  cout << endl;
//  rep(i, 0, 20) { rep(j, 0, 20) cout << dp[i][j][0] << " "; cout << endl; }
//  cout << endl;
//  rep(i, 0, 20) { rep(j, 0, 20) cout << dp[i][j][1] << " "; cout << endl; }
//  cout << endl;
//	cout << dp[M / 2][M / 2][0] << " " << dp[M / 2][M / 2][1] << endl;

	int ans = -1;
	rep(i, 0, 2) {
		if (!a[0][i]) continue;
		rep(j, 0, 2) {
			if (~dp[0][0][i] && ~dp[M / 2][M / 2][j]) {
				update(ans, dp[0][0][i] + dp[M / 2][M / 2][j] + (i != j));
			}
		}
	}
	return ans;
	/*
	rep(k, 1, M + 1) {
		rep(i, 0, k + 1) {
			int j = k - i;
			if (i > M / 2) continue;
			if (j > M / 2) continue;
			if (i) {
				if (~dp[i - 1][j][0]) {
					if (a[k][0]) update(dp[i][j][0], dp[i - 1][j][0]);
					if (a[k][1]) update(dp[i][j][1], dp[i - 1][j][0] + 1);
				}
				if (~dp[i - 1][j][1]) {
					if (a[k][0]) update(dp[i][j][0], dp[i - 1][j][1] + 1);
					if (a[k][1]) update(dp[i][j][1], dp[i - 1][j][1]);
				}
			}
			if (j) {
				if (~dp[i][j - 1][0]) {
					if (a[k][0]) update(dp[i][j][0], dp[i][j - 1][0]);
					if (a[k][1]) update(dp[i][j][1], dp[i][j - 1][0] + 1);
				}
				if (~dp[i][j - 1][1]) {
					if (a[k][0]) update(dp[i][j][0], dp[i][j - 1][1] + 1);
					if (a[k][1]) update(dp[i][j][1], dp[i][j - 1][1]);
				}
			}
		}
	}
  cout << endl;
  rep(i, 0, M / 2 + 1) { rep(j, 0, M / 2 + 1) cout << dp[i][j][0] << " "; cout << endl; }
  cout << endl;
  rep(i, 0, M / 2 + 1) { rep(j, 0, M / 2 + 1) cout << dp[i][j][1] << " "; cout << endl; }
  cout << endl;
	cout << dp[M / 2][M / 2][0] << " " << dp[M / 2][M / 2][1] << endl;
*/
}

//@ Main Function
int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  int _, __ = 1;
  for(std::cin >> _; _; --_, ++__) {
    std::cout << "Case #" << __ << ": ";
  	memset(a, true, sizeof a);

  	cin >> n >> m;
  	rep(i, 0, n) {
  		int x, y; cin >> x >> y;
  		rep(j, x, y) a[j][0] = false;
  	}
  	rep(i, 0, m) {
  		int x, y; cin >> x >> y;
  		rep(j, x, y) a[j][1] = false;
  	}
  	a[M][0] = a[0][0];
  	a[M][1] = a[0][1];

  	int ans = -1;
  	update(ans, solve(0));
  	update(ans, solve(1));
  	cout << ans << endl;
  }
  return 0;
}
