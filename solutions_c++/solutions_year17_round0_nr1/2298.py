#include <bits/stdc++.h>
using namespace std;
int T, n, k;
char s[1005];
void solve(int test) {
	memset(s, 0, sizeof s);
	scanf("%s %d", s, &k);
	n=strlen(s);
	int res=0;
	for (int i=0; i+k-1<n; i++) {
		if (s[i]=='-') {
			res++;
			for (int j=i; j<=i+k-1; j++) {
				if (s[j]=='+') s[j]='-';
				else s[j]='+';
			}
		}
	}
	bool ok=true;
	for (int i=0; i<n; i++) if (s[i]=='-') ok=false;
	printf("Case #%d: ", test);
	if (!ok) printf("IMPOSSIBLE\n");
	else printf("%d\n", res);
}
int main () {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for (int i=1; i<=T; i++) {
		solve(i);
	}
	return 0;
}
