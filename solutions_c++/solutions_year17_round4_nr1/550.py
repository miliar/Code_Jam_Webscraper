/********************************************************************
  >  Author: fujiaozhu
  >  File Name: A.cc
  >  Mail: gaopengyong.code@gmail.com
  >  Created Time: Sat 13 May 2017 10:07:33 PM CST
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

const int mx = 105;

int T, N, P, a[mx];

void solve() {
	int ret = 0;
	if (P == 2) {
		int cnt = 0;
		for (int i = 0; i < N; i++)
			if (a[i] % 2) cnt ++;
		ret = cnt / 2 + N - cnt;
		if (cnt % 2 == 1)
			ret ++;
	}
	else if (P == 3) {
		int c1 = 0, c2 = 0;
		for (int i = 0; i < N; i++) {
			if (a[i] % 3 == 1) c1 ++;
			else if (a[i] % 3 == 2) c2 ++;
		}
		ret = min(c1, c2) + N - c1 - c2;
		int tmp = max(c1, c2) - min(c1, c2);
		ret += tmp / 3;
		if (tmp % 3)
			ret ++;
	}
	else {
		int c1 = 0, c2 = 0, c3 = 0;
		for (int i = 0; i < N; i++) {
			if (a[i] % 4 == 1) c1 ++;
			else if (a[i] % 4 == 2) c2 ++;
			else if (a[i] % 4 == 3) c3 ++;
		}
		ret = N - c1 - c2 - c3;
		ret += c2 / 2;
		ret += min(c1, c3);
		int tmp = max(c1, c3) - min(c1, c3);
		if (c2 % 2 == 0) {
			ret += (tmp + 3) / 4;
		}
		else {
			if (tmp >= 2) ret = ret + 1 + (tmp + 1) / 4;
			else ret ++;
		}
	}
	cout << ret << endl;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("out", "w", stdout);
	cin >> T;
	for (int cs = 1; cs <= T; cs ++) {
		cin >> N >> P;
		for (int i = 0; i < N; i++) cin >> a[i];
		cout << "Case #" << cs << ": ";
		solve();
	}
	return 0;
}
