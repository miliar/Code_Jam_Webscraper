#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <string>

using namespace std;

char bit[1000][1000];

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int N, C, M;
		scanf("%d%d%d", &N, &C, &M);
		int c[2][1000] = {0};
		int k[2] = {0};
		for (int i = 0; i < M; i++) {
			int a, b;
			scanf("%d%d", &a, &b);
			c[b - 1][a-1]++;
			k[b - 1]++;
		}
		int D = max(k[0], k[1]);
		int ans = 0;
		for (int i = 0; i < N; i++) {
			int sum = 0;
			for (int j = 0; j < C; j++) {
				sum += c[j][i];
			}
			if (sum > D) {
				if (i == 0) {
					D = sum;
					break;
				} else {
					ans = sum - D;
				}
			}
		}
		printf("Case #%d: %d %d\n", t, D, ans);
	}
	return 0;
}
