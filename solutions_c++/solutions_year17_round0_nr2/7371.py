#include <cstdio>
#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t;
	cin>>t;
	for(int cas=1;cas<=t;cas++) {
		string s;
		cin>>s;
		int i=1;
		for(i=1;i<s.length();i++) {
			if(s[i-1]>s[i]) {
				break;
			}
		}
		if(s.length() == i) {
			cout<<"Case #"<<cas<<": "<<s<<endl;
			continue;
		}
		for(int j=0;j<s.length();j++) {
			if(s[j] == s[i-1]) {
				s[j] = s[j]-1;
				i = j+1;
				break;
			}
		}
		for(int j=i;j<s.length();j++) {
			s[j] = '9';
		}
		int leadingzero = 0;
		for(int j=0;j<s.length();j++) {
			if(s[j] != '0') break;
			leadingzero++;
		}
		cout<<"Case #"<<cas<<": "<<s.substr(leadingzero)<<endl;
	}
}