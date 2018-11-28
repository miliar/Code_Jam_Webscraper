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

#define ZYX_DEBUG

typedef long long LL;

const int maxn = 1005;
char s[maxn];
int K;

void solve() {
	int len = strlen(s);
	int ans = 0;
	
	for (int i=0; i+K<=len; ++i) {
		if (s[i] == '+')
			continue;
		++ans;
		for (int j=0; j<K; ++j)
			s[i+j] = (s[i+j]=='-') ? '+':'-';
	}
	
	for (int i=0; i<len; ++i) {
		if (s[i] != '+') {
			ans = -1;
			break;
		}
	}
	
	if (ans < 0)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n", ans);
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	// #ifdef ZYX_DEBUG
		// freopen("data.in", "r", stdin);
		// freopen("data.out", "w", stdout);
	// #endif
	
	int t;
	
	scanf("%d", &t);
	rep(tt, 1, t+1) {
		scanf("%s %d", s, &K);
		printf("Case #%d: ", tt);
		solve();
	}
	
	// #ifdef ZYX_DEBUG
		// printf("time = %ldms.\n", clock());
	// #endif
	
	return 0;
}
