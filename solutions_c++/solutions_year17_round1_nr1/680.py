#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <ctime>

#define inf 0x3f3f3f3f
#define Inf 0x3FFFFFFFFFFFFFFFLL
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define Rep(i, n) for (int i = 1; i <= (n); ++i)
#define clr(x, a) memset(x, (a), sizeof x)
using namespace std;
typedef long long ll;
int const N = 33;
char g[N][N];
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large-ans.out", "w", stdout);
	int T, ca = 1; scanf("%d", &T);
	while (T--) {
		int n, m; scanf("%d%d", &n, &m);
		rep(i, n) scanf(" %s", g[i]);
		rep(i, n) rep(j, m) {
			int t = j;
			while (t > 0 && g[i][t - 1] == '?') g[i][t - 1] = g[i][j], --t;
			t = j;
			while (t + 1 < m && g[i][t + 1] == '?') g[i][t + 1] = g[i][j], ++t;
		}
		rep(i, n) rep(j, m) {
			int t = i;
			while (t > 0 && g[t - 1][j] == '?') g[t - 1][j] = g[i][j], --t;
			t = i;
			while (t + 1 < n && g[t + 1][j] == '?') g[t + 1][j] = g[i][j], ++t;
		}
		printf("Case #%d:\n", ca++);
		rep(i, n) puts(g[i]);
		
	}
	return 0;
}

