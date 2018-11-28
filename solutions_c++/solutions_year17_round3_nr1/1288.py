#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <stack>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef double DB;

const DB PI = acos(-1);
const int MaxN = 1e3;
int T, n, k;
struct Node {
	DB r, h;
}a[MaxN + 5], b[MaxN + 5];
DB dp[MaxN + 5][MaxN + 5];

bool cmp(Node x, Node y) {
	if(x.r == y.r) return x.h > y.h;
	return x.r > y.r;
}

int main() 
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &T); int cas = 0;
	while(T--) {
		scanf("%d%d", &n, &k);
		for(int i = 1; i <= n; i++) scanf("%lf%lf", &a[i].r, &a[i].h);
		sort(a + 1, a + n + 1, cmp);
		for(int i = 0; i <= n; i++)
			for(int j = 0; j <= k; j++) dp[i][j] = 0.00;
		for(int i = 1; i <= n; i++) {
			for(int j = 1; j <= k; j++) {
				if(j == 1) 
					dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + (a[i].r * a[i].r + 2.00 * a[i].r * a[i].h) * PI);
				else dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + 2.00 * a[i].r * PI * a[i].h);
			}
		}
		printf("Case #%d: %.10lf\n", ++cas, dp[n][k]);
	}
	fclose(stdin);
	fclose(stdout);
}
