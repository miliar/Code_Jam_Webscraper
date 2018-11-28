#include <bits/stdc++.h>
using namespace std;
int main() {
	int t;
	cin >> t;
	for(int k = 0; k < t; ++k) {
		string s;
		cin >> s;
		for(int i = 0; i < s.size() - 1; ++i) {
			if(s[i] > s[i + 1]) {
				for(int j = i + 1; j < s.size(); ++j) 
					s[j] = '9';
				while(i >= 1 && s[i] == s[i - 1]) {
					s[i] = '9';
					i--;
				}
				s[i] = s[i] - 1;
				break;
			}
		}
		int i = 0;
		cout << "Case #" << k + 1 << ": ";
		while(s[i] == '0')
			i++;
		for(; i < s.size(); ++i)
			cout << s[i];
		cout << endl;
	}

}