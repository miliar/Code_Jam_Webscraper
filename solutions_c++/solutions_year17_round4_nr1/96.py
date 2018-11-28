#include <bits/stdc++.h>
using namespace std;
#define REP(i,a,b) for (int i = (a); i <= (b); ++i)
#define REPD(i,a,b) for (int i = (a); i >= (b); --i)
#define FORI(i,n) REP(i,1,n)
#define FOR(i,n) REP(i,0,int(n)-1)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define vi vector<int>
#define ll long long
#define SZ(x) int((x).size())
#define DBG(v) cerr << #v << " = " << (v) << endl;
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define fi first
#define se second

const int N = 102;

int n,p,tn;
int dp[N][N][N][4], vis[N][N][N][4];

int rec(int c1, int c2, int c3, int r) {
	if (vis[c1][c2][c3][r] == tn) {
		return dp[c1][c2][c3][r];
	}
	vis[c1][c2][c3][r] = tn;
	int ret = 0;
	dp[c1][c2][c3][r] = 0;
	if (c1 > 0) {
		int cur = rec(c1-1, c2, c3, (r+1)%p);
		if (r == 0) cur++;
		if (cur > ret) ret = cur;
	}
	if (c2 > 0) {
		int cur = rec(c1, c2-1, c3, (r+2)%p);
		if (r == 0) cur++;
		if (cur > ret) ret = cur;
	}
	if (c3 > 0) {
		int cur = rec(c1, c2, c3-1, (r+3)%p);
		if (r == 0) cur++;
		if (cur > ret) ret = cur;
	}
	return dp[c1][c2][c3][r] = ret;
}

int c[4];

void test() {
	scanf("%d%d", &n, &p);
	FOR(i,4) c[i] = 0;
	FOR(i,n) {
		int aa;
		scanf("%d", &aa);
		aa %= p;
		c[aa]++;
	}
	int res = c[0];
	printf("%d\n", res + rec(c[1], c[2], c[3], 0));
}

int main() {
	int ttn;
	scanf("%d", &ttn);
	FORI(i,ttn) {
		printf("Case #%d: ", i);
		tn = i;
		test();
	}
	return 0;
}
