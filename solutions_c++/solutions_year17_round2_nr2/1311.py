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
const int maxl = 1005;
int ids[128];
char scol[] = "ROYGBV";
int Z[10], n;
char s[maxl];
int l = 0;

void init() {
	int len = strlen(scol);
	
	rep(i, 0, len)
		ids[scol[i]] = i;
}

bool check(char a, char b) {
	if (a=='R' && (b=='R' || b=='O' || b=='V')) 
		return false;
	if (a=='Y' && (b=='Y' || b=='O' || b=='G')) 
		return false;
	if (a=='B' && (b=='B' || b=='G' || b=='V')) 
		return false;
	
	// orange
	if (a=='O' && (b=='R' || b=='O' || b=='V')) 	
		return false;
	if (a=='O' && (b=='Y' || b=='O' || b=='G')) 
		return false;
	// green
	if (a=='G' && (b=='Y' || b=='O' || b=='G')) 
		return false;
	if (a=='G' && (b=='B' || b=='G' || b=='V')) 
		return false;
	// violet
	if (a=='V' && (b=='R' || b=='O' || b=='V')) 
		return false;
	if (a=='V' && (b=='B' || b=='G' || b=='V')) 
		return false;
	
	return true;
}

bool check(char *s) {
	int l = strlen(s);
	
	if (l != n) return false;
	if (!check(s[0], s[l-1])) return false;
	
	for (int i=1; i<n; ++i) {
		if (!check(s[i], s[i-1]))
			return false;
	}
	
	
	return true;
}

bool judge(int a, int b, int c, char aa, char bb, char cc) {
	if (a+b < c-1) return false;
	
	{// case 1
		int xplusy = a + b - (c - 1);
		int x, y;
		l = 0;
		for (x=0; x<=xplusy; ++x) {
			y = xplusy - x;
			if (!(x>=0 && x<=a && y>=0 && y<=b))
				continue;
			
			if (abs(x-y) > 1) continue;
			
			if (x == y) {
				int da = a - x, db = b - y;
				
				for (int i=0; i<c; ++i) {
					s[l++] = cc;
					if (i != c-1) {
						if (da > 0) {
							--da;
							s[l++] = aa;
						} else {
							assert(db > 0);
							--db;
							s[l++] = bb;
						}
					}
				}
				
				for (int i=0; i<x; ++i) {
					s[l++] = aa;
					s[l++] = bb;
				}
				
			} else if (x == y+1) {
				int da = a - x, db = b - y;
				
				for (int i=0; i<c; ++i) {
					s[l++] = cc;
					if (i != c-1) {
						if (da > 0) {
							--da;
							s[l++] = aa;
						} else {
							assert(db > 0);
							--db;
							s[l++] = bb;
						}
					}
				}
				
				for (int i=0; i<y; ++i) {
					s[l++] = aa;
					s[l++] = bb;
				}
				s[l++] = aa;
				
			} else {
				assert(x == y-1);
				
				int da = a - x, db = b - y;
				
				for (int i=0; i<c; ++i) {
					s[l++] = cc;
					if (i != c-1) {
						if (da > 0) {
							--da;
							s[l++] = aa;
						} else {
							assert(db > 0);
							--db;
							s[l++] = bb;
						}
					}
				}
				
				for (int i=0; i<x; ++i) {
					s[l++] = bb;
					s[l++] = aa;
				}
				s[l++] = bb;
			}
			
			s[l] = '\0';
		
			if (check(s)) {
				puts(s);
				return true;
			}
		}
	}
	
	{// case 2
		int xplusy = a + b - c;
		int x, y;
		
		l = 0;
		for (x=0; x<=xplusy; ++x) {
			y = xplusy - x;
			if (!(x>=0 && x<=a && y>=0 && y<=b))
				continue;
			
			if (abs(x-y) > 1) continue;
			
			if (x == y) {
				int da = a - x, db = b - y;
				
				for (int i=0; i<c; ++i) {
					if (da > 0) {
						--da;
						s[l++] = aa;
					} else {
						assert(db > 0);
						--db;
						s[l++] = bb;
					}
					s[l++] = cc;
				}
				
				for (int i=0; i<x; ++i) {
					s[l++] = aa;
					s[l++] = bb;
				}
				
			} else if (x == y+1) {
				int da = a - x, db = b - y;
				
				for (int i=0; i<c; ++i) {
					if (da > 0) {
						--da;
						s[l++] = aa;
					} else {
						assert(db > 0);
						--db;
						s[l++] = bb;
					}
					s[l++] = cc;
				}
				
				for (int i=0; i<y; ++i) {
					s[l++] = aa;
					s[l++] = bb;
				}
				s[l++] = aa;
				
			} else {
				assert(x == y-1);
				
				int da = a - x, db = b - y;
				
				for (int i=0; i<c; ++i) {
					if (da > 0) {
						--da;
						s[l++] = aa;
					} else {
						assert(db > 0);
						--db;
						s[l++] = bb;
					}
					s[l++] = cc;
				}
				
				for (int i=0; i<x; ++i) {
					s[l++] = bb;
					s[l++] = aa;
				}
				s[l++] = bb;
			}
			
			s[l] = '\0';
			if (check(s)) {
				puts(s);
				return true;
			}
		}
	}
	
	return false;
}

void solve() {
	int nR = Z[ids['R']];
	int nY = Z[ids['Y']];
	int nB = Z[ids['B']];
	
	if (judge(nR, nY, nB, 'R', 'Y', 'B') || judge(nY, nR, nB, 'Y', 'R', 'B')) {
		return ;
	}
	if (judge(nR, nB, nY, 'R', 'B', 'Y') || judge(nB, nR, nY, 'B', 'R', 'Y')) {
		return ;
	}
	if (judge(nB, nY, nR, 'B', 'Y', 'R') || judge(nY, nB, nR, 'Y', 'B', 'R')) {
		return ;
	}
	
	puts("IMPOSSIBLE");
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	// #ifndef ONLINE_JUDGE
		// freopen("data.in", "r", stdin);
		// freopen("data.out", "w", stdout);
	// #endif
	
	int t;
	
	init();
	scanf("%d", &t);
	rep(tt, 1, t+1) {
		scanf("%d", &n);
		rep(i, 0, 6)
			scanf("%d", Z+i);
		printf("Case #%d: ", tt);
		solve();
	}
	
	// #ifndef ONLINE_JUDGE
		// printf("time = %ldms.\n", clock());
	// #endif
	
	return 0;
}
