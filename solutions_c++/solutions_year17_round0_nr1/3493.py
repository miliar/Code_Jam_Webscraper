#include <stdio.h>
#include <bits/stdc++.h>
using namespace std;
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)
typedef long long ll;
typedef pair <int, int> pii;
typedef pair <long long, long long> pll;

char s[1005];
int main()
{
	int t, k, n, ok, cont;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++) {
		scanf(" %s %d", s, &k);
		cont = 0;
		n = strlen(s);
		for (int i = 0; i < n; i++) {
			if (i+k-1 >= n) break;
			if (s[i] == '+') continue;
			cont++;
			for (int j = i; j <= i+k-1; j++) {
				if (s[j] == '+') s[j] = '-';
				else s[j] = '+';
			}
		}

		ok = 1;
		for (int i = 0; i < n; i++) {
			if (s[i] == '-') {
				printf("Case #%d: IMPOSSIBLE\n", tt+1);
				ok = 0;
				break;
			}
		}
		if (ok) printf("Case #%d: %d\n", tt+1, cont);
	}

	return 0;
}