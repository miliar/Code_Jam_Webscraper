#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>

const int T = 24 * 60;
const int MAXT = T + 1;
const int MAXH = T / 2 + 1;

int dp[MAXT][MAXH][2];
int valid[T];

void opt(int &a, int b) {
	if (b < a) {
		a = b;
	}
}

int main() {
	int task;
	scanf("%d", &task);
	for (int task_id = 1; task_id <= task; ++ task_id) {
		int n, m;
		scanf("%d %d", &n, &m);
		memset(valid, -1, sizeof valid);
		for (int i = 0; i < n; ++ i) {
			int l, r;
			scanf("%d %d", &l, &r);
			for (int j = l; j < r; ++ j) {
				valid[j] = 0;
			}
		}
		for (int i = 0; i < m; ++ i) {
			int l, r;
			scanf("%d %d", &l, &r);
			for (int j = l; j < r; ++ j) {
				valid[j] = 1;
			}
		}
		memset(dp, 127, sizeof dp);
		dp[0][0][0] = 1;
		dp[0][0][1] = 1;
		for (int i = 0; i < T; ++ i) {
			for (int j = 0; j <= std::min(T / 2, i); ++ j) {
				for (int k = 0; k < 2; ++ k) {
					if (valid[i] != k) {
						int _j = j + (k ^ 1);
						if (_j <= T / 2) {
							opt(dp[i + 1][_j][k], dp[i][j][k]);
						}
					}
					if (valid[i] != (k ^ 1)) {
						int _j = j + k;
						if (_j <= T / 2) {
							opt(dp[i + 1][_j][k ^ 1], dp[i][j][k] + 1);
						}
					}
				}
			}
		}
		int ret = std::min(dp[T][T / 2][0], dp[T][T / 2][1]) / 2 * 2;
		printf("Case #%d: %d\n", task_id, ret);
	}
	return 0;
}

