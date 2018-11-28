#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double Double;
char S[1005];
int main() {
	int TC;
	scanf("%d", &TC);
	for (int cn = 1; cn <= TC; ++cn) {
		int K, ans = 0;
		scanf("%s%d", S, &K);
		int n = strlen(S);
		for (int i = 0; i + K <= n; ++i) {
			if (S[i] == '-') {
				for (int j = i; j < i + K; ++j)
					S[j] = S[j] == '+' ? '-' : '+';
				++ans;
			}
		}
		bool bad = false;
		for (int i = 0; i < n; ++i)
			if (S[i] == '-') {
				bad = true;
				break;
			}
		printf("Case #%d: ", cn);
		if (bad) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
}

