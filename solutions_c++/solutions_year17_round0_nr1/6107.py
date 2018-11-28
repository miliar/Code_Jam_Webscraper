#include<iostream>

using namespace std;

int main() {
	int t;
	cin>>t;
	for(int i=1;i<=t;i++) {
		string s;
		int n;
		cin>>s>>n;
		int len = s.length(), count = 0;
		for(int j=0;j <= len - n;j++) {
			if(s[j] == '-') {
				count++;
				for(int k=0;k<n;k++) {
					if(s[j+k] == '-') {
						s[j+k] = '+';
					}
					else {
						s[j+k] = '-';
					}
				}
			}
		}
		bool flag = true;
		for(int j=len-n+1;j<len;j++) {
			if(s[j] == '-') {
				flag = false;
				break;
			}
		}
		cout<<"Case #"<<i<<": ";
		if(flag) {
			cout<<count;
		}
		else {
			cout<<"IMPOSSIBLE";
		}
		cout<<endl;
	}
	return 0;
}