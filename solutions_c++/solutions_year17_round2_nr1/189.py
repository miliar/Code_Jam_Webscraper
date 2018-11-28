#include"stdio.h"
#include"algorithm"
using namespace std;
int T, D, N, K, S;
double Ans, MaxT;
int main() {
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.txt", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.txt", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%d%d", &D, &N);
		MaxT = 0;
		for (int i = 0; i < N; i++) {
			scanf("%d%d", &K, &S);
			MaxT = max(MaxT, 1. * (D-K) / S);
		}
		Ans = 1. * D / MaxT;
		printf("Case #%d: %lf\n", t, Ans);
	}
}
