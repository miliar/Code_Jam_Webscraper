#include <bits/stdc++.h>
using namespace std;

const int maxn = 1010;
char s[maxn];

int main() {
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T, kase = 0;
	scanf("%d",&T);
	while (T--) {
		int k;
		scanf("%s%d",s,&k);
		int cnt = 0;
		int len = strlen(s);
		for (int i = 0; i + k - 1 < len; i++) {
			if (s[i] == '-') {
				cnt++;
				for (int j = i; j <= i + k - 1; j++) {
					if (s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
			}
		}
		bool ok = true;
		for (int i = 0; i < len; i++) {
			if (s[i] == '-') {
				ok = false;
				break;
			}
		}
		if (!ok) printf("Case #%d: IMPOSSIBLE\n",++kase);
		else printf("Case #%d: %d\n",++kase,cnt);
	}
	return 0;
}
