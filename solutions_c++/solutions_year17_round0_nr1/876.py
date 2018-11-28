
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	int tc, cn, K;
	char S[10000];
	scanf("%d", &tc);
	for(cn = 1; cn <= tc; cn++) {
		scanf("%s%d", S, &K);
		int ans = 0, valid = 1;
		int l = strlen(S);
		for(int i = 0; i + K <= l; i++)
			if(S[i] == '-') {
				ans++;
				for(int j = 0; j < K; j++)
					if(S[i + j] == '-')
						S[i + j] = '+';
					else
						S[i + j] = '-';
			}
		for(int i = l - K + 1; i < l; i++)
			if(S[i] == '-') {
				valid = 0;
				break;
			}
		printf("Case #%d: ", cn);
		if(valid)
			printf("%d\n", ans);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
