#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < n; i ++)
typedef long long LL;
const int N = 1000 + 5;
int cnt[6];
std::vector<int> contains;
char color[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};

bool cmp(int i, int j) {
	return cnt[i] > cnt[j];
}

int main() {
	int T, n;
	scanf("%d", &T);
	rep(cas, T) {
		rep(i, 6) {
			cnt[i] = 0;
		}
		scanf("%d", &n);
		contains.clear();
		rep(i, 6) {
			scanf("%d", cnt + i);
			if (cnt[i] != 0) {
				contains.push_back(i);
			}
		}
		printf("Case #%d: ", cas + 1);
		if (contains.size() == 1) {
			puts("IMPOSSIBLE");
			continue;
		}
		if (contains.size() == 2) {
			if (cnt[contains[0]] != cnt[contains[1]]) {
				puts("IMPOSSIBLE");
			} else {
				rep(i, n/2) {
					putchar(color[contains[0]]);
					putchar(color[contains[1]]);
				}
				puts("");
			}
			continue;
		}
		std::sort(contains.begin(), contains.end(), cmp);
		if (cnt[contains[1]] + cnt[contains[2]] < cnt[contains[0]]) {
			puts("IMPOSSIBLE");
			continue;
		}
		int remain = cnt[contains[1]] + cnt[contains[2]] - cnt[contains[0]];
		int total = 0;
		rep(i, remain) {
			total += 3;
			putchar(color[contains[0]]);
			putchar(color[contains[1]]);
			putchar(color[contains[2]]);
		}
		rep(i, cnt[contains[1]] - remain) {
			total += 2;
			putchar(color[contains[0]]);
			putchar(color[contains[1]]);
		}
		rep(i, cnt[contains[0]] - cnt[contains[1]]) {
			total += 2;
			putchar(color[contains[0]]);
			putchar(color[contains[2]]);
		}
		puts("");
		if (total != n) {
			printf("=========%d\n\n", total);
		}
	}
	return 0;
}
