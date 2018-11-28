#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
using namespace std;
int T, n, m, p, ans;
int a[110], b[5][5], c[5];

int main()  {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> T;
	for (int C = 1; C <= T; C++) {
		cin >> n >> p;
		memset(b, 0, sizeof(b));
		memset(c, 0, sizeof(c));
		for (int i = 1; i <= n; i++) {
			scanf("%d", &a[i]);
			b[2][a[i] & 1]++;
			b[3][a[i] % 3]++;
			b[4][a[i] % 4]++;
		}
		for (int i = 0; i < 5; i++) c[i] = b[p][i];
		if (p == 2) {
			ans = c[0] + (c[1] + 1) / 2;
		}
		else if (p == 3) {
			ans = min(c[1], c[2]);
			c[1] -= ans;
			c[2] -= ans;
			ans += c[0];
			ans += (max(c[1], c[2]) + 2) / 3;
		}
		else if (p == 4) {
			ans = min(c[1], c[3]);
			c[1] -= ans;
			c[3] -= ans;
			ans += c[0] + c[2] / 2;
			c[2] &= 1;
			// 1,2 or 2,3
			if (c[1]) {
				if (c[2] == 0) ans += (c[1] + 3) / 4;
				else {
					ans++, c[1] -= 2;
					if (c[1] > 0) ans += (c[1] + 3) / 4;
				}
			}
			else if (c[3]) {
				if (c[2] == 0) ans += (c[3] + 3) / 4;
				else {
					ans++, c[3] -= 2;
					if (c[3] > 0) ans += (c[3] + 3) / 4;
				}
			}
			else if (c[2]) {
				ans++;
			}
		}
		printf("Case #%d: %d\n", C, ans);
	}
}