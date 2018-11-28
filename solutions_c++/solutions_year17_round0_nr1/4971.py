#include <bits/stdc++.h>
using namespace std;

int T;
char s[2005];

void flip(int st, int k){
	for(int i=st; i<st+k; i++){
		s[i] = ((s[i] == '+') ? '-' : '+');
	}
}

int main() {
	scanf("%d", &T);
	for(int t=0; t<T; t++){
		int n;
		scanf("%s %d", &s, &n);
		int ss = strlen(s), cnt = 0, i;
		for(i=0; i<=ss-n; i++){
			if(s[i] == '-'){
				flip(i, n);
				cnt++;
			}
		}
		bool ok = true;
		for(;i<ss; i++) {
			if(s[i] == '-') {
				ok = false;
				break;
			}
		}
		if(ok)
			printf("Case #%d: %d\n", t+1, cnt);
		else
			printf("Case #%d: IMPOSSIBLE\n", t+1);

	}
}
