#include <bits/stdc++.h>

using namespace std;

char s[1005];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int cas = 1;  cas <= T; ++ cas) {
		int n, k;
		scanf("%s%d", s, &k);
		n = strlen(s);
		int ans = 0;
		for(int i = 0; i + k - 1 < n; ++ i) {
			if(s[i] == '+')
				continue;
			++ ans;
			for(int j = i; j <= i + k - 1; ++ j)
				s[j] = s[j] == '+' ? '-' : '+';
		}
		bool flag = true;
		for(int i = 0; i < n; ++ i)
			if(s[i] == '-')
				flag = false;
		printf("Case #%d: ", cas);
		if(!flag)
			puts("IMPOSSIBLE");
		else
			printf("%d\n", ans);

	}
	return 0;
}