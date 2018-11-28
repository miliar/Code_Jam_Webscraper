#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int T, K;
char s[1010];

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		scanf("%s%d",s,&K);
		int cnt = 0, len = strlen(s);
		bool flag = false;
		for (int i = 0; s[i]; i++) if(s[i] == '-') {
			if(i+K > len) {
				flag = true;
				break;
			}
			cnt++;
			for (int j = 0; j < K; j++) {
				if(s[i+j] == '-') s[i+j] = '+';
				else s[i+j] = '-';
			} 
		} 
		printf("Case #%d: ", cas);
		if(flag) puts("IMPOSSIBLE");
		else printf("%d\n", cnt);
	}
	return 0;
}