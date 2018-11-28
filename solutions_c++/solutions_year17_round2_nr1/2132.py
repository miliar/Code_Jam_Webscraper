#include<stdio.h>
#define Max(a,b) (a > b ? a : b)
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt", "w", stdout);
	int t, test = 1;
	scanf("%d", &t);
	while (test <= t) {
		int D, N,K,M;
		scanf("%d %d", &D, &N);
		double max = 0;
		for (int i = 0; i < N; i++) {
			scanf("%d %d", &K, &M);
			max = Max(max,(double)(D - K) / (double)M);
		}
		printf("Case #%d: %lf\n", test++, ((double)D / max)+0.0000001);
	}
}