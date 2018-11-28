#include <stdio.h>
#include <string>

using namespace std;

int solve(string s, int K) {
	int cur;
	int len=s.length();
	int i;
	for (i=0; i<len; i++) 
		if (s[i] == '-') break;
	
	if (i==len) return 0;

	cur = i;
	int ans = 0;
	while (cur!=len) {
		int tmp=cur;
		int cnt=0;
		for (int i=0; i<K; i++) {
			if (tmp+i>=len) return -1;
			if (s[tmp+i]=='-') s[tmp+i]='+';
			else {
				if (!cnt) {
					cur=tmp+i;
					cnt=1;
				}
				s[tmp+i]='-';
			}
		}
		ans++;
		if (!cnt) {
			cur=len;
			for (int i=tmp+K; i<len; i++) {
				if (s[i]=='-') {
					cur=i;
					break;
				}
			}
		}
	}
	return ans;
}

int main() {

	int T;
	int K;	
	char s[2000];

	scanf("%d", &T);

	for (int i=0; i<T; i++) {
		scanf("%s%d", s, &K);
		int ans=solve(s, K);
		if (ans >= 0) printf("Case #%d: %d\n", i+1, ans);
		else printf("Case #%d: IMPOSSIBLE\n", i+1);
	}

	return 0;
}
