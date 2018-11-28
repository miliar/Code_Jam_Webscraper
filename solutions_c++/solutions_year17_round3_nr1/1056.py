#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

#define MaxN 1010
#define PI 3.14159265358979323846264338327950288419716939937510

int N, K;
pair<int, int> a[MaxN];

double best[MaxN][MaxN];

double getTop(const pair<int, int> &p) {
	return PI * (double)p.first * p.first;
}

double getSide(const pair<int, int> &p) {
	return 2.0 * PI * (double)p.first * p.second;
}

double probOk() {
	for (int i = 0; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			best[i][j] = -1;
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j <= K; j++) {
			if (best[i][j] < 0) {
				continue;
			}
			best[i + 1][j] = max(best[i + 1][j], best[i][j]);
			double increm = getSide(a[i]);
			if (j == 0) {
				increm += getTop(a[i]);
			}

			best[i + 1][j + 1] = max(best[i + 1][j + 1], best[i][j] + increm);
		}
	}
	return best[N][K];
}

void Solve() {
	scanf("%d %d", &N, &K);
	for (int i = 0; i < N; i++) {
		scanf("%d %d", &a[i].first, &a[i].second);
	}
	sort(a, a + N);
	reverse(a, a + N);
	printf("%.9f\n", probOk());
}

int main() {
	freopen("data.in", "rb", stdin);
	freopen("data.out", "wb", stdout);
	int tst;
	scanf("%d", &tst);
	for (int index = 1; index <= tst; index++) {
		fprintf(stderr, "Doing test %d\n", index);
		printf("Case #%d: ", index);
		Solve();
	}
	return 0;
}
