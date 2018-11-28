/********************************************************************
  >  Author: fujiaozhu
  >  File Name: B.cc
  >  Mail: gaopengyong.code@gmail.com
  >  Created Time: Sat 13 May 2017 11:05:10 PM CST
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

const int mx = 1005;

int T, N, C, M;
int cp[mx], cb[mx];

void solve() {
	int r1 = 0, r2 = 0;
	
	for (int i = 1; i <= C; i++)
		r1 = max(r1, cb[i]);
	
	int tmp = 0;
	for (int i = 1; i <= N; i++) {
		tmp += cp[i];
		r1 = max(r1, (tmp + i - 1) / i);
	}
	
	for (int i = 1; i <= N; i++) {
		r2 += max(0, cp[i] - r1);
	}
	cout << r1 << " " << r2 << endl;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("out", "w", stdout);
	cin >> T;
	for (int cs = 1; cs <= T; cs++) {
		cin >> N >> C >> M;
		memset(cp, 0, sizeof(cp));
		memset(cb, 0, sizeof(cb));
		for (int i = 0; i < M; i++) {
			int p, b;
			cin >> p >> b;
			cp[p] ++;
			cb[b] ++;
		}
		cout << "Case #" << cs << ": ";
		solve();
	}
	return 0;
}
