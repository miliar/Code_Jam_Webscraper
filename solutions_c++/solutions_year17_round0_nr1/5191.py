#include <cstdio>
#include <cstring>
#include "A.h"
//using namespace A;
namespace A {
	int n, k;
	char str[1111];
	void input() {
		scanf("%s%d", str, &k);
	}
	void solve() {

		n = strlen(str);
		int cnt = 0;
		for (int i = 0; i <= n - k; i++) {
			if (str[i] == '-') {
				cnt++;
				for (int j = i; j < i + k; j++) {
					if (str[j] == '-')
						str[j] = '+';
					else
						str[j] = '-';
				}
				//puts(str);
			}
		}
		for (int i = 0; i < n; i++)
			if (str[i] == '-') {
				printf("IMPOSSIBLE\n");
				return;
			}
		printf("%d\n", cnt);
	}

	void main() {
		int zz;
		scanf("%d", &zz);
		for (int kase = 1; kase <= zz; kase++) {
			input();
			printf("Case #%d: ", kase);
			solve();
		}
	}
}