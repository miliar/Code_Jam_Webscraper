#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <utility>
#include <cstdlib>
#include <memory>
#include <queue>
#include <cassert>
#include <cmath>
#include <ctime>
#include <complex>
#include <bitset>
#include <fstream>
#include <unordered_map>
#include <unordered_set>
#include <numeric>

using namespace std;

#define ws ws_____________________
#define y1 y1_____________________
#define y0 y0_____________________
#define left left_________________
#define right right_______________
#define next next_________________
#define prev prev_________________
#define hash hash_________________

#define pb push_back
#define fst first
#define snd second
#define mp make_pair 
#define sz(C) ((int) (C).size())
#define forn(i, n) for (int i = 0; i < int(n); ++i)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; --i)
#define all(C) begin(C), end(C)

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef pair<int,int> pii;
typedef pair<ll, ll> pll;
typedef vector<ll> vll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vii;
typedef long double ld;
typedef complex<double> cd;

#define FILE_NAME "a"


string s;
int k;

bool read() {
	static const int MAXN = 1e3 + 10;
	static char t[MAXN];
	if  (scanf("%s %d\n", t, &k) < 2) {
		return 0;
	}
	s = t;
	return 1;
}



bool solve() {
	const int n = sz(s);
	vi flip(n + 1, 0);
	int ans = 0;
	int pref = 0;
	forn(i, n) {
		pref ^= flip[i];
		int cur = (s[i] == '+') ^ pref;
		if  (!cur) {
			if  (i + k - 1 >= n) {
				return 0;
			}
			if  (i + k < n) {
				flip[i + k] ^= 1;
			}
			pref ^= 1;
			++ans;
		}
	}
	printf("%d\n", ans);
	return 1;
}	

int main() {
#ifdef LOCAL
	freopen(FILE_NAME ".in", "r", stdin);
	freopen(FILE_NAME ".out", "w", stdout);
#endif

	int T;
	scanf("%d\n", &T);
	forn(t, T) {
		assert(read());
		printf("Case #%d: ", t + 1);
		if  (!solve()) {
			puts("IMPOSSIBLE");
		}
	}

#ifdef LOCAL
	cerr.precision(5);
	cerr << "Time: " << fixed << (double) clock() / CLOCKS_PER_SEC << endl;
#endif
	return 0;
}

