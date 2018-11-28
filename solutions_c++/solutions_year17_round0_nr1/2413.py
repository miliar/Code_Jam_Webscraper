#include <bits/stdc++.h>
using namespace std;

void solve() {
	string s;
	int k,i,j;
	cin>>s>>k;
	int ctr=0;
	for(i=0;i<s.length()-k+1;i++) {
		if (s[i]=='-') {
			ctr++;
			for(j=i;j<k+i;j++) {
				s[j]=s[j]=='+'?'-':'+';
			}
		}
	}
	for(;i<s.length();i++) {
		if (s[i]=='-') break;
	}
	if (i==s.length()) {
		cout<<ctr<<'\n';
	} else cout<<"IMPOSSIBLE\n";
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