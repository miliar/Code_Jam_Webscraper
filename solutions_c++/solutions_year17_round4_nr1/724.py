#include <bits/stdc++.h>
#define ll long long
#define mk make_pair
using namespace std;
 
const int N = 1e2 + 5;
const int mod = 1e9 + 7;
const int inf = 1e9;

int n, p, a[N], b[N]; 
int dp[N][N][N];

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("1.txt", "w", stdout);
	int T, cas = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%d %d", &n, &p);
		for (int i = 1; i <= n; i++) scanf("%d", a + i), a[i] %= p;
		for (int i = 0; i <= p; i++) b[i] = 0;
		for (int i = 1; i <= n; i++) b[a[i]]++;
		int ans = 0;
		if (p == 2) {
			ans = b[0];
			ans += b[1] / 2;
			if (b[1] % 2) ans++;
		} else 
		if (p == 3) {
			ans = b[0];
			int tmp = min(b[1], b[2]);
			ans += tmp;
			b[1] -= tmp;
			b[2] -= tmp;
			if (b[1]) {
				ans += b[1] / 3;
				b[1] %= 3;
			}
			if (b[2]) {
				ans += b[2] / 3;
				b[2] %= 3;
			}
			if (b[1] > 0 || b[2] > 0) ans++;
		} else {
			ans = b[0];
			if ((b[1] + b[2] * 2 + b[3] * 3) % 4 == 0) ans--;
			int tmp = min(b[1], b[3]);
			ans += tmp;
			b[1] -= tmp;
			b[3] -= tmp;
			if (b[1]) {
				ans += b[1] / 4;
				b[1] %= 4;
			}
			if (b[2]) {
				ans += b[2] / 2;
				b[2] %= 2;
			}
			if (b[3]) {
				ans += b[3] / 4;
				b[3] %= 4;
			}
			if ((b[2] * 2 + b[1] + b[3] * 3) % 4 == 0) ans++;
		}
		printf("Case #%d: %d\n", ++cas, ans);
	}
}
