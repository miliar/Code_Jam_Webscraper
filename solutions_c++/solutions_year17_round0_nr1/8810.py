#include <cstdio>
#include <cstring>

#include <algorithm>
using namespace std;
char buf[1024];
int n, k;
int moves[111], cnt;

int main() {
	int T;
	scanf("%d", &T);
	for (int kase = 1; kase <= T; ++ kase) {
		scanf("%s%d", buf, &k);
		n = strlen(buf);
		cnt = 0;
		for (int i = 0; i < n; ++ i) {
			if (i + k <= n) {
				moves[cnt ++] = i;
			}
		}
		int res = 0x3f3f3f3f;
		for (int msk = 0; msk < 1 << cnt; ++ msk) {
			char tmp[12];
			for (int i = 0; i < n; ++ i) {
				tmp[i] = buf[i];
			}
			for (int i = 0; i < cnt; ++ i) {
				if (msk >> i & 1) {
					for (int j = 0; j < k; ++ j) {
						int p = moves[i] + j;
						tmp[p] = (tmp[p] == '+' ? '-' : '+');
					}
				}
			}
			bool flag = true;
			for (int i = 0; i < n; ++ i) {
				if (tmp[i] != '+') flag = false;
			}
			if (flag) res = min(res, __builtin_popcount(msk));
		}
		printf("Case #%d: ", kase);
		if (res == 0x3f3f3f3f) puts("IMPOSSIBLE");
		else printf("%d\n", res);
	}
	return 0;
}
