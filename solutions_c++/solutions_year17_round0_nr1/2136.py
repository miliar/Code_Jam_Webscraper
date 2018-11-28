#include <cstdio>
#include <cstring>

char buf[2000];
int main(){
	freopen("A.in", "r", stdin);
	int T; scanf("%d", &T);
	for (int Tcase = 0; Tcase < T; Tcase++){
		printf("Case #%d: ", Tcase + 1);
		int k; scanf("%s%d", buf, &k);
		int n = strlen(buf);
		int cnt = 0;
		for (int i = 0; i < n; i++){
			if (buf[i] == '-') {
				if (i + k > n) {
					printf("IMPOSSIBLE\n");
					goto over;
				} else {
					for (int j = i; j < i + k; j++)
						if (buf[j] == '-')
							buf[j] = '+';
						else
							buf[j] = '-';
					cnt++;
				}
			}
		}
		printf("%d\n", cnt);
		over:;
	}
}