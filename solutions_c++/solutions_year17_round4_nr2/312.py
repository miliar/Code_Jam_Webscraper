#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <vector>

using namespace std;

int pos[1005], cus[1005];

void run(int cas) {
	int n, m, c, x, y;
	scanf("%d%d%d", &n, &c, &m);
	memset(cus, 0, sizeof(cus));
	memset(pos, 0, sizeof(pos));
	for (int i = 0 ; i < m; i++) {
		scanf("%d%d", &x, &y);
		pos[x]++;
		cus[y]++;
	}
	int least = *max_element(cus + 1, cus + c + 1);
	int sum = 0, ans = 0;
	for (int i = 1; i <= n; i++) {
		sum += pos[i];
		int cur = (sum + (i - 1)) / i;
		least = max(least, cur);
	}
	for (int i = 1; i <= n; i++)
		ans += (pos[i] <= least ? 0 : pos[i] - least);
	printf("Case #%d: %d %d\n", cas, least, ans);
}

int main() {
	int cas, tt;
	scanf("%d", &tt);
	for (cas = 1; cas <= tt; cas++)
		run(cas);
	return 0;
}
