#include <bits/stdc++.h>

using namespace std;
int t;
string s;
int k;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin>>t;
	for(int c=1;c<=t;++c) {
		cin>>s>>k;
		int n = s.length();
		int cnt = 0;
		for(int i=0;i<n-k+1;++i) {
			if(s[i]=='-') {
				cnt++;
				for(int j=i;j<i+k;++j) {
					if(s[j]=='-') s[j]='+';
					else s[j]='-';
				}
			}
		}
		for(int i=0;i<n;++i) {
			if(s[i]=='-')
				cnt=-1;
		}
		if(cnt==-1) cout<<"Case #"<<c<<": IMPOSSIBLE\n";
		else cout<<"Case #"<<c<<": "<<cnt<<"\n";
	}

	return 0;
}
