/********************************************************************
  >  Author: fujiaozhu
  >  File Name: 3.cc
  >  Mail: gaopengyong.code@gmail.com
  >  Created Time: Sat 08 Apr 2017 10:29:38 AM CST
  >  Start of something new | Do cool things that matters
 *******************************************************************/

#include <bits/stdc++.h>
using namespace std;

#define bits(a)     __builtin_popcount(a)

#define PB          push_back
#define SIZE(x)     (int)x.size()
#define MP(x,y)     make_pair(x,y)
#define All(t)      (t).begin(),(t).end()
#define CLR(x,y)    memset(x,y,sizeof(x))
#define FOR(i,n,m)  for (int i = n; i <= m; i++)
#define ROF(i,n,m)  for (int i = n; i >= m; i--)

#define RI(x)       scanf ("%d", &(x))
#define RII(x,y)    RI(x),RI(y)
#define RIII(x,y,z) RI(x),RI(y),RI(z)

typedef long long ll;
typedef unsigned int ui;
typedef unsigned long long ull;

/***********************END OF DEFINE******************************/

int t, n, k;

void solve_s1() {
	int mxmn, mxmx;
	vector<bool> vis(n, 0);
	vector<int> l(n, 0), r(n, 0);
	vis[0] = vis[n - 1] = 1;
	for (int i = 0; i < k; i++) {
		int pre = 0;
		for (int j = 1; j < n - 1; j++) {
			if (vis[j]) pre = j;
			l[j] = j - pre;
		}
		pre = n - 1;
		for (int j = n - 2; j > 0; j--) {
			if (vis[j]) pre = j;
			r[j] = pre - j;
		}
		int id = 0;
		mxmn = mxmx = 0;
		for (int j = 1; j < n - 1; j++) {
			if (min(l[j], r[j]) > mxmn) {
				mxmn = min(l[j], r[j]);
				mxmx = max(l[j], r[j]);
				id = j;
			}
			else if (min(l[j], r[j]) == mxmn) {
				if (max(l[j], r[j]) > mxmx) {
					mxmx = max(l[j], r[j]);
					id = j;
				}
			}
		}
		vis[id] = 1;
	}
	cout << mxmx - 1 << " " << mxmn - 1 << endl;
}

void solve_s2() {
	n -= 2;
	while (k > 1) {
		if (k & 1) n = (n - 1) >> 1;
		else n >>= 1;
		k >>= 1;
	}
	cout << n / 2 << " " << (n - 1) / 2 << endl;
}

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> n >> k;
		n += 2;
		cout << "Case #" << i + 1 << ": ";
		solve_s2();
	}
	return 0;
}

