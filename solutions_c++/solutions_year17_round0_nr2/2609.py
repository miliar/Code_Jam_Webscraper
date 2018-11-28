#include <iostream>
#include <string>

using namespace std;

void makeTidier(string &s) {
	char last = *s.rbegin();
	for (auto rit = s.rbegin(); rit != s.rend(); ++rit) {
		if (*rit > last) {
			(*rit)--;
			for (auto it = (rit).base(); it != s.end(); ++it)
				*it = '9';
		}
		last = *rit;
	}
}




int main() {
	int tsts;
	cin >> tsts;
	for (int tst = 0; tst < tsts; ++tst) {
		string s;
		cin >> s;
		cout << "Case #" << tst+1 << ": ";
		makeTidier(s);
		if (*s.begin() == '0')
			s.assign(s, 1);
		cout << s << "\n";
	
	}
	return 0;
}