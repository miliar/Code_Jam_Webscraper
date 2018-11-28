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

// #define ZYX_DEBUG

typedef long long LL;
const int maxd = 61;
LL n, K;

void solve() {
	set<LL, greater<LL> > Q;
	map<LL, LL> ctb;
	LL tot = 0, L = -1, c = 1, l;
	
	Q.insert(n);
	ctb[n] = 1;
	
	while (!Q.empty()) {
		l = *Q.begin();
		c = ctb[l];
		Q.erase(Q.begin());
		ctb.erase(l);
		tot += c;
		if (K <= tot) {
			L = l;
			break;
		}
		
		if (l & 1) {
			LL k = l / 2;
			if (k > 0) {
				if (Q.count(k) == 0) {
					Q.insert(k);
					ctb[k] = c * 2;
				} else {
					ctb[k] += c * 2;
				}
			}
		} else {
			LL k = l / 2;
			if (k > 0) {
				if (Q.count(k) == 0) {
					Q.insert(k);
					ctb[k] = c;
				} else {
					ctb[k] += c;
				}
			}
			--k;
			if (k > 0) {
				if (Q.count(k) == 0) {
					Q.insert(k);
					ctb[k] = c;
				} else {
					ctb[k] += c;
				}
			}
		}
	}
	
	#ifdef ZYX_DEBUG
	assert(L > 0);
	// printf("L = %I64d\n", L);
	#endif
	
	LL ls, rs;
	
	if (L & 1) {
		ls = rs = L / 2;
	} else {
		ls = L / 2 - 1;
		rs = L / 2;
	}
	
	printf("%I64d %I64d\n", max(ls, rs), min(ls, rs));
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	#ifdef ZYX_DEBUG
		freopen("data.in", "r", stdin);
		freopen("data.out", "w", stdout);
	#endif

	int t;

	scanf("%d", &t);
	rep(tt, 1, t+1) {
		scanf("%I64d %I64d", &n, &K);
		printf("Case #%d: ", tt);
		solve();
	}

	// #ifndef ONLINE_JUDGE
		// printf("time = %ldms.\n", clock());
	// #endif

	return 0;
}
