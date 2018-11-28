#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#define mp make_pair
#define pb push_back
#define fir first
#define sec second
using namespace std;
typedef long long ll;

template <typename T> inline void R(T &x) {
	char ch = getchar(); x = 0;
	for (; ch<'0' || ch>'9'; ch = getchar());
	for (; ch<='9' && ch>='0'; ch=getchar()) x = x*10 + ch-'0';
}
const int N = 105;
int n, q, e[N], s[N];
double d[N][N], md[N][N], t[N][N];
const double inf = 1e100;
double floyd(double f[N][N]) {
	for (int k=1; k<=n; ++k)
		for (int i=1; i<=n; ++i) if (i != k)
			for (int j=1; j<=n; ++j) if (i != j && i != k)
				f[i][j] = min(f[i][j], f[i][k] + f[k][j]);
}
void run() {
	scanf("%d%d", &n, &q);
	for (int i=1; i<=n; ++i) {
		scanf("%d%d", &e[i], &s[i]);
	}
	for (int i=1; i<=n; ++i)
		for (int j=1; j<=n; ++j)
			scanf("%lf", &d[i][j]),
			md[i][j] = d[i][j] < 0 ? inf: d[i][j];
	floyd(md);
	for (int i=1; i<=n; ++i)
		for (int j=1; j<=n; ++j)
			t[i][j] = (i == j ? 0 : inf);
	for (int i=1; i<=n; ++i)
		for (int j=1; j<=n; ++j)
			if (md[i][j] <= e[i])
				t[i][j] = min(t[i][j], md[i][j] / s[i]);
	floyd(t);
	int x, y;
	while (q--) {
		scanf("%d%d", &x, &y);
		printf(" %.9lf", t[x][y]);
	}
	puts("");
}
int main( ){
	int T; R(T);
	for (int i=1; i<=T; ++i) {
		printf("Case #%d:", i);
		run();
	}
	return 0;
}