#include <bits/stdc++.h>
using namespace std;
#define MAXN 1005
int gauss(int n,int a[][MAXN],int b[]){
	for(int i = 0; i < n; i++) a[i][n] = b[i];

	// for(int ii = 0; ii < n; ii++) {
	// 	for(int jj = 0; jj < n; jj++)
	// 		printf("%d ", a[ii][jj]);
	// 	printf("  %d\n", a[ii][n]);
	// }
	// puts("------");

	for(int i = 0; i < n; i++) {
		// printf("%d\n",i+1);
		for(int j = i; j < n; j++)
			if(a[j][i] == 1) {
				swap(a[i], a[j]);
				break;
			}
		if(a[i][i] == 0) {
		 	for(int j = 0; j < i; j++)
		 		a[j][i] = 0;
		 	continue;
		}
		for(int j = 0; j < n; j++) 
			if(j != i && a[j][i] == 1) {
				for(int k = i; k < n + 1; k++)
					a[j][k] ^= a[i][k];
			}
	}
	int ret = 0;
	for(int i = n-1; i >= 0; i--) 
		if(a[i][i] == 1) {
			if(a[i][n] == 1)
				ret++;
		}
		else if(a[i][n] == 1) {
			return -1;
		}
	return ret;
}
int a[MAXN][MAXN];
int b[MAXN];
int main() {
	int T, k;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; cas++) {
		char s[MAXN];
		scanf("%s", s);
		scanf("%d", &k);
		int l = strlen(s);
		for(int i = 0; i <= l; i++)
			for(int j = 0; j <= l; j++)
				a[i][j] = 0;
		for(int i = 0; i < l; i++) {
			for(int j = max(0, i - (k-1)); j < min(l+1-k, i+1); j++)
				a[i][j] = 1;
			b[i] = s[i] == '-';
		}
		int ans = gauss(l, a, b);
		printf("Case #%d: ", cas);
		if (ans == -1)
			puts("IMPOSSIBLE");
		else
			printf("%d\n", ans);
	}
}