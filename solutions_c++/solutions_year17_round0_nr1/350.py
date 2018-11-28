#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int tcs;
	cin>>tcs;
	for (int tc=1;tc<=tcs;tc++) {
		string s;
		int k;
		cin>>s>>k;
		int n=s.size();
		int cntr=0;
		for (int j=0;j+k<=n;j++) {
			if (s[j]=='-') {
				cntr++;
				for (int i=j;i<j+k;i++) {
					if (s[i]=='+') s[i]='-';
					else s[i]='+';
				}
			}
		}
		cout<<"Case #"<<tc<<": ";
		bool ok=true;
		for (int i=0;i<n;i++) {
			if (s[i]=='-') ok=false;
		}
		if (ok) cout<<cntr<<"\n";
		else cout<<"IMPOSSIBLE\n";
	}
}
