#include <bits/stdc++.h>

using namespace std;

#define N 1000

int k[N + 1];
int s[N + 1];

int main(){
	int tc, ic, d, n, i;
	double t;
	
	scanf("%d", &tc);
	
	for (ic = 1; ic <= tc; ic++){
		scanf("%d%d", &d, &n);

		for (i = 0; i < n; i++){
			scanf("%d%d", k + i, s + i);
		}

		t = 0.0;

		for (i = 0; i < n; i++){
			t = max(t, (double)(d - k[i]) / (double)s[i]);
		}

		printf("Case #%d: %.8lf\n", ic, (double)d / t);
	}

	return 0;
}