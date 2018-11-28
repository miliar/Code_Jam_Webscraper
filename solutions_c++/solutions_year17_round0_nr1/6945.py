#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

char flip(char c) {
	if(c=='-')	return '+';
	return '-';
}

int main() {
	// your code goes here
	int t,k;
	string s;
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);

	cin>>t;
	for(int T=0;T<t;T++) {
		cin>>s>>k;
		int w = 0 , c = 0;
		for(int i=0;i<s.length()-k+1;i++) {
			if(s[i]=='-') {
				c++;
				for(int j=i;j<i+k;j++) {
					s[j] = flip(s[j]);
				}
			}
		}
		for(int i = s.length()-k+1;i<s.length();i++) {
			if(s[i] == '-') {
				c = -1;
				break;
			}
		}
		if(c==-1)
			cout<<"Case #"<<(T+1)<<": IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<(T+1)<<": "<<c<<endl;
	}
	return 0;
}