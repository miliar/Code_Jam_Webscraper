#include <iostream>

using namespace std;

int main() {
	int tc;
	cin >> tc;
	for(int t = 0; t < tc; ++t) {
		string s;
		cin >> s;
		
		s = "00" + s;
		int i = 0;
		while(i < (int)s.size() - 1 && s[i] <= s[i + 1]) {
			++i;
		}
		if(i != (int)s.size() - 1) {
			while(i > 0 && s[i] == s[i - 1]) --i;
			--s[i];
			++i;
			while(i < (int)s.size()) {
				s[i] = '9';
				++i;
			}
		}
		while(s[0] == '0') s = s.substr(1);
		
		cout << "Case #" << t + 1 << ": " << s << '\n';
	}
	
	return 0;
}
