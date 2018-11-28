


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
#define vi vector<int>
#define v(a) vector<a>

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
	++ans;
	cout << "Case #" << test << ": " << ans << '\n';
	return;
}
int cnt[4];
int check(int a, int b, int c) {
	return a <= cnt[1] && b <= cnt[2] && c <= cnt[3];
}


int main() {
	cin.sync_with_stdio(false);
	cin.tie(0);

	freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
	//freopen("delicious.in", "r", stdin);freopen("delicious.out", "w", stdout);
	int qwe;
	cin >> qwe;
	forn(test, qwe) {
		int n, p;
		cin >> n >> p;
		forn(i, p)
			cnt[i] =0 ;
		forn(i, n) {
			int a;
			cin >> a;
			cnt[a % p]++;
		}
		int ans;
		if (p == 2) {
			ans = cnt[0] + cnt[1] / 2;
			if (cnt[1] % 2 == 0)
				--ans;
		}
		else if (p == 3) {
			ans = cnt[0];
			int q = -infi;
			forn(i, 101) {
				if (i > cnt[1] || i > cnt[2])
					break;
				int a = cnt[1] - i, b = cnt[2] - i;
				int c = i + a / 3 + b / 3;
				int d = a % 3 + b % 3;
				if (!d)
					--c;
				q = max(q, c);
			}
			ans += q;
		}
		else {
			ans = cnt[0];
			int res = -infi;
			forn(i, 101) {
				forn(j, 101) {
					forn(k, 101) {
						int a, b, c;
						a = b = c = 0;
						a += i, c += i;
						a += j * 2, b += j;
						b += k;
						c += k * 2;
						if (!check(a, b, c))
							continue;
						int sum = i + j + k;
						a = cnt[1] - a, b = cnt[2] - b, c = cnt[3] - c;
						sum += a / 4 + b / 2 + c / 4;
						int ost = a % 4 + b % 2 + c % 4;
						if (!ost)
							sum--;
						res = max(res, sum);
					}
				}
			}
			ans += res;
		}
		print_ans(test + 1, ans);
	}

	return 0;
}

