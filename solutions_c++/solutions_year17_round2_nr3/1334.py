/*  */
#include <iostream>
#include <sstream>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <deque>
#include <bitset>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstring>
#include <climits>
#include <cctype>
#include <cassert>
#include <functional>
#include <iterator>
#include <iomanip>
using namespace std;
//#pragma comment(linker,"/STACK:102400000,1024000")

#define sti				set<int>
#define stpii			set<pair<int, int> >
#define mpii			map<int,int>
#define vi				vector<int>
#define pii				pair<int,int>
#define vpii			vector<pair<int,int> >
#define rep(i, a, n) 	for (int i=a;i<n;++i)
#define per(i, a, n) 	for (int i=n-1;i>=a;--i)
#define clr				clear
#define pb 				push_back
#define mp 				make_pair
#define fir				first
#define sec				second
#define all(x) 			(x).begin(),(x).end()
#define SZ(x) 			((int)(x).size())
#define lson			l, mid, rt<<1
#define rson			mid+1, r, rt<<1|1
#define getBits(x)		__builtin_popcount(x)
#define getBitIdx(x)	__builtin_ffs(x)

typedef long long LL;
const double inf = 1e22;
const int maxn = 105;
int D[maxn][maxn];
int E[maxn], S[maxn];
bool visit[maxn][maxn];
int n, q;

struct node_t {
	int hid, tot;
	int cid;
	double t;
	
	node_t(int hid=0, int tot=0, int cid=0, double t=0.):
		hid(hid), tot(tot), cid(cid), t(t) {}
};

void solve(int st, int ed) {
	double ans = inf;
	memset(visit, false, sizeof(visit));
	queue<node_t> Q;
	node_t nd(0, -2, 0, 0.0), d;
	
	memset(visit, false, sizeof(visit));
	// visit[0][0] = true;
	Q.push(nd);
	
	while (!Q.empty()) {
		d = Q.front();
		Q.pop();
		if (d.cid == n-1) {
			ans = min(d.t, ans);
			continue;
		}
		
		int cid = d.cid, s = S[d.hid];
		int l = D[cid][cid+1];
		if (l == -1)
			continue;
		
		// no swtich horse, iff E[cid]>=curTot && S[cid]>=dS, switch is defintely
		if (d.tot >= l) {
			nd = d;
			nd.t += l*1.0 / s;
			nd.cid += 1;
			nd.tot -= l;
			// if (!visit[nd.cid][nd.hid]) {
				// visit[nd.cid][nd.hid] = true;
				Q.push(nd);
			// }
		}
		
		// switch horse
		if (E[cid] >= l) {
			s = S[cid];
			nd = d;
			nd.t += l*1.0 / s;
			nd.cid += 1;
			nd.hid = cid;
			nd.tot = E[cid] - l;
			// if (!visit[nd.cid][nd.hid]) {
				// visit[nd.cid][nd.hid] = true;
				Q.push(nd);
			// }
		}
	}
	
	printf(" %.10lf", ans);
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	// #ifndef ONLINE_JUDGE
		// freopen("data.in", "r", stdin);
		// freopen("data.out", "w", stdout);
	// #endif
	
	int t;
	int u, v;

	scanf("%d", &t);
	rep(tt, 1, t+1) {
		scanf("%d %d", &n, &q);
		rep(i, 0, n)
			scanf("%d %d", E+i, S+i);
		rep(i, 0, n)
			rep(j, 0, n)
				scanf("%d", &D[i][j]);
		printf("Case #%d:", tt);
		while (q--) {
			scanf("%d %d", &u, &v);
			solve(u, v);
		}
		putchar('\n');
	}
	
	
	// #ifndef ONLINE_JUDGE
		// printf("time = %ldms.\n", clock());
	// #endif
	
	return 0;
}
