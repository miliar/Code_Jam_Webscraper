#include <iostream>
#include <string>

using namespace std;

bool is_tidy(string s, int slen)
{
	if (slen == 1)
		return true;

	for (int i = 0; i < slen - 1; i++)
		if (s[i] > s[i + 1])
			return false;

	return true;
}

string compute_tidy(string s)
{
	int n, carry = 0;
	int len = s.size();
	for (int i = len - 1; i >= 0; i--) {
		if (!is_tidy(s, i + 1)) {
			s[i] = '9';
			s[i - 1] -= 1;
		} else 
			return s;
	}
}

int main()
{
	int T;
	string s;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> s;
		if (is_tidy(s, s.size())) {
			cout << "Case #" << i + 1 << ": " << s << endl;
		} else {
			string o = compute_tidy(s);
			if (o[0] == '0')
				cout << "Case #" << i + 1 << ": " << o.substr(1) << endl;
			else
				cout << "Case #" << i + 1 << ": " << o << endl;
		}
	}
	return 0;
}
