#include <iostream>

using namespace std;

int main() {
	int cases;
	cin >> cases;
	for (int casei=0; casei<cases; casei++) {
		string s;
		cin >> s;
		int i=0;
		char last = '0';
		for (; i<s.size(); i++) {
			if (s[i] < last) {
				while (i > 0 && s[i-1] == last) i--;
				s[i]--;
				i++;
				break;
			}
			last = s[i];
		}
		for (; i<s.size(); i++) s[i] = '9';
		cout << "Case #" << casei+1 << ": ";
		i = 0;
		while (s[i] == '0') i++;
		for (; i<s.size(); i++) cout << s[i];
		cout << endl;
	}
}
