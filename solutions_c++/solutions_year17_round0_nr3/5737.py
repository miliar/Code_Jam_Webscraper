#include <stdio.h>
#include <vector>
using namespace std;

int t;

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	scanf("%d", &t);
	for (int cnt = 1; cnt <= t; ++cnt) {
		int n, k;
		scanf("%d %d", &n, &k);
		printf("Case #%d: ", cnt);
		vector<int> p(n + 2);
		p[0] = 1;
		p[n + 1] = 1;
		int max_start = 1, max_end = 1;
		while (k > 0) {
			int cur = 0;
			int cur_start = 1, cur_end = 1;
			int max = 0;
			max_start = 1;
			max_end = 1;
			for (int i = 1; i <= n; ++i) {
				if (p[i] == 0) {
					++cur;
					cur_end = i;
				}
				else {
					if (cur > max) {
						max = cur;
						max_start = cur_start;
						max_end = cur_end;
					}
					cur_start = i + 1;
					cur = 0;
				}
			}
			if (cur > max) {
				max_start = cur_start;
				max_end = cur_end;
			}
			p[(max_start + max_end) / 2] = 1;
			--k;
		}
		int left = 0, right = 0;
		for (int i = (max_start + max_end) / 2 - 1; i > 0; --i) {
			if (p[i] == 0) ++left;
			else break;
		}
		for (int i = (max_start + max_end) / 2 + 1; i <= n; ++i) {
			if (p[i] == 0) ++right;
			else break;
		}
		if (left > right) printf("%d %d\n", left, right);
		else printf("%d %d\n", right, left);
	}

	fclose(stdin); fclose(stdout);
	return 0;
}