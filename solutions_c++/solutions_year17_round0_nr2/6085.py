#include <iostream>
#include <sstream>
#include <string>

using namespace std;

void dec_r(string& s, int i) {
	if (i == s.length()-1)
		return;
	dec_r(s, i + 1);
	while (s[i] > s[i+1]){
		for (int j = i+1; j<s.length(); ++j)
			s[j] = '9';

		if (s[i] == '0')
			s[i] = '9';
		else
			s[i]--;
	}
}

int main() {
	int T;
	cin >> T;
	int t = 0;
	while (++t <= T) {
		string s;
		cin >> s;

		string o = s;
		dec_r(o, 0);
		cout << "Case #" << t << ": " << o.substr(o[0]=='0'?1:0) << endl;
	}
	return 0;
}