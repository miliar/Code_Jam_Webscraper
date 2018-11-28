#include<bits/stdc++.h>
#include<algorithm>
using namespace std;

int D, N, K, S;

int main()
{
	int T, kase = 0;
	scanf("%d", &T);

	while(T--) {
		double maxi = 0.0;
		scanf("%d%d", &D, &N);
		for(int i = 0; i < N; i++) {
			scanf("%d%d", &K, &S);
			double tmp = D-K;
			tmp = tmp/S;
			maxi = max(maxi, tmp);
		}

		printf("Case #%d: %lf\n", ++kase, D/maxi);
	}

	return 0;
}
