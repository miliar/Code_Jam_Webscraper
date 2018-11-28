#include <bits/stdc++.h>
using namespace std;
int main() {
	int T;
	cin>>T;
	int t = 1;
	while(T--) {
		string s;
		cin>>s;
		int len = s.size()-1;
		int carry = 0;
		for(int i=len; i>0; i--) {
			s[i]-=carry;
			if(s[i] >= s[i-1]) continue;
			else{
				for(int j=i; j<=len; j++)
					s[j] = '9';
				s[i-1]--;
				if(s[i-1] < '0') {
					carry = 1;
					s[i-1] = '9';
				}else {
					carry = 0;
				}
			}
		}
		string ans = "";
		int p = 0;
		while(s[p] == '0') p++;
		for(int j=p; j<=len; j++) ans+=s[j];
		cout<<"Case #"<< t <<": "<<ans<<"\n";
		t++;
	}
	return 0;
}