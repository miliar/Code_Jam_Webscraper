#include <bits/stdc++.h>
using namespace std;
int validate(int n) {
	string s = to_string(n);
	int flag = 0;
	for (int i=1;i<s.length();i++) {
		if(s[i] < s[i-1]) {
			return 0;
		}
	}
	return 1;
}
int main() {
	long long int t;
	cin>>t;
	for(long long int c = 1; c<=t; c++) {
		int n;
		cin>>n;
		int res = 0;
		while(n >= 0) {
			if(validate(n) == 1) {
				res = n;
				break;
			}
			n--;
		}
		cout<<"Case #"<<c<<": "<<res<<endl;
	}
	return 0;
}