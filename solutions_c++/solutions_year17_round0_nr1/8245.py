#include <stdio.h>
#include <string.h>

int T, N, K;
char A[1001];

void flip(int p){
	for(int i = p; i < p + K; i++){
		if(A[i] == '-')
			A[i] = '+';
		else
			A[i] = '-';
	}
}

void solve(int n){
	int flips = 0;
	scanf("%s %d", A, &K);
	N = strlen(A);
	for(int i = 0; i <= N - K; i++){
		if(A[i] == '-'){
			++flips;
			flip(i);
		}
	}
	for(int i = N - K + 1; i < N; i++){
		if(A[i] == '-'){
			printf("Case #%d: IMPOSSIBLE\n", n);
			return;
		}
	}
	printf("Case #%d: %d\n", n, flips);
}

int main(){
	freopen("P1.in", "r", stdin);
	freopen("P1.out", "w", stdout);
	scanf("%d", &T);
	for(int i = 1; i <= T; i++) solve(i);
	fclose(stdin);
	fclose(stdout);
}
