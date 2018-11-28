#include <bits/stdc++.h>
#define ll long long
using namespace std;

const int N = 1445;

int f[N][N][2], t[N];
int a, b, l[N], r[N], l1[N], r1[N];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("2.txt", "w", stdout); 
	int T, cas = 0;
	scanf("%d", &T);
	while (T--) {
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				f[i][j][0] = f[i][j][1] = N + N, t[j] = -1;
		cin >> a >> b;
		for (int i = 1; i <= a; i++) {
			scanf("%d %d", l + i, r + i);
			l[i]++;
			for (int j = l[i]; j <= r[i]; j++)
				t[j] = 1;
		}
		for (int i = 1; i <= b; i++) {
			scanf("%d %d", l1 + i, r1 + i);
			l1[i]++;
			for (int j = l1[i]; j <= r1[i]; j++)
				t[j] = 0;
		}
		int ans = N + N;
		f[0][0][0] = 0;
		for (int i = 0; i < 1440; i++) {
			for (int j = 0; j <= i; j++) {
				for (int k = 0; k <= 1; k++) {
					if (t[i + 1] == 0) {
						f[i + 1][j + 1][0] = min(f[i][j][k] + (k == 1), f[i + 1][j + 1][0]);
					} else
					if (t[i + 1] == 1) {
						f[i + 1][j][1] = min(f[i][j][k] + (k == 0), f[i + 1][j][1]);
					} else {
						f[i + 1][j + 1][0] = min(f[i][j][k] + (k == 1), f[i + 1][j + 1][0]);
						f[i + 1][j][1] = min(f[i][j][k] + (k == 0), f[i + 1][j][1]);
					}
				}
			}
		}
		ans = min(ans, f[1440][720][0]);
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				f[i][j][0] = f[i][j][1] = N + N;
		f[0][0][1] = 0;
		for (int i = 0; i < 1440; i++) {
			for (int j = 0; j <= i; j++) {
				for (int k = 0; k <= 1; k++) {
					if (t[i + 1] == 0) {
						f[i + 1][j + 1][0] = min(f[i][j][k] + (k == 1), f[i + 1][j + 1][0]);
					} else
					if (t[i + 1] == 1) {
						f[i + 1][j][1] = min(f[i][j][k] + (k == 0), f[i + 1][j][1]);
					} else {
						f[i + 1][j + 1][0] = min(f[i][j][k] + (k == 1), f[i + 1][j + 1][0]);
						f[i + 1][j][1] = min(f[i][j][k] + (k == 0), f[i + 1][j][1]);
					}
				}
			}
		}
		ans = min(ans, f[1440][720][1]);
		printf("Case #%d: %d\n", ++cas, ans);
	}
}
