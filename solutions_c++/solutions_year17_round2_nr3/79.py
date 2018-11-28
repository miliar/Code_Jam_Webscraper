#include<bits/stdc++.h>
using namespace std;
const int N(105);
typedef long long LL;
LL inf(1e18);
LL e[N], s[N], a[N][N];
double b[N][N];
int main() {
	int tests;
	scanf("%d", &tests);
	for(int qq(1); qq <= tests; qq++) {
		int n, Q;
		scanf("%d%d", &n, &Q);
		for(int i(1); i <= n; i++)
			cin >> e[i] >> s[i];
		for(int i(1); i <= n; i++) {
			for(int j(1); j <= n; j++) {
				cin >> a[i][j];
				if(a[i][j] == -1)
					a[i][j] = inf;
			}
		}
		for(int k(1); k <= n; k++) {
			for(int i(1); i <= n; i++) {
				for(int j(1); j <= n; j++) {
					a[i][j] = min(a[i][j], a[i][k] + a[k][j]);
				}
			}
		}
		for(int i(1); i <= n; i++) {
			for(int j(1); j <= n; j++) {
				if(a[i][j] <= e[i]) {
					b[i][j] = a[i][j] / (double)s[i];
				}else {
					b[i][j] = inf;
				}
			}
		}
		for(int k(1); k <= n; k++) {
			for(int i(1); i <= n; i++) {
				for(int j(1); j <= n; j++) {
					b[i][j] = min(b[i][j], b[i][k] + b[k][j]);
				}
			}
		}
		printf("Case #%d:", qq);
		for(int i(0); i < Q; i++) {
			int x, y;
			cin >> x >> y;
			printf(" %.12f", b[x][y]);
		}
		printf("\n");
	}
}

