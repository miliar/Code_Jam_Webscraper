#include <cstdio>
#include <cstring>

int T, k;
char a[1010];

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%s", a+1);
		scanf("%d", &k);
		int len = strlen(a + 1);
		for (int i = 1; i <= len; i++) {
			if (a[i] == '+')a[i] = 0;
			else a[i] = 1;
		}
		int ans = 0;
		for (int i = 1; i <= len-k+1 ; i++) {
			if (a[i]) {
				for (int j = 0; j < k; j++) {
					a[i+j] = 1 - a[i+j];
				}
				ans++;
			}
		}
		int f = 0;
		for (int i = 1; i <= len; i++) {
			if (a[i]) {
				f = 1;
				break;
			}
		}
		printf("Case #%d: ", t);
		if(f)printf("IMPOSSIBLE");
		else printf("%d", ans);
		printf("\n");
	}
	return 0;
}