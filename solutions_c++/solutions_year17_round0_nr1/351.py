#include <bits/stdc++.h>
using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	
	for (int tt=1; tt<=T; ++tt) {
		int K, N;
		char temp[1005];
		scanf("%s%d", temp, &K);
		N = strlen(temp);

		int ans = 0;
		for (int i=0; i<N-(K-1); ++i) {
			if (temp[i] == '-') {
				++ans;
				for (int j=0; j<K; ++j)
					temp[i+j] = '+' + '-' - temp[i+j];
			}
		}

		int i;
		for (i=0; i<N; ++i)
			if (temp[i] == '-')
				break;

		printf("Case #%d: ", tt);
		if (i == N) printf("%d\n", ans);
		else printf("IMPOSSIBLE\n");
	}

	return 0;
}

