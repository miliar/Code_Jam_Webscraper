#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int main() {

	int T;
	scanf("%d", &T);

	for (int tt = 1; tt <= T; tt++) {

		int N, P;
		scanf("%d %d", &N, &P);

		vector<int> arr(N);

		for (int i = 0; i < N; i++) scanf("%d", &arr[i]);

		vector<int> remain(P, 0);

		for (int i = 0; i < N; i++) {
			remain[arr[i] % P]++;
		}

		int cnt = 0;
		cnt += remain[0];

		if (P == 2) {
			cnt += (remain[1] + 1) / 2;
		}
		else if (P == 3) {
			int sub = min(remain[1], remain[2]);
			cnt += sub;
			remain[1] -= sub;
			remain[2] -= sub;

			cnt += (max(remain[1], remain[2]) + 2) / 3;
		}
		else {
			int sub = min(remain[1], remain[3]);
			cnt += sub;
			remain[1] -= sub;
			remain[3] -= sub;

			if (remain[2] % 2 == 0) {
				cnt += remain[2] / 2;
				remain[2] = 0;
			}
			else {
				cnt += remain[2] / 2;
				remain[2] = 1;
			}

			if (remain[2] == 1) {

				if (remain[1] >= 2) {
					cnt++;
					remain[1] -= 2;
				}
				else if (remain[3] >= 2) {
					cnt++;
					remain[3] -= 2;
				}
				else {
					cnt++;
					remain[1]--;
					remain[3]--;
				}
			}
			cnt += (max(remain[1], remain[3]) + 3) / 4;
		}

		printf("Case #%d: %d\n", tt, cnt);
	}
}