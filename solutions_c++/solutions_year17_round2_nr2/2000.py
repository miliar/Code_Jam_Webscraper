#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char translate(int index);
int main() {
	int T, N, colors[6];
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		scanf("%d %d %d %d %d %d %d", &N, &colors[0], &colors[1], &colors[2], &colors[3], &colors[4], &colors[5]);
		int now, opposite, opp_left, opp_right;
		char ans[1000] = {};
		bool impossible = false;
		for (int i = 0; i < 6; i ++) {
			int index = (i < 3) ? (i * 2) : (i * 2 - 5);
			if (colors[index] > 0) {
				now = index;
				ans[0] = translate(now);
				colors[now]--;
				break;
			}
		}
		for (int n = 1; n < N; n++) {
			opposite = (now + 3) % 6;
			opp_left = (now + 2) % 6;
			opp_right = (now + 4) % 6;
			if (colors[opposite] > 0) {
				now = opposite;
			} else if (now & 1) {
				impossible = true;
				break;
			} else if (colors[opp_left] > colors[opp_right]) {
				now = opp_left;
			} else if (colors[opp_right] > 0) {
				now = opp_right;
			} else {
				impossible = true;
				break;
			}
			ans[n] = translate(now);
			colors[now]--;
		}
		if (impossible || ans[0] == ans[N - 1]) {
			printf("Case #%d: IMPOSSIBLE\n", t + 1);
		} else {
			printf("Case #%d: %s\n", t + 1, ans);
		}
	}
	return 0;
}

char translate(int index) {
	if (index == 0) return 'R';
	if (index == 1) return 'O';
	if (index == 2) return 'Y';
	if (index == 3) return 'G';
	if (index == 4) return 'B';
	if (index == 5) return 'V';
}

