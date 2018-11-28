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

const int N = 33;
const int M = 11;
const int K = 1050;
const int inf = 1000100100;

int dst[N][N], t[N][N];
char s[N][N];
vi infl[N][N];
int can[K][M][M];

int vis[K][K], dp[K][K];
pii prv[K][K];

int dx[4] = {0,1,0,-1}, dy[4] = {1,0,-1,0};

int r,c,m;
int snum, tnum;
map<pii,int> sold, turr;

void bfs(int x, int y, int mask) {
	FOR(i,r) FOR(j,c) dst[i][j] = inf;
	dst[x][y] = 0;
	queue<int> q;
	q.push(x);
	q.push(y);
	while (!q.empty()) {
		int ax = q.front(); q.pop();
		int ay = q.front(); q.pop();
		if (t[ax][ay] == 2) continue;
		FOR(k,4) {
			int bx = ax+dx[k], by = ay+dy[k];
			if (bx<0 || by<0 || bx>=r || by>=c) continue;
			if (t[bx][by] == 1) continue;
			if (t[bx][by] == 2) {
				dst[bx][by] = min(dst[bx][by], dst[ax][ay] + 1);
				continue;
			}
			if (dst[bx][by] > dst[ax][ay] + 1) {
				dst[bx][by] = dst[ax][ay] + 1;
				q.push(bx);
				q.push(by);
			}
		}
	}
	int id = sold[mp(x,y)];
	FOR(i,r) FOR(j,c) if (dst[i][j] <= m) {
		FOR(k,SZ(infl[i][j])) can[mask][id][infl[i][j][k]] = 1;
	}
}

int rec(int tmask, int smask) {
	if (vis[tmask][smask]) return dp[tmask][smask];
	vis[tmask][smask] = 1;
	FOR(i,snum) if (smask & (1<<i)) FOR(j,tnum) if (can[tmask][i][j]) {
		int cur = rec(tmask ^ (1<<j), smask ^ (1<<i)) + 1;
		if (cur > dp[tmask][smask]) {
			dp[tmask][smask] = cur;
			prv[tmask][smask] = mp(i,j);
		}
	}
	return dp[tmask][smask];
}

void test() {
	scanf("%d%d%d", &c, &r, &m);
	FOR(i,r) scanf("%s", s[i]);
	snum=tnum=0;
	sold.clear(); turr.clear();
	FOR(i,r) FOR(j,c) {
		if (s[i][j] == 'S') sold[mp(i,j)] = snum++;
		if (s[i][j] == 'T') turr[mp(i,j)] = tnum++;
	}
	FOR(i,1<<tnum) FOR(j,1<<snum) vis[i][j] = dp[i][j] = 0;
	FOR(mask, (1<<tnum)) {
		FOR(i,snum) FOR(j,tnum) can[mask][i][j] = 0;
		FOR(i,r) FOR(j,c) infl[i][j].clear();
		FOR(i,r) FOR(j,c) {
			t[i][j] = 0;
			if (s[i][j]=='#') t[i][j] = 1;
		}
		FOR(i,r) FOR(j,c) if (s[i][j] == 'T' && (mask & (1<<turr[mp(i,j)]))) {
			int id = turr[mp(i,j)];
			t[i][j] = 2;
			infl[i][j].pb(id);
			FOR(k,4) {
				for (int l = 1; i+l*dx[k] < r && j+l*dy[k] < c && i+l*dx[k] >= 0 && j+l*dy[k] >= 0; l++) {
					if (s[i+l*dx[k]][j+l*dy[k]] == '#') break;
					t[i+l*dx[k]][j+l*dy[k]] = 2;
					infl[i+l*dx[k]][j+l*dy[k]].pb(id);
				}
			}
		}
		FOR(i,r) FOR(j,c) if (s[i][j] == 'S') {
			bfs(i,j, mask);
		}
	}
	int tm = (1<<tnum)-1, sm = (1<<snum)-1;
	rec(tm, sm);
	printf("%d\n", dp[tm][sm]);
	while (dp[tm][sm]) {
		pii cc = prv[tm][sm];
		tm ^= 1<<cc.se;
		sm ^= 1<<cc.fi;
		printf("%d %d\n", cc.fi+1, cc.se+1);
	}
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
