#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	string s;
	cin >> t;
	for(int test = 1; test <= t; test++) {
		cin >> s;
		cout << "Case #" << test << ": ";
		if(s.size() == 1) {
			cout << s << endl;
			continue;
		}
		for(int i = 1; i < s.size(); i++) {
			if(s[i - 1] <= s[i])
				continue;
			for(int j = i; j < s.size(); j++)
				s[j] = '9';
			i -= 1;
			while(i >= 1 && s[i - 1] == s[i]) {
				s[i--] = '9';
			}
			s[i] = (char)(s[i] - 1);
			break;
		}
		if(s[0] == '0') cout << s.substr(1) << endl;
		else cout << s << endl;
	}	
}