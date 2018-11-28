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
const int NUM = 100010;
int n, m;
int g[110];
int cnt[5];
int main() {
#ifdef ACM_TEST
	freopen("in.txt", "r", stdin);
#endif
	int T; scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas) {
		scanf("%d%d", &n, &m);
		for(int i = 0; i < m; ++i) cnt[i] = 0;
		for(int i = 0; i < n; ++i) {
			scanf("%d", &g[i]);
			++cnt[g[i] % m];
		}
		int ans = 0;
		if(m == 2) {
			ans = cnt[0] + (cnt[1] + 1) / 2;
		}
		else if(m == 3) {
			ans = cnt[0];
			if(cnt[1] > cnt[2])
				swap(cnt[1], cnt[2]);
			ans += cnt[1];
			cnt[2] -= cnt[1];
			ans += (cnt[2] + 2) / 3;
		}
		else {
			// need 1: 0
			ans = cnt[0];
			// need 2: 2 + 2 or 1 + 3
			int v = cnt[2] / 2;
			ans += v;
			cnt[2] -= v + v;
			v = min(cnt[1], cnt[3]);
			ans += v;
			cnt[1] -= v;
			cnt[3] -= v;
			// need 3: 1 + 1 + 2 or 3 + 3 + 2
			if(cnt[1] == 0) cnt[1] = cnt[3];
            v = min(cnt[1] / 2, cnt[2]);
            ans += v;
            cnt[1] -= v + v;
            cnt[2] -= v;
            // need 4: 1 * 4 or 3 * 4
            v = cnt[1] / 4;
            ans += v;
            cnt[1] -= 4 * v;
            // left
            if(cnt[1] || cnt[2])
				++ans;
		}
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
