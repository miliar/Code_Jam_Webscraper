// In the name of God

#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <deque>
#include <assert.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <stdio.h>
#include <string.h>
#include <utility>
#include <math.h>
#include <bitset>
#include <iomanip>
#include <complex>

using namespace std;

#define rep(i, a, b) for (int i = (a), i##_end_ = (b); i < i##_end_; ++i)
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define SZ(x) (int((x).size()))
#define ALL(x) (x).begin(), (x).end()

template<typename T> inline bool chkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template<typename T> inline bool chkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }
template<typename T> inline bool smin(T &a, const T &b)   { return a > b ? a = b : a;    }
template<typename T> inline bool smax(T &a, const T &b)   { return a < b ? a = b : a;    }

typedef long long LL;

const int N = (int) 1e5 + 5, mod = (int) 0;
int n, p;
int cnt[10], cur[10];
int dp[105][105][105][105];
void go(int pos) {
	if (pos == p) {
		dp[cur[0]][cur[1]][cur[2]][cur[3]] = 0;
		for (int a0 = 0; a0 < p; ++a0) {
			cur[a0]--;
			if (cur[a0] >= 0) {
				int sum = 0;
				for (int j = 0; j < 4; ++j) sum = (sum + cur[j] * j) % p;
				cur[a0]++;
				int &to_upd = dp[cur[0]][cur[1]][cur[2]][cur[3]];	
				cur[a0]--;
				int val = dp[cur[0]][cur[1]][cur[2]][cur[3]] + (sum == 0);
				to_upd = max(to_upd, val);
			}
			cur[a0]++;
		}
		return;
	}
	for (int j = 0; j <= cnt[pos]; ++j) {
		cur[pos] = j;
		go(pos + 1);
	}
}
int a[N];
int main() {
	int tc;
	cin >> tc;
	for (int tt = 1; tt <= tc; ++tt) {
		cin >> n >> p;
		memset(cnt, 0, sizeof cnt);
		for (int j = 0; j < n; ++j) {
			cin >> a[j];
			cnt[a[j] % p]++;
		}
		memset(cur, 0, sizeof cur);
		go(0);
		cout << "Case #" << tt << ": ";
		cout << dp[cnt[0]][cnt[1]][cnt[2]][cnt[3]] << '\n';
	}
}

















