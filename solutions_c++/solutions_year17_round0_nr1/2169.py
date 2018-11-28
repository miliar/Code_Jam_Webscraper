#include <cstdio>
#include <cstring>

int main() {
	
	int T,k,res;
	char s[1005];

	scanf("%d",&T);

	for (int tc = 1; tc <= T; tc++) {
		scanf("%s %d",s,&k);
		res = 0;
		for (int i = 0; i <= strlen(s)-k; i++) {
			if (s[i] == '-') {
				for (int j = i; j < i+k; j++) {
					if (s[j] == '-') {
						s[j] = '+';
					} else {
						s[j] = '-';
					}
				}
				res++;
			}
		}
		bool impossible = false;
		for (int i = 0; i < strlen(s); i++) {
			if (s[i] == '-') {
				impossible = true;
				break;
			}
		}

		printf("Case #%d: ", tc);
		if (impossible) {
			printf("IMPOSSIBLE\n");
		} else {
			printf("%d\n",res);
		}
	}

	return 0;
}