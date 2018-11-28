#include<stdio.h>
#include<string.h>
#pragma warning(disable:4996)

char str[30];
char cmp[30];
int state[30];
long long int num;
long long int cmpnum;

int search(int n,int cur) {
	if (cur >= n) return 1;
	int m, i, j;
	cmp[cur] = str[cur];
	for (i = cur; i < n; i++) cmp[i] = cmp[cur];
	cmpnum = 0;
	for (i = 0; i < n; i++) {
		cmpnum *= 10;
		cmpnum += cmp[i];
	}
	if (cmpnum > num) {
		cmp[cur] -= 1;
		for (i = cur + 1; i < n; i++) cmp[i] = 9;
		return 0;
	}
	else search(n, cur + 1);
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int m, n, i, j, down,state;
	int t, ti;
	scanf("%d", &t);
	for (ti = 0; ti < t; ti++) {
		down = 0;
		state = 1;
		printf("Case #%d: ", ti + 1);
		scanf("%s", str);
		n = strlen(str);
		for (i = 0; i < n; i++) str[i] -= '0';
		num = 0;
		for (i = 0; i < n; i++) {
			num *= 10;
			num += str[i];
		}
		search(n, 0);
		cmpnum = 0;
		for (i = 0; i < n; i++) {
			cmpnum *= 10;
			cmpnum += cmp[i];
		}
		printf("%lld\n", cmpnum);

	}
	return 0;
}