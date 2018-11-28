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
int const N = 111;
int a[N];
int main() {
  freopen("A-large.in", "r", stdin);
	freopen("A-large-ans.out", "w", stdout);
	int T, ca = 1; scanf("%d", &T);
	while (T--) {
		int n, p; scanf("%d%d", &n, &p);
		Rep(i, n) scanf("%d", &a[i]);
		int ans = 0;
		Rep(i, n) {
			if (a[i] % p == 0) ++ans;
			a[i] %= p;
		}
		if (p == 2) {
			int s = 0;
			Rep(i, n) s += a[i];
			ans += (s + 1) / 2;
		} else if (p == 3) {
			int c1 = 0, c2 = 0;
			Rep(i, n) { if (a[i] == 1) ++c1; if (a[i] == 2) ++c2; }
			int g = min(c1, c2);
			ans += g; c1 -= g; c2 -= g;
			int t = max(c1, c2);
			ans += t / 3; t %= 3;
			if (t > 0) ++ans;
		} else if (p == 4) {
			int c1 = 0, c2 = 0, c3 = 0;
			Rep(i, n) { if (a[i] == 1) ++c1; if (a[i] == 2) ++c2; if (a[i] == 3) ++c3; }
			ans += c2 / 2; c2 %= 2;
			int g = min(c1, c3);
			ans += g; c1 -= g; c3 -= g;
			int t = max(c1, c3);
			ans += t / 4; t %= 4;
			if (c2 > 0) {
				if (t <= 2) ans += 1;
				else ans += 2;
			} else {
				if (t > 0) ans += 1;
			}
		}
		
		printf("Case #%d: %d\n", ca++, ans);
	}
	return 0;
}

