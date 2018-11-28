#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

int r, c;
char in[30][30];

/* Real Main */
void ___() {
	int i;
	int n;
	scanf("%d %d", &r, &c);
	for(i=0;i<r;i++) {
		scanf(" %s", in[i]);
	}
	int v[30] = {0};

	int j, k, l;
	for(i=0;i<r;i++) {
		k = 0;
		l = -1;
		v[i] = 1;
		for(j=0;j<c;j++) {
			if(in[i][j] != '?') {
				v[i] = 0;
				for(k=j-1;k>=0&&in[i][k] == '?';k--) {
					in[i][k] = in[i][j];
				}
				l = j;
			}
		}
		if(!v[i]) {
			for(k=j-1;k>=0&&in[i][k] == '?';k--) {
				in[i][k] = in[i][l];
			}
		}
	}

	for(i=1;i<r;i++) {
		if(v[i] && !v[i-1]) {
			for(j=0;j<c;j++) in[i][j] = in[i-1][j];
			v[i] = 0;
		}
	}
	for(i=r-2;i>=0;i--) {
		if(v[i] && !v[i+1]) {
			for(j=0;j<c;j++) in[i][j] = in[i+1][j];
			v[i] = 0;
		}
	}

	printf("\n");
	for(i=0;i<r;i++) {
		printf("%s\n", in[i]);
	}
}



/* Fake Main */
int main() {
	int T, i;
	/* Test Case */
	scanf("%d", &T);
	for(i=0;i<T;i++) {
		printf("Case #%d:", i + 1);
		___();
	}
	return 0;
}
