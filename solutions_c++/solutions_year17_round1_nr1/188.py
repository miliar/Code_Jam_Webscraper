#pragma GCC optimize(2)
#include <bits/stdc++.h>
#define LL long long
#define INF (1LL << 60)
using namespace std;

template<class T> inline
void read(T& x) {
	int f = 1; x = 0;
	char ch = getchar();
	while (ch < '0' || ch > '9')   {if (ch == '-') f = -1; ch = getchar();}
	while (ch >= '0' && ch <= '9') {x = x * 10 + ch - '0'; ch = getchar();}
	x *= f;
}

/*============ Header Template ============*/

const int N = 100 + 5;

int n, m;
int c[N];
char mp[N][N], ans[N][N];

int main() {
	int T, kas = 0;
	read(T);
	while (T--) {
		read(n), read(m);
		for (int i = 1; i <= n; i++) scanf("%s", mp[i] + 1);
		int f = 0;
		for (int i = 1; i <= n; i++) c[i] = 0;
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) if (mp[i][j] != '?') c[i]++;
			if (!f && c[i]) f = i;
		}
		for (int i = f; i <= n; i++) {
			if (!c[i]) {
				for (int j = 1; j <= m; j++) ans[i][j] = ans[i - 1][j];
				continue;
			}
			int last = 0;
			for (int j = 1; j <= m; j++) {
				if (mp[i][j] != '?') {
					for (int k = last + 1; k <= j; k++) ans[i][k] = mp[i][j];
					last = j;
				}
			}
			for (int j = last + 1; j <= m; j++) ans[i][j] = ans[i][last];
		}
		printf("Case #%d:\n", ++kas);
		for (int i = f - 1; i; i--)
			for (int j = 1; j <= m; j++) ans[i][j] = ans[i + 1][j];
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) printf("%c", ans[i][j]);
			printf("\n");
		}
	}
	return 0;
}