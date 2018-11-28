#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

int T, D, n;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		scanf("%d%d", &D, &n);
		double MaT = 0;
		for (int i = 1; i <= n; i++) {
			int p, v;
			scanf("%d%d", &p, &v);
			double t = (D - p)	* 1.0 / v;
			MaT = max(MaT, t);
		}
		printf("Case #%d: %.10lf\n", cas, D * 1.0 / MaT);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
