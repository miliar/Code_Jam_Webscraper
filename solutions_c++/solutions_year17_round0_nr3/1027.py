#include<stdio.h>
#pragma warning(disable:4996)

long long int max[100], min[100], maxcount[100], mincount[100];

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long int m, n, i, j, k;
	int t, ti;
	scanf("%d", &t);
	for (ti = 0; ti < t; ti++) {
		max[0] = 0, min[0] = 0;
		maxcount[0] = 0, mincount[0] = 0;
		printf("Case #%d: ", ti + 1);
		scanf("%lld %lld", &n, &k);
		if (k == 1) {
			printf("%lld %lld\n", n / 2, (n - 1) / 2);
			continue;
		}
		long long int count = 1;
		long long int cnum = 1;
		max[0] = n / 2, min[0] = (n - 1) / 2;
		maxcount[0] = 1, mincount[0] = 1;
		for (i = 0; count + 2*cnum < k; i++) {
			max[i + 1] = (max[i])/2;
			min[i + 1] = (min[i]-1)/2;
			maxcount[i + 1] = maxcount[i];
			mincount[i + 1] = mincount[i];
			if ((max[i] - 1) / 2 == min[i + 1]) mincount[i+1] += maxcount[i];
			else maxcount[i + 1] += maxcount[i];
			if (min[i] / 2 == min[i + 1]) mincount[i + 1] += mincount[i];
			else maxcount[i + 1] += mincount[i];
			cnum *= 2;
			count += cnum;
		}
		long long int ord = k - count;
		if (ord <= maxcount[i]) printf("%lld %lld\n", max[i] / 2, (max[i] - 1) / 2);
		else printf("%lld %lld\n", min[i] / 2, (min[i] - 1) / 2);
	}
	return 0;
}