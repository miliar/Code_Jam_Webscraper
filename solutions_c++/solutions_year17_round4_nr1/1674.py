/*input
3
4 3
4 5 6 4
4 2
4 5 6 4
3 3
1 1 1
*/
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
#include <random>
using namespace std;
#define sp ' '
#define endl '\n'
#define fi first
#define se second
#define mp make_pair
#define int long long
#define N

int n, m;
int cnt[5];
int ans;

int ceil(int x, int y) {
	int ret = x / y;
	if (x % y) ret++;
	return ret;
}
signed main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
#ifdef UncleGrandpa
	freopen("1test.inp", "r", stdin);
#endif
	int T; cin >> T; int CT = 0;
	while (T--) {
		CT++;
		cin >> n >> m; ans = 0;
		memset(cnt, 0, sizeof(cnt));
		for (int i = 1; i <= n; i++) {
			int t; cin >> t; cnt[t % m]++;
		}
		if (m == 2) {
			ans += cnt[0] + ceil(cnt[1], 2);
		}
		else if (m == 3) {
			ans += cnt[0] + min(cnt[1], cnt[2]);
			int t = min(cnt[1], cnt[2]);
			cnt[1] -= t; cnt[2] -= t;
			ans += ceil(max(cnt[1], cnt[2]), 3);
		}
		cout << "Case #" << CT << ": ";
		cout << ans << endl;
	}

}