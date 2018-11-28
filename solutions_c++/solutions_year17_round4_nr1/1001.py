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

const int MAXP = 4;
const int MAXN = 100 + 4;

int n, p;
vi g;

bool read() {
	if  (scanf("%d%d", &n, &p) < 2) {
		return 0;
	}
	g.resize(n);
	forn(i, n) {
		scanf("%d", &g[i]);
	}
	return 1;
}

int dp[MAXP][MAXN][MAXN][MAXN][MAXN];

void remax(int& x, int y) {
	if  (x < y) {
		x = y;
	}
}

int solve() {
	memset (dp, -1, sizeof dp);

	vi cnt(4, 0);
	for (int x : g) {
		++cnt[x % p];
	}

	dp[0][cnt[0]][cnt[1]][cnt[2]][cnt[3]] = 0;
	for (int sum = n; sum > 0; --sum) {
		for (int c0 = 0; c0 <= sum; ++c0) {
			for (int c1 = 0; c0 + c1 <= sum; ++c1) {
				for (int c2 = 0; c0 + c1 + c2 <= sum; ++c2) {
					const int c3 = sum - c0 - c1 - c2;
					forn(have, p) {
						const int& cur_dp = dp[have][c0][c1][c2][c3];
						if  (cur_dp == -1) {
							continue;
						}
						// if  (cur_dp) {
						// 	printf("have=%d, c0=%d, c1=%d, c2=%d, c3=%d -> %d\n", have, c0, c1, c2, c3, cur_dp);
						// }
						if  (c0) {
							int h = have % p;
							remax(dp[h][c0 - 1][c1][c2][c3], cur_dp + (have == 0));
						}
						if  (c1) {
							int h = (have + 1) % p;
							remax(dp[h][c0][c1 - 1][c2][c3], cur_dp + (have == 0));
						}
						if  (c2) {
							int h = (have + 2) % p;
							remax(dp[h][c0][c1][c2 - 1][c3], cur_dp + (have == 0));
						}
						if  (c3) {
							int h = (have + 3) % p;
							remax(dp[h][c0][c1][c2][c3 - 1], cur_dp + (have == 0));
						}
					}
				}
			}
		}
	}

	int ans = 0;
	forn(have, p) {
		remax(ans, dp[have][0][0][0][0]);
	}
	return ans;
}

int main() {
#ifdef LOCAL
	freopen(FILE_NAME ".in", "r", stdin);
	freopen(FILE_NAME ".out", "w", stdout);
#endif

	int T;
	scanf("%d\n", &T);
	forn(t, T) {
		cerr << t + 1 << " / " << T << endl;

		assert(read());
		printf("Case #%d: %d\n", t + 1, solve());
	}

#ifdef LOCAL
	cerr.precision(5);
	cerr << "Time: " << fixed << (double) clock() / CLOCKS_PER_SEC << endl;
#endif
	return 0;
}

