#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

inline char change(char c) {
	if (c=='-') return '+';
	return '-';
}

void solve() {
	char s[1005];
	int k,ans=0;
	scanf("%s%d",s,&k);
	int l = strlen(s);
	for (int i=0;i<l-k+1;i++) {
		if (s[i]=='-') {
			ans++;
			for (int j=i;j<i+k;j++)
				s[j] = change(s[j]);
		}
	}
	for (int i=l-k+1;i<l;i++) {
		if (s[i]=='-') {
			printf("IMPOSSIBLE\n");
			return;
		}
	}
	printf("%d\n",ans);
}

int main() {
	int tt;
	cin>>tt;
	for (int cs=1;cs<=tt;cs++){
		printf("Case #%d: ",cs);
		solve();
	}

	return 0;
}