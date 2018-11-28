/********************************************************************
  >  Author: fujiaozhu
  >  File Name: 2.cc
  >  Mail: gaopengyong.code@gmail.com
  >  Created Time: Sat 08 Apr 2017 09:43:37 AM CST
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

bool check(string s) {
	for (int i = 1; i < (int)s.size(); i++) {
		if (s[i] < s[i - 1]) return false;
	}
	return true;
}

void solve(string s) {
	while (!check(s)) {
		for (int i = 1; i < (int)s.size(); i++) {
			if (s[i] < s[i - 1]) {
				s[i - 1] --;
				for (int j = i; j < (int)s.size(); j++)
					s[j] = '9';
				break;
			}
		}
	}
	if ((int)s.size() == 1) cout << s << endl;
	else {
		for (int i = 0; i < (int)s.size(); i++) {
			if (s[i] != '0') {
				cout << s.substr(i) << endl;
				break;
			}
		}
	}
}

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int t;
	string s;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> s;
		cout << "Case #" << i + 1 << ": ";
		solve(s);
	}
	return 0;
}
