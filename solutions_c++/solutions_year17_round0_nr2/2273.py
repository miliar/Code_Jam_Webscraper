#include <bits/stdc++.h>
using namespace std;
int T, n;
char s[100];
void solve(int test) {
	memset(s, 0, sizeof s);
	scanf("%s", s);
	n=strlen(s);
	for (int i=1; i<n; i++) {
		if (s[i]<s[i-1]) {
			int j=i-1;
			while (j-1>=0&&s[j-1]==s[j])j--;
			s[j]--;
			for (int k=j+1; k<n; k++) s[k]='9';
			bool st=false;
			printf("Case #%d: ", test);
			for (int k=0; k<n; k++) {
				if (s[k]!='0') st=true;
				if (st) printf("%c", s[k]);
			}
			printf("\n");
			return;
		}
	}
	printf("Case #%d: %s\n", test, s);
}
int main () {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
	for (int i=1; i<=T; i++) {
		solve(i);
	}
	return 0;
}
