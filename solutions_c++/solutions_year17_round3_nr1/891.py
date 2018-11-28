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
const double eps = 1e-7;
const double PI = acos(-1.0);
const int maxn = 1005;
pair<LL,LL> p[maxn];
int n, K;

inline int dcmp(double x) {
	if (fabs(x) < eps)
		return 0;
	return x>0 ? 1:-1;
}

void solve() {
	double ans = 0.0, tmp;
	LL tot = 0;
	priority_queue<LL, vector<LL>, greater<LL> > Q;
	sort(p, p+n);
	
	rep(i, 0, n) {
		if (i >= K-1) {
			tmp = PI * p[i].fir * p[i].fir + 2.0 * PI * (tot + p[i].fir*p[i].sec);
			// printf("tmp = %.2lf\n", tmp);
			if (dcmp(tmp-ans) > 0)
				ans = tmp;
		}
		tot += p[i].fir * p[i].sec;
		Q.push(p[i].fir * p[i].sec);
		while (Q.size() >= K) {
			tot -= Q.top();
			Q.pop();
		}
	}
	
	printf("%.10lf\n", ans);
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	// #ifndef ONLINE_JUDGE
		// freopen("data.in", "r", stdin);
		// freopen("data.out", "w", stdout);
	// #endif
	
	int t;
	
	scanf("%d", &t);
	rep(tt, 1, t+1) {
		scanf("%d %d", &n, &K);
		rep(i, 0, n)
			scanf("%I64d %I64d", &p[i].fir, &p[i].sec);
		printf("Case #%d: ", tt);
		solve();
	}
	
	// #ifndef ONLINE_JUDGE
		// printf("time = %ldms.\n", clock());
	// #endif
	
	return 0;
}
