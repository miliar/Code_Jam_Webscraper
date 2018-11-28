#include <bits/stdc++.h> 
using namespace std;
int main() {
	int t;
	cin >> t;
	for(int h=1;h<=t;h++) {
		string s;
		cin >> s;
		int carry = 0;
		for(int i=s.size()-1;i>0;i--) {
			int num = s[i]-'0';
			num += carry;
			carry = 0;
			if(num<s[i-1]-'0' || num<1) {
				s[i] = '9';
				for(int j=i+1;j<s.size();j++) {
					if(s[j]<s[j-1]) {
						s[j] = s[j-1];
					} else break;
				}
				carry = -1;
			} else s[i] = num+'0';
		}
		s[0]+=carry;
		if(s[0]-'0'<1) s.erase(s.begin());
		cout << "Case #" << h << ": " << s << endl;
	}
}

