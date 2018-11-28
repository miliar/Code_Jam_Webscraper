#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
	char s[10005];
	int T; scanf("%d",&T);
	for (int t=1;t<=T;++t) {
		int k;
		scanf("%s%d",s,&k);
		bool impossible=false;
		int cnt=0;
		for (int i = 0; s[i]; ++i) {
			if (s[i] == '-') {
				for (int j=0;j<k;++j) {
					if (!s[i+j]) {
						impossible=true;
						break;
					} else if (s[i+j]=='-') s[i+j]='+';
					else s[i+j]='-';
				}
				++cnt;
			}
			if(impossible)break;
		}

		printf("Case #%d: ",t);
		if (impossible) {
			puts("IMPOSSIBLE");
		} else {
			printf("%d\n",cnt);
		}
	}
	return 0;
}
