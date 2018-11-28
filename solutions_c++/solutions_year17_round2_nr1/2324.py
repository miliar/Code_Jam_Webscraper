#include <bits/stdc++.h>

using namespace std;

int main() {
	int T, t, D, N, n, k, s, bk, bs;
	scanf("%d", &T);
	for(t = 0; t < T; ++t) {
		scanf("%d %d", &D, &N);
		bk = D;
		bs = 1;	
		for(n = 0; n < N; ++n) {
			scanf("%d %d", &k, &s);
			if(((D-k) / (double) s) > ((D-bk) / (double) bs)) {
				bk = k;
				bs = s;
			}
		}
		printf("Case #%d: %f\n", t+1, D / ((D-bk) / (double) bs));
	}
	return 0;
}