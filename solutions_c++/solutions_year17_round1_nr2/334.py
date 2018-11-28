#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>

using namespace std;

int Kiriage(int a, int b)
{
	return (a + b - 1) / b;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int N, P;
		int R[50], Q[50][50];
		scanf("%d%d", &N, &P);
		for (int i = 0; i < N; i++) {
			scanf("%d", &R[i]);
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < P; j++) {
				scanf("%d", &Q[i][j]);
			}
			sort(&Q[i][0], &Q[i][0] + P);
		}
		int ret = 0;
		int pos[50] = {0};
		while (true) {
			int kosuu = 0;
			for (int i = 0; i < N; i++) {
				int cur = Q[i][pos[i]];
				int ckos = Kiriage(Kiriage(cur * 10, 11), R[i]);
				while (!(cur >= Kiriage(ckos * R[i] * 9, 10) && cur <= ckos * R[i] * 11 / 10)) {
					pos[i]++;
					if (pos[i] >= P) {
						goto END;
					}
					cur = Q[i][pos[i]];
					ckos = Kiriage(Kiriage(cur * 10, 11), R[i]);
				}
				kosuu = max(ckos, kosuu);
			}
			bool valid = true;
			for (int i = 0; i < N; i++) {
				int cur = Q[i][pos[i]];
				if (!(cur >= Kiriage(kosuu * R[i] * 9, 10) && cur <= kosuu * R[i] * 11 / 10)) {
					valid = false;
					pos[i]++;
					if (pos[i] >= P) {
						goto END;
					}
				}
			}
			if (valid) {
				ret++;
				for (int i = 0; i < N; i++) {
					pos[i]++;
					if (pos[i] >= P) {
						goto END;
					}
				}
			}
		}
	END:
		printf("Case #%d: %d\n", t, ret);
	}
	return 0;
}
