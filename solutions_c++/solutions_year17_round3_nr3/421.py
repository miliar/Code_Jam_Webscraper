#include <bits/stdc++.h>
using namespace std;

int T, N, K;
double U, P[55];

int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		scanf("%d %d %lf", &N, &K, &U);

		for(int i = 0; i < N; i++)
			scanf("%lf", &P[i]);
		P[N++] = 1.0;

		sort(P, P + N);

		double s = 0.0;
		for(int i = 0; i < N; i++){
			if(P[i] * i - s <= U){
				for(int j = 0; j < i; j++){
					U -= P[i] - P[j];
					P[j] = P[i];
				}
				s = P[i] * (i + 1);
			}else{
				for(int j = 0; j < i; j++)
					P[j] = (s + U) / i;
				break;
			}
		}

		double r = 1.0;
		for(int i = 0; i < N; i++)r *= P[i];

		printf("Case #%d: %.6f\n", t, r);
	}
	return 0;
}
