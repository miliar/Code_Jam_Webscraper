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
ld ar[100];

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
		ld s;
		cin >> s;
		forn(i, n) {
			cin >> ar[i];
		}
		int cnt = 0;
		ld last = 0;
		int i = 0;
		sort(ar, ar + n);
		for (; i < n; ++i) {
			ld d = ar[i]- last;
			ld sum = d * cnt;
			if (sum <= s) {
				s-= sum;
				last = ar[i];
				++cnt;
				continue;
			}
			break;
		}
		if (cnt) {
			s /= cnt;
			last += s;
			s = 0;
		}
		ld ans = 1;
		forn(j, cnt) {
			ans *= last;
		}
		for (; i < n; ++i) {
			ans *= ar[i];
		}
		ans = max(0.0l, ans);
		ans = min(1.0l, ans);
		print_ans(test, ans);
	}

	return 0;
}