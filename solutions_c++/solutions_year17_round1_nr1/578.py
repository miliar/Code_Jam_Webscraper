#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;
int n, m;
char c[30][30], a[30][30];
int flag[30];
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int T;
	cin >> T;
	for(int ii = 1; ii <= T; ++ii) {
		scanf("%d%d", &n, &m);
		for(int i = 1; i <= n; ++i) {
			scanf("%s", a[i]+1);
			for(int j = 1; j <= m; ++j)
				if(a[i][j] != '?') {
					flag[i] = true;
					for(int k = j - 1; k >= 1 && a[i][k] == '?'; k--)
						a[i][k] = a[i][j];
					for(int k = j + 1; k <= m && a[i][k] == '?'; k++)
						a[i][k] = a[i][j];
				}
		}
		for(int i = 1; i <= n; ++i)
			if(flag[i]) {
				for(int k = i - 1; k >= 1 && !flag[k]; k--) {
					flag[k] = true;
					for(int j = 1; j <= m; ++j)
						a[k][j] = a[i][j];
				}
				for(int k = i + 1; k <= n && !flag[k]; k--) {
					flag[k] = true;
					for(int j = 1; j <= m; ++j)
						a[k][j] = a[i][j];
				}
			}
		printf("Case #%d:\n", ii);
		for(int i = 1; i <= n; ++i)
			printf("%s\n",a[i]+1);
		memset(flag, 0, sizeof flag);
	}
	return 0;
}