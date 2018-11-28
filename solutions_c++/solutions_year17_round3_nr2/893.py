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

#define LOCAL_DEBUG

typedef long long LL;
const int maxn = 105;
const int mod = 1440;
pii cp[maxn], jp[maxn];
int visit[mod+10];
int ac, aj;
int ans;

struct node_t {
	int w, l, r;

	node_t(int w=0, int l=0, int r=0):
		w(w), l(l), r(r) {}

	bool operator< (const node_t& p) const {
		return w < p.w;
	}
};

void init(pii *p, int n) {
	rep(i, 0, n) {
		p[i].sec = (p[i].sec - 1) % mod;
	}
	sort(p, p+n);
}

int token;
bool check(int l, int r) {
	if (l > r) return true;
	rep(i, l, r+1)
		if (visit[i] == -token)
			return false;
	return true;
}

void gao2(pii *cp, int ac, bool f, int& tot) {
	tot = mod / 2;

	rep(i, 0, ac) {
		tot -= (cp[i].sec - cp[i].fir + 1);
	}

	set<node_t> st;

	if (f)
		token = 1;
	else
		token = -1;

	rep(i, 0, ac) {
		if (i == ac-1) {
			int w = (cp[0].fir + mod - 1 - cp[i].sec);
			assert(w>=0 && w<mod);
			bool flag = (w>0) && check(0, cp[0].fir-1) && check(cp[i].sec+1, mod-1);
			if (flag) {
				st.insert(node_t(w, cp[i].sec, cp[0].fir));
			}
		} else {
			int w = cp[i+1].fir - cp[i].sec - 1;
			bool flag = (w>0) && check(cp[i].sec+1, cp[i+1].fir-1);
			if (flag) {
				st.insert(node_t(w, cp[i].sec, cp[i+1].fir));
			}
		}
	}

	while (!st.empty() && tot>=st.begin()->w) {
		node_t nd = *st.begin();
		tot -= nd.w;
		if (nd.l <= nd.r) {
			int l = nd.l + 1;
			int r = nd.r - 1;
			rep(j, l, r+1)
				visit[j] = token;
		} else {
			{// 0->r
				int l = 0;
				int r = nd.r-1;
				rep(j, l, r+1)
					visit[j] = token;
			}
			{// l->mod-1
				int l = nd.l + 1;
				int r = mod - 1;
				rep(j, l, r+1)
					visit[j] = token;
			}
		}
	}
}

void update(bool f, int& tot) {
	if (f)
		token = 1;
	else
		token = -1;

	int i = 0;

	while (i < mod) {
		if (visit[i] != token) {
			++i;
			continue;
		}
		int j = i++;
		while (j<mod && visit[j]==token) ++j;
		int k;

		// endswith i, startswith j
		k = i - 1;
		if (k < 0) k = mod - 1;
		while (tot>0 && visit[k]==0) {
			visit[k] = token;
			--k;
			--tot;
			if (k < 0) k = mod - 1;
		}

		k = j;
		if (k >= mod) k = 0;
		while (tot>0 && visit[k]==0) {
			visit[k] = token;
			i = max(i, k+1);
			++k;
			--tot;
			if (k >= mod) k = 0;
		}

	}

	// if (tot) {
		// rep(j, 0, mod) {
			// if (visit[j] == 0) {
				// visit[j] = token;
				// --tot;
			// }
		// }

		// #ifdef LOCAL_DEBUG
		// if (tot != 0)
			// printf("tot = %d\n", tot);
		// #endif
	// }
}

void gao(pii *cp, int ac, pii *jp, int aj) {
	memset(visit, 0, sizeof(visit));
	int totc, totj;

	rep(i, 0, ac) {
		rep(j, cp[i].fir, cp[i].sec+1) {
			visit[j] = 1;
		}
	}
	rep(i, 0, aj) {
		rep(j, jp[i].fir, jp[i].sec+1) {
			visit[j] = -1;
		}
	}

	gao2(cp, ac, true, totc);
	gao2(jp, aj, false, totj);

	// printf("before: totc = %d, totj = %d\n", totc, totj);
	if (ac > 0) {
		update(true, totc);
		update(false, totj);
	} else {
		update(false, totj);
		update(true, totc);
	}
	// printf("after: totc = %d, totj = %d\n", totc, totj);
	assert(totc==0 || totj==0);
	if (totc == 0) {
		rep(j, 0, mod)
			if (visit[j] == 0)
				visit[j] = -1;
	} else if (totj == 0) {
		rep(j, 0, mod)
			if (visit[j] == 0)
				visit[j] = 1;
	}

	{// calculate
		int tmp = 1, i = 0;

		while (i < mod) {
			int j = i++;
			while (i<mod && visit[i]==visit[j])
				++i;
			// printf("%d: %d %d\n", visit[j], j, i-1);
			if (i >= mod) break;
			++tmp;
		}
		if (visit[0] == visit[mod-1])
			--tmp;

		ans = min(ans, tmp);
	}
}

void solve() {
	if (ac<=1 && aj<=1) {
		puts("2");
		return ;
	}

	init(cp, ac);
	init(jp, aj);

	ans = INT_MAX;
	gao(cp, ac, jp, aj);
	gao(jp, aj, cp, ac);

	printf("%d\n", ans);
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
		freopen("data.in", "r", stdin);
		freopen("data.out", "w", stdout);
	#endif

	int t;

	scanf("%d", &t);
	rep(tt, 1, t+1) {
		scanf("%d %d", &ac, &aj);
		rep(i, 0, ac)
			scanf("%d %d", &cp[i].fir, &cp[i].sec);
		rep(i, 0, aj)
			scanf("%d %d", &jp[i].fir, &jp[i].sec);
		printf("Case #%d: ", tt);
		solve();
	}

	#ifndef ONLINE_JUDGE
		printf("time = %ldms.\n", clock());
	#endif

	return 0;
}
