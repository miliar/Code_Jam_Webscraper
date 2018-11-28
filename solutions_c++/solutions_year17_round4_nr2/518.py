//writted by dnvtmf
#include <bits/stdc++.h>
#define INF 1000000007
#define FI first
#define SE second
#define PB push_back
#define VI vector<int>
#define MP make_pair
#define FOR(x, st, ed) for(auto x = (st); x < (ed); ++x)
#define FORE(x, st, ed) for(auto x = (st); x <= (ed); ++x)
#define CLR(arr, val) memset(arr, val, sizeof(arr))
#define INFO(tag, st, ed, x) printf("%s: ", tag); \
	FOR(_i, st, ed) cout << x[_i] << ' '; puts("");
using namespace std;
typedef long long LL;
typedef pair <int, int> PII;
const int NUM = 1100;
int n, m, c;
int a[NUM], b[NUM];
int ans;
bool solve(int x) {
	int d;
	d = ans = 0;
	for(int i = 1000; i > 0; i--) {
		if(a[i] > x) ans += a[i] - x;
		d = max(0, d + a[i] - x);
	}
	return d == 0;
}
int main() {
#ifdef ACM_TEST
	freopen("in.txt", "r", stdin);
#endif
	int T; scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas) {
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		scanf("%d%d%d", &n, &c, &m);
		for(int i = 0, x, y; i < m; ++i) {
			scanf("%d%d", &x, &y);
			a[x]++;
			b[y]++;
		}
		int l = 1, r = m, mid, y = -1, z = -1;
		for(int i = 1; i <= c; ++i)
			l = max(l, b[i]);
		while(l <= r) {
			mid = (l + r) >> 1;
			if(solve(mid)) {
				y = mid;
				z = ans;
				r = mid - 1;
			}
			else
				l = mid + 1;
		}
		printf("Case #%d: %d %d\n", cas, y, z);
	}
	return 0;
}
