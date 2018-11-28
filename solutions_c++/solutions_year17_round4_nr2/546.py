#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 5005;

int N, C, M, cases;
int A[MAXN], B[MAXN], CC[MAXN];

int cc(int x, int y) {
	return x / y + ((x % y) ? 1 : 0);
}

int main() {
	scanf("%d", &cases);
	for(int xx = 1; xx <= cases; ++xx) {
		scanf("%d%d%d", &N, &C, &M);
		memset(A, 0, sizeof(A));
		memset(B, 0, sizeof(B));
		memset(CC, 0, sizeof(CC));
		for(int i = 0; i < M; ++i) {
			int x, y;
			scanf("%d%d", &x, &y);
			A[y]++;
			B[x]++;
		}
		// Pos prefix
		for(int i = 1; i <= N; ++i)
			CC[i] = CC[i - 1] + B[i];
		// People count
		int max1 = -1;
		for(int i = 1; i <= C; ++i)
			max1 = max(max1, A[i]);
		// Seat count
		int max2 = -1;
		for(int i = 1; i <= N; ++i)
			max2 = max(max2, cc(CC[i], i));
		int ans1 = max(max1, max2);
		int ans2 = 0;
		for(int i = 1; i <= N; ++i)
			if(B[i] > ans1) ans2 += B[i] - ans1;
		printf("Case #%d: %d %d\n", xx, ans1, ans2);
	}
}
