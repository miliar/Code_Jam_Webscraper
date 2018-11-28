#include <bits/stdc++.h>
using namespace std;
int T, N;
double K[2000], S[2000], D;
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for(int Ks=1; Ks<=T; Ks++) {
		scanf("%lf%d", &D, &N);
		double m = 0;
		for(int i=0; i<N; i++) {
			scanf("%lf%lf", K+i, S+i);
			m = max(m, (D - K[i]) / S[i]);
		}
		printf("Case #%d: %.10f\n", Ks, D / m);
	}
}
