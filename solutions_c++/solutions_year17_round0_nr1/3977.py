#include <bits/stdc++.h>

using namespace std;

const int maxn = 1010;

int n, k;
char str[maxn];

int main() {
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	int T, tCase = 0;
	scanf("%d", &T);
	while(T --) {
		scanf("%s%d", str, &k);
		printf("Case #%d: ", ++tCase);
		n = strlen(str);
		int res = 0;
		for(int i = 0;i <= n-k;++ i) {
			if(str[i] == '-') {
				++ res;
				for(int j = i;j < i+k;++ j) {
					if(str[j] == '-')	str[j] = '+';
					else 	str[j] = '-';
				}
			}
		}
		for(int i = 0;i < n;++ i) if(str[i] == '-') {
			res = 1<<30;
			break;
		}
		if(res == (1<<30))
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", res);
	}
	return 0;
}