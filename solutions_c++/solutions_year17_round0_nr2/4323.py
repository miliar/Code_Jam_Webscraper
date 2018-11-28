#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

void solve() {
	char s[100];
	scanf("%s",s);
	int l = strlen(s);
	int t = -1, p, st = 0;
	for (int i=0;i<l-1;i++) {
		if (s[i]>s[i+1]) {
			t = i; break;
		}
	}
	if (t<0) {
		printf("%s\n",s);
		return;
	}
	for (int i=t;i>=0;i--) {
		s[i]--;
		p = i;
		if (i>0 && s[i-1]<=s[i])
			break;
	}
	for (int i=p+1;i<l;i++) {
		s[i] = '9';
	}
	for (int i=0;i<l;i++) {
		if (s[i]=='0') st++;
	}
	printf("%s\n",s+st);
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