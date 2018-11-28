#include <iostream>
#include <cstdio>
#include <map>
#include <tuple>
#include <cstring>
using namespace std;

map<tuple<int, int, int, int, int>, int> M;
int TT, T, n, p, count[4], ans;

int dfs(int leftover, int c0, int c1, int c2, int c3) {
	if (c0 + c1 + c2 + c3 == 0)
		return 0;
	tuple<int, int, int, int, int> t = make_tuple(leftover, c0, c1, c2, c3);
	if (M.find(t) != M.end())
		return M[t];
	int ret = 10000;
	if (c0 > 0)
		ret = min(ret, dfs(leftover, c0 - 1, c1, c2, c3));
	if (c1 > 0)
		ret = min(ret, dfs((leftover + 1) % p, c0, c1 - 1, c2, c3));
	if (c2 > 0 && p > 2)
		ret = min(ret, dfs((leftover + 2) % p, c0, c1, c2 - 1, c3));
	if (c3 > 0 && p > 3)
		ret = min(ret, dfs((leftover + 3) % p, c0, c1, c2, c3 - 1));
	ret = ret + (leftover > 0);
	// printf("  [%d, %d, %d, %d, %d], %d\n", leftover, c0, c1, c2, c3, ret + (leftover > 0));
	M[t] = ret;
	return ret;
}

int main() {

	scanf("%d", &TT);
	for (int T = 1; T <= TT; T++) {
		printf("Case #%d: ", T);

		memset(count, 0, sizeof(count));
		scanf("%d%d", &n, &p);
		for (int i = 0; i < n; i++) {
			int x;
			scanf("%d", &x);
			count[x % p] ++;
		}
		M.clear();
		ans = dfs(0, count[0], count[1], count[2], count[3]);
		printf("%d\n", n - ans);
	}

	return 0;
}