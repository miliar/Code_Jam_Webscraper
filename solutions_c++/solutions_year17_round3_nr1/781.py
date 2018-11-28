#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:256000000")
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cstring>
#include <numeric>
#include <queue>
#include <cassert>
#include <unordered_map>

using namespace std;

typedef long long ll;
typedef double ld;

#define TASK "divisible"

int solve();

int main() {
#ifdef PoDuReM
	freopen("input.txt", "r", stdin), freopen("output.txt", "w", stdout);
#else
	//freopen(TASK".in", "r", stdin), freopen(TASK".out", "w", stdout);
#endif
	return solve();
}

const int dd = (int)1e3 + 1;
const ld pi = atan2(1, 1) * 4;

struct N {
	int r, h;
} A[dd];

int solve() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: ", i);
		int n, k;
		scanf("%d %d", &n, &k);
		for (int i = 0; i < n; ++i)
			scanf("%d %d", &A[i].r, &A[i].h);
		ld ans = 0;
		if (k == 1) {
			for (int i = 0; i < n; ++i)
				ans = max(ans, 2 * pi * A[i].r * A[i].h + pi * A[i].r * A[i].r);
		} else {
			sort(A, A + n, [](N a, N b) {
				return a.r < b.r;
			});
			ll B = 0;
			multiset<ll> S;
			for (int i = 0; i < n; ++i) {
				if ((int)S.size() == k - 1)
					ans = max(ans, 2 * pi * B + pi * A[i].r * A[i].r + 2 * pi * A[i].r * A[i].h);
				S.insert(1ll * A[i].h * A[i].r);
				B += 1ll * A[i].r * A[i].h;
				if ((int)S.size() == k) {
					ll O = *S.begin();
					B -= O;
					S.erase(S.begin());
				}
			}
		}
		printf("%.7f\n", ans);
	}
	return 0;
}