#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int test,tc=1;
	cin >> test;
	while(test--) {
		string s;
		cin >> s;
		printf("Case #%d: ",tc++);
		int l = s.length();
		bool flag=0;
		for (int i=0;i<l-1;i++) {
			if(s[i]>s[i+1]) {
				flag=1;
				break;
			}
		}
		if(flag) {
			s = "0" + s;
			l = s.length();
			int c;
			for (int i=0;i<l;i++) {
				if(s[i]>s[i+1]) {
					c = i;
					break;
				}
			}
			
			s[c] = s[c]-1;
			int d=c;
			for (int i=c-1;i>=0;i--) {
				while(s[i]>s[i+1]) {
					d=i;
					s[i]--;
				}
			}
			for (int i=d+1;i<l;i++) {
				s[i] = '9';
			}
			string ans="";
			int i=0;
			for (;i<l;i++) if(s[i]!='0') break;
			for (;i<l;i++) ans += s[i];
			cout << ans << endl;
		}
		else cout << s << endl;
		
		
		
	}
	
}
