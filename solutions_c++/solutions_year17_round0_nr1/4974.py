#include <iostream>
#include <string>
using namespace std;

int main() {
	int T;	cin>>T;
	
	for (int t = 1; t <= T; ++t) {
		string s;	cin>>s;
		int k;		cin>>k;
		int len = s.length();
		int cnt = 0;
		for (int i = 0; i <= len-k; ++i) {
			//cout<<s<<endl;
			if (s[i] == '-') {
				cnt++;
				for (int j = 0; j < k; ++j) {
					if (s[i+j] == '-')
						s[i+j] = '+';
					else
						s[i+j] = '-';
				}
			}
		}
		bool ok = true;
		for (int i = len-k; i < len; ++i)
			if (s[i] == '-') {
				ok = false;
				break;
			} 
		
		cout<<"Case #"<<t<<": ";
		if (ok)
			cout<<cnt<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
	}
	
	return 0;
}
