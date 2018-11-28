#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <memory.h>
#include <set>
#include <ctime>
#include <map>
#include <cstring>
#include <iterator>
#include <queue>
#include <assert.h>
#include <unordered_set>
#include <bitset>


using namespace std;



#define pb push_back
#define pii pair<int, int>
#define mp make_pair
#define ull unsigned long long
#pragma comment(linker, "/STACK:64000000")
#define null NULL
#define forn(i, n) for (int i = 0; i < (n); ++i)
#define fornr(i, n) for (int i = (n); i >= 0; --i)
#define forab(i, a, b) for (int i = (a); i < (b); ++i)
#define all(a) a.begin(), a.end()

//typedef long double ld;
typedef long double ld;
typedef pair<ld, ld> pldld;
typedef long long ll;
typedef pair<ll, ll> pll;


typedef unsigned int ui;
typedef unsigned char uc;
const int infi = 1e9 + 7;
const ll infl = 2e18 + 7;

/*
const int MAX_MEM = 1e8;
int mpos = 0;
char mem[MAX_MEM];
inline void * operator new ( size_t n ) {
  char *res = mem + mpos;
  mpos += n;
  assert(mpos <= MAX_MEM);
  return (void *)res;
}
inline void operator delete ( void * ) { }

inline void * operator new [] ( size_t ) { assert(0); }
inline void operator delete [] ( void * ) { assert(0); }
*/

void print_ans(int test, int ans) {
	cout << "Case #" << test << ": " << ans << '\n';
	return;
}
int used[2][1440];
int dp[721][721][2];

void upd(int &a, int b) {
	a = min(a, b);
	return;
}

int solve1(int start) {
	memset(dp, 60, sizeof(dp));
	dp[0][0][0] = 0;
	if (used[0][start])
		return infi;
	forn(q, 721) {
		forn(w, 721) {
			int cur = (q + w + start - 1);
			if (cur > 1440)
				cur -= 1440;
			if (cur < 0)
				cur += 1440;
			forn(e, 2) {
				if (e == 0) {
					if (!q)
						continue;
					if (used[0][cur])
						continue;
					upd(dp[q][w][0], dp[q - 1][w][0]);
					upd(dp[q][w][0], dp[q - 1][w][1] + 1);
				}
				else {
					if (!w)
						continue;
					if (used[1][cur])
						continue;
					upd(dp[q][w][1], dp[q][w - 1][1]);
					upd(dp[q][w][1], dp[q][w - 1][0] + 1);
				}
			}
		}
	}
	return min(dp[720][720][0], dp[720][720][1] + 1);
}
int solve2(int start) {
	memset(dp, 60, sizeof(dp));
	dp[0][0][1] = 0;
	if (used[1][start])
		return infi;
	forn(q, 721) {
		forn(w, 721) {
			int cur = (q + w + start - 1);
			if (cur > 1440)
				cur -= 1440;
			if (cur < 0)
				cur += 1440;
			forn(e, 2) {
				if (e == 0) {
					if (!q)
						continue;
					if (used[0][cur])
						continue;
					upd(dp[q][w][0], dp[q - 1][w][0]);
					upd(dp[q][w][0], dp[q - 1][w][1] + 1);
				}
				else {
					if (!w)
						continue;
					if (used[1][cur])
						continue;
					upd(dp[q][w][1], dp[q][w - 1][1]);
					upd(dp[q][w][1], dp[q][w - 1][0] + 1);
				}
			}
		}
	}
	return min(dp[720][720][0] + 1, dp[720][720][1]);
}

int main() {
	cin.sync_with_stdio(false);
	cin.tie(0);

	freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
	//freopen("delicious.in", "r", stdin);freopen("delicious.out", "w", stdout);
	int t;
	cin >> t;
	for (int test = 1; test <= t; ++test) {
		int n, m;
		cin >> n >> m;
		memset(used, 0, sizeof(used));
		forn(i, n) {
			int l, r;
			cin >> l >> r;
			for (int j = l; j < r; ++j)
				used[0][j] = 1;
		}
		forn(i, m) {
			int l, r;
			cin >> l >> r;
			for (int j = l; j < r; ++j)
				used[1][j] = 1;
		}
		int ans = infi;
		int a = solve1(0);
		int b = solve2(0);
		ans = min(a, b);
		print_ans(test, ans);
	//	cerr << "test: " << test << '\n' << 1.0 * clock() / CLOCKS_PER_SEC << endl;
	}

	return 0;
}