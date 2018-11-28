#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int test,tc=1;
	cin >> test;
	while(test--) {
		int cnt=0;
		string s;
		int k;
		cin >> s >> k;
		int l = s.length();
		for (int i=0;i<=l-k;i++) {
			if(s[i]=='-') {
				for (int j=0;j<k;j++) {
					if(s[i+j]=='-') s[i+j]='+';
					else s[i+j] = '-';
				}
				cnt++;
			}
		}
		int i=0;
		for (i=0;i<l;i++) if(s[i]=='-') break;
		  
		printf("Case #%d: ",tc++);
		if(i==l) cout << cnt << endl;
		else puts("IMPOSSIBLE");
	}
	
}
