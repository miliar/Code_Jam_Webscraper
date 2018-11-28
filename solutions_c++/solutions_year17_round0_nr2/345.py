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
		string n;
		cin>>n;
		char prev='1';
		int chind=-1;
		bool drop=false;
		int le=n.size();
		for (int i=0;i<le;i++) {
			if (n[i]>prev) chind=i;
			else if (n[i]<prev) {
				drop=true;
				break;
			}
			prev=n[i];
		}
		cout<<"Case #"<<tc<<": ";
		if (drop) {
			if (chind==-1) {
				for (int i=0;i<le-1;i++) cout<<9;
			} else {
				for (int i=0;i<chind;i++) cout<<n[i];
				cout<<(char)(n[chind]-1);
				for (int i=chind+1;i<le;i++) cout<<9;
			}
		} else cout<<n;
		cout<<"\n";
	}
}
