#include <bits/stdc++.h>
using namespace std;

void solve() {
	string s;
	int i,j;
	cin>>s;
	for(i=0;i<s.length()-1;i++) {
		if (s[i]>s[i+1]) {
			s[i]--;
			break;
		}
	}
	for(j=i+1;j<s.length();j++) {
		s[j]='9';
	}
	for(j=i-1;j>=0;j--) {
		if (s[j]>s[j+1]) {
			s[j]--;
			s[j+1]='9';
		}
	}
	for(i=0;i<s.length() && s[i]=='0';i++);
	for(;i<s.length();i++) {
		cout<<s[i];
	}
	cout<<'\n';
}

int main(int argc, char const *argv[])
{
	ios::sync_with_stdio(false);
	int t,i;
	cin>>t;
	for(i=1;i<=t;i++) {
		cout<<"Case #"<<i<<": ";
		solve();
	}
	return 0;
}