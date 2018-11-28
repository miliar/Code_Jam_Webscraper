#include <stdio.h>
#include <string.h>

int T;

int n;
long long int R;
char arr[40], res[40];

int f(int i, int t) {
	if(arr[i] < 0) return 1;
	int j;
	for(j=t?9:arr[i];j>=0&&(i==0||j>=arr[i-1]);j--) {
		res[i] = j;
		if(f(i + 1, t)) return 1;
		t = 1;
	}
	return 0;
}

int foo(int C) {
	scanf(" %s", arr);
	int len = strlen(arr);
	int i;
	for(i=0;i<len;i++)
		arr[i] = arr[i] - '0', res[i] = 0;
	arr[len] = -1;

	f(0, 0);

	printf("Case #%d: ", C);
	for(i=0;i<len;i++) if(res[i] != 0) break;
	for(;i<len;i++) printf("%d", res[i]);
	printf("\n");
}

int main() {
	scanf("%d", &T);
	for(int i=0;i<T;i++) {
		foo(i+1);
	}
	return 0;
}

