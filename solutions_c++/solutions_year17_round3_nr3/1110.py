#include<cstdio>
#include<algorithm>
using std::sort;
const int maxn = 50 + 10;

int N, K;
double X, P[maxn];

int main()
{
	int T, kase=0;
	scanf("%d", &T);

	while(T--) {
		scanf("%d%d%lf", &N, &K, &X);
		for(int i = 0; i < N; i++) scanf("%lf", &P[i]);
		sort(P, P+N);

		for(int i = 0; i < N-1; i++) {
			double a = (i+1)*(P[i+1] - P[i]);
			if(X > a) {
				for(int j = 0; j <= i; j++) P[j] += P[i+1]-P[j];
				X -= a;
			} else {
				for(int j = 0; j <= i; j++) P[j] += X/(i+1);
				X = 0;
				break;
			}
		}
		if(X > 0) for(int j = 0; j < N; j++) P[j] += X/N;

		double AI = 1.0;
		for(int i = 0; i < N; i++) AI *= P[i];

		printf("Case #%d: %lf\n", ++kase, AI);
	}

	return 0;
}
