#include <cstdio>
#include <memory.h>

int N, C, M;
int A[1001];
int B[1001];
int R[1001];

int max(int a, int b) { return a > b ? a : b; }
int min(int a, int b) { return a < b ? a : b; }

int assign(int op) {
	memset(R, 0, sizeof(R));
	int promo = 0;
	for (int i = 1; i <= N; ++i) {
		R[i] = R[i - 1] + op;
		if (R[i] < A[i]) {
			return -1;
		} else {
			promo += max(0, A[i] - op);
			R[i] -= A[i];
		}
	}
	return promo;
}

int main() {
	int TC;
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; ++tc) {
		memset(A, 0, sizeof(A));
		memset(B, 0, sizeof(B));
		scanf("%d%d%d", &N, &C, &M);
		int maxb = 0;
		for (int i = 0; i < M; ++i) {
			int p, b;
			scanf("%d%d", &p, &b);
			A[p]++;
			B[b]++;
			maxb = max(maxb, B[b]);
		}
		int minop = max((M + N - 1) / N, maxb);
		int lb = minop;
		int ub = M;
		int ans1 = 0;
		int ans2 = 0;
		while (lb <= ub) {
			int mid = (lb + ub) / 2;
			int pro = assign(mid);
			if (pro >= 0) {
				ans1 = mid;
				ans2 = pro;
				ub = mid - 1;
			} else {
				lb = mid + 1;
			}
		}
		printf("Case #%d: %d %d\n", tc, ans1, ans2);
	}
	return 0;
}

