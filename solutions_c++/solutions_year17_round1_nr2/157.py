#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>


int N, P;
int R[100];
int Q[100][100]; /* [N][P] */
int S[100][100][2];
int v[100];

int ans;

#define MIN(X, Y) ((X)<(Y)?(X):(Y))
#define MAX(X, Y) ((X)>(Y)?(X):(Y))

int f(int i=0, int l=0, int h=999999) {
	if(i >= N) return 1;
	
	int j;
	for(j=v[i]+1;j<P;j++) {
		if(l <= S[i][j][1] && h >= S[i][j][0] && S[i][j][0]<=S[i][j][1]) {
			if(f(i + 1, MAX(l, S[i][j][0]), MIN(h, S[i][j][1]))) {
				v[i] = j;
				return 1;
			}
		}
	}
	return 0;
}

/* Real Main */
void ___() {
	int i, j;
	scanf("%d %d", &N, &P);
	for(i=0;i<N;i++) scanf("%d", &R[i]);
	for(i=0;i<N;i++) {
		for(j=0;j<P;j++) {
			scanf("%d", &Q[i][j]);
		}
	}

	for(i=0;i<N;i++) std::sort(Q[i], Q[i] + P);

	ans = 0;
	for(j=0;j<P;j++) {
		int ll, hh;
		for(i=0;i<N;i++) {
			hh = floor((double)Q[i][j] * 10 / 9 / R[i]);
			ll = ceil((double)Q[i][j] * 10 / 11 / R[i]);
			S[i][j][0] = ll;
			S[i][j][1] = hh;
		}
	}

	for(i=0;i<N;i++) v[i] = -1;
	for(i=0;i<P;i++) {
		ans += f();
	}

	printf("%d\n", ans);
}



/* Fake Main */
int main() {
	int T, i;
	/* Test Case */
	scanf("%d", &T);
	for(i=0;i<T;i++) {
		printf("Case #%d: ", i + 1);
		___();
	}
	return 0;
}
