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

const int N = 111;
const ll inf = 10001001001001001LL;

int hd[N], hs[N];
ll d[N][N];
double c[N][N];

void test() {
	int n,q;
	scanf("%d%d", &n, &q);
	FOR(i,n) scanf("%d%d", &hd[i], &hs[i]);
	FOR(i,n) FOR(j,n) scanf("%d", &d[i][j]);
	FOR(i,n) FOR(j,n) if (d[i][j] == -1) d[i][j] = inf;
	FOR(k,n) FOR(i,n) FOR(j,n) {
		if (d[i][j] > d[i][k] + d[k][j]) {
			d[i][j] = d[i][k] + d[k][j];
		}
	}
	FOR(i,n) FOR(j,n) {
		if (d[i][j] <= hd[i]) c[i][j] = 1.0 * d[i][j] / hs[i];
		else c[i][j] = inf;
	}
	FOR(k,n) FOR(i,n) FOR(j,n) {
		if (c[i][j] > c[i][k] + c[k][j]) {
			c[i][j] = c[i][k] + c[k][j];
		}
	}
	FOR(i,q) {
		int u,v;
		scanf("%d%d", &u, &v);
		u--; v--;
		printf("%.8lf ", c[u][v]);
	}
	printf("\n");
}

int main() {
	int ttn;
	scanf("%d", &ttn);
	FORI(i,ttn) {
		printf("Case #%d: ", i);
		test();
	}
	return 0;
}
