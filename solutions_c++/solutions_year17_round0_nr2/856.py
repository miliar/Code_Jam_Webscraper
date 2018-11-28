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
char s[105];
int n;

bool judge(int x) {
	sprintf(s, "%d", x);
	int len = strlen(s);
	
	for (int i=1; i<len; ++i) {
		if (s[i] < s[i-1])
			return false;
	}
	
	return true;
}

bool judge(char *s) {
	int len = strlen(s);
	
	for (int i=1; i<len; ++i) {
		if (s[i] < s[i-1])
			return false;
	}
	
	return true;
}

void solve() {
	if (judge(s)) {
		printf("%s\n", s);
		return ;
	}
	
	int len = strlen(s), i, j, k;
	
	for (i=0; i<len; ++i) {
		if (s[i] > s[i+1])
			break;
	}
	
	for (j=i; j>=0; --j) {
		if (j==0 || s[j]>s[j-1]) {
			--s[j];
			break;
		}
	}
	
	for (k=j+1; k<len; ++k)
		s[k] = '9';
	
	k = 0;
	while (k<len && s[k]=='0') ++k;
	
	assert(judge(s+k));
	printf("%s\n", s+k);
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
		scanf("%s", s);
		printf("Case #%d: ", tt);
		solve();
	}
	
	// #ifndef ONLINE_JUDGE
		// printf("time = %ldms.\n", clock());
	// #endif
	
	return 0;
}
