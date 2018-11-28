#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	ios::sync_with_stdio(false);
	cin>>t;
	for(int i=1;i<=t;i++) {
		string str;
		int k;
		cin>>str;
		cin>>k;
		int ans = 0;
		int l = str.length();
		// cout<<i<<endl;
		for(int j=0;j<l-k+1;j++) {
			if(str[j]=='-') {
				ans++;
				// cout<<j<<" "<<str<<endl;
				str[j] = '+';
				for(int p=j+1;p<l && p<j+k;p++) {
					if(str[p]=='-') {
						str[p] = '+';
					}else {
						str[p] = '-';
					}
				}
			}
		}
		bool flag = false;
		for(int j=0;j<l;j++) {
			if(str[j]=='-') {
				flag = true;
				break;
			}
		}
		if(flag) {
			cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
		} else {
			cout<<"Case #"<<i<<": "<<ans<<endl;
		}
		
	}
	return 0;
}
