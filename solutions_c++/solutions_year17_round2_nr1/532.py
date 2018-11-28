#include <cstdio>

int K[1111], S[1111];
int N, D;


void work(){
	scanf("%d%d", &D, &N);

	double speed = 1e100;

	for (int i = 0; i < N; i++){
		scanf("%d%d", K + i, S + i);
		double t = (D - K[i]) / (double)S[i];
		double s = D / t;
		if (s < speed)
			speed = s;
	}
	
	printf("%f\n", speed);
}

int main(){
	freopen("A.in", "r", stdin);
	int Tcase; scanf("%d", &Tcase);
	for (int T = 1; T <= Tcase; T++){
		printf("Case #%d: ", T);
		work();
	}
}