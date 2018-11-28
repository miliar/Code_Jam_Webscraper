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

void print_ans(int test, ld ans) {
	cout << "Case #" << test << ": " << ans << '\n';
	return;
}
const ld pi = acosl(-1);
ld get_area(ld r) {
	return pi * r * r;
}
ld get_area(ld r, ld h) {
	return pi * 2 * r * h;
}
pii ar[1010];
ld dp[1010][1010];
int cmp (pii a, pii b) {
	return a.first > b.first || a.first == b.first && a.second > b.second;
}
void upd(ld &a, ld b) {
	a = max(a, b);
	return;
}

int main() {
	cin.sync_with_stdio(false);
	cin.tie(0);

	freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
	//freopen("delicious.in", "r", stdin);freopen("delicious.out", "w", stdout);
	cout.precision(20);
	cout << fixed;
	int t;
	cin >> t;
	for (int test = 1; test <= t; ++test) {
		int n, k;
		cin >> n >> k;
		forn(i, n)
			cin >> ar[i].first >> ar[i].second;
		memset(dp, 0, sizeof(dp));
		sort(ar, ar + n, cmp);
		forn(i, n) {
			dp[1][i] = get_area(ar[i].first, ar[i].second) + get_area(ar[i].first);
		}
		forn(i, n) {
			if (i)
				upd(dp[1][i], dp[1][i - 1]);
		}
		for (int q = 2; q <= k; ++q) {
			forn(i, n) {
				if (!i)
					continue;
				upd(dp[q][i], dp[q][i - 1]);
				upd(dp[q][i], dp[q - 1][i - 1] + get_area(ar[i].first, ar[i].second));
			}
		}
		print_ans(test, dp[k][n - 1]);
	}

	return 0;
}