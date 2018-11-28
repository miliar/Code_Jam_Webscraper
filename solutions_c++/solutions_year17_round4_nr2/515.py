#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

int onboard[1010][1010];

int ticket[1010];
int seat[1010];

int N, C, M;

void solve() {
	scanf("%d%d%d", &N, &C, &M);

	memset(seat, 0, sizeof(seat));
	memset(ticket, 0, sizeof(ticket));

	for (int i = 0; i < M; i++) {
		int a, b; scanf("%d%d", &a, &b);
		ticket[b]++;
		seat[a]++;
	}

	int mv = -1;
	for (int i = 1; i <= C; i++) {
		mv = max(mv, ticket[i]);
	}

	for (;; mv++) {
		int flag = 0;
		int available = 0;
		int promoted = 0;
		for (int i = 1; i <= N; i++) {
			available += mv;
			available -= seat[i];
			promoted += max(seat[i] - mv, 0);

			if (available < 0) {
				flag = 1; break;
			}
		}

		if (flag) {
			continue;
		}

		printf("%d %d\n", mv, promoted);
		break;
	}
}

int main(void) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solve();
	}
}
