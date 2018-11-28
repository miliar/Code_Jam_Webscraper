#include <bits/stdc++.h>
using namespace std;
#define fo(i,a,b) for (int i = (a); i < (b); i++)

int tc; int n;
char a[99], ans[99];
int main() {
	scanf("%d", &tc);
	fo(_,1,tc+1) {
		printf("Case #%d: ", _);
		scanf("%s", a);
		n = strlen(a);
		fo(i,0,n) ans[i] = '0';
		ans[n] = '\0';
		fo(i,0,n) {
			if (ans[i] >= a[i]) continue;
			fo(j,i,n) ans[j] = a[i];
			if (atoll(ans) > atoll(a)) {
				ans[i] = a[i]-1;
				fo(j,i+1,n) ans[j] = '9';
			}
		}
		if (ans[0]=='0') puts(ans+1);
		else puts(ans);
	}

	return 0;
}