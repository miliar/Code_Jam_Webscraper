#include <bits/stdc++.h>

int main() {
	int T;
	scanf("%d", &T);
	int t = 1;
	while(T--) {
		int D, N;
		scanf("%d %d", &D, &N);
		float max_time = -1;
		while (N--) {
			int K, S;
			scanf("%d %d", &K, &S);
			float time = (D - K) * 1.0 / S;
			if (time > max_time)
				max_time = time;
		}
		printf("Case #%d: %f\n", t, D * 1.0 / max_time);
		t++;
	}
	return 0;
}