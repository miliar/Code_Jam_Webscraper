#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int main() {

	int T;
	scanf("%d", &T);

	for (int tt = 1; tt <= T; tt++) {

		int N, C, M;
		scanf("%d %d %d", &N, &C, &M);

		vector<int> seat(N + 1, 0);
		vector<int> cnt(C + 1, 0);

		for (int i = 0; i < M; i++) {
			int a, b;
			scanf("%d %d", &a, &b);
			seat[a]++;
			cnt[b]++;
		}

		int MAX = 0;
		for (int i = 1; i <= C; i++) {
			MAX = max(MAX, cnt[i]);
		}

		for (int k = MAX; k <= M; k++) {
			int sum = 0;
			int CNT = 0;

			for (int i = N; i >= 1; i--) {
				if (seat[i] > k) {
					sum += seat[i] - k;
					CNT += seat[i] - k;
				}
				else {
					sum -= k - seat[i];
					if (sum < 0)sum = 0;
				}
			}
			if (sum == 0) {
				printf("Case #%d: %d %d\n",tt, k, CNT);
				break;
			}
		}
	}
}