#include <bits/stdc++.h>
using namespace std;

int t;
char s[1234];
int k, l;
int ans;

int main()
{
scanf("%d\n", &t);
for(int q=1; q<=t; q++) {
	scanf("%s %d\n", s, &k);
	l=strlen(s);
	ans=0;
	for(int i=0; i<=l-k; i++) {
		if(s[i]=='-') {
			ans++;
			for(int j=i; j<i+k; j++) {
				if(s[j]=='-') s[j]='+';
				else s[j]='-';
			}
		}
	}
	int ok=1;
	for(int i=0; i<l; i++) {
		if(s[i]=='-') ok=0;
	}
	if(ok) printf("Case #%d: %d\n", q, ans);
	else printf("Case #%d: IMPOSSIBLE\n", q);
}

	return 0;
}
