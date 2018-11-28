#include <stdio.h>
#include <string.h>

int T;

char in[2000];
int n, k;
int R;

int flip(int i, int k) {
	int j;
	for(j=0;j<k;j++) {
		if(in[i+j] == '-') in[i+j] = '+';
		else in[i+j] = '-';
	}
}

int foo(int C) {
	scanf("%s", in);
	scanf("%d", &k);
	n = strlen(in);
	int i, j;

	R = 0;

	for(i=0;i<=n-k;i++) {
		if(in[i] == '-') {
			flip(i, k);
			R++;
		}
	}

	for(;i<n;i++)
		if(in[i] == '-') R = -1;

	printf("Case #%d: ", C);
	if(R < 0) printf("IMPOSSIBLE\n");
	else printf("%d\n", R);
}

int main() {
	scanf("%d", &T);
	for(int i=0;i<T;i++) {
		foo(i+1);
	}
	return 0;
}

