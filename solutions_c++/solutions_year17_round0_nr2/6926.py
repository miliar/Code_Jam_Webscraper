#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

string trim(string s) {
	return s[0] == '0' ? s.substr(1,s.length()-1) : s;
}

int getIndex(string s) {
	for(int i=0;i<s.length()-1;i++) {
		if(s[i]>s[i+1])	return i;
	}
	return -1;
}

int main() {
	// your code goes here
	int t;
	string s;
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);

	cin>>t;
	for(int T=0;T<t;T++) {
		cin>>s;
		s = trim(s);
		int index = getIndex(s);
		if(index >=0) {
			for(int i=index+1;i<s.length();i++) {
				s[i] = '9';
			}
			char c = s[index];
			int j = index;
			while(j>=0) {
				if(s[j] == c) {
					s[j]--;
					s[j+1] = '9';
				}
				else {
					break;
				}
				j--;
			}
			s = trim(s);
		}
		cout<<"Case #"<<(T+1)<<": "<<s<<endl;
	}
	return 0;
}