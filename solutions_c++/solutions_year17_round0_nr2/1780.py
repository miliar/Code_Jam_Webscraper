#include <iostream>
#include <string>

using namespace std;
int checkZero(string s) {
	for (int i = 0; i < s.length(); i++) {
		if (s[i] == '0') return 1;
	}
	return 0;
}
int main()
{
	int t, ct;
	freopen("a.in", "r", stdin);
	cin >> ct;
	for (t = 1; t <= ct; t++)
	{
		cout << "Case #" << t << ": ";
		string s;
		cin >> s;
		if (s == "0") {
			cout << s << endl;
			continue;
		}
		
		for (int i = s.length()-1; i >0; i--) {
			if (s[i] < s[i - 1]) {
				s[i - 1]--;
				for (int j = i; j < s.length(); j++) {
					s[j] = '9';
				}
			}
		}
		for (int i = 0; i < s.length(); i++) {
			if (s[i] == '0') continue;
			cout << s[i];
		}
		cout << endl;
		//cout << s << endl;
	}
	return 0;
}
