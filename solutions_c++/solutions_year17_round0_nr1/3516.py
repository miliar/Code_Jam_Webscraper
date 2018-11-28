/********************************************************************
  >  Author: fujiaozhu
  >  File Name: 1.cc
  >  Mail: gaopengyong.code@gmail.com
  >  Created Time: Sat 08 Apr 2017 09:17:24 AM CST
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

int t, k;
string s;

void solve() {
	int ret = 0;
	bool flag = true;
	for (int i = 0; i < (int)s.size(); i++) {
		if (s[i] == '-') {
			if (i + k > (int)s.size()) {
				flag = false;
				break;
			}
			ret ++;
			for (int j = 0; j < k; j++) {
				if (s[i + j] == '+') s[i + j] = '-';
				else s[i + j] = '+';
			}
		}
	}
	if (flag) cout << ret << endl;
	else cout << "IMPOSSIBLE" << endl;
}

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> s >> k;
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
	return 0;
}
