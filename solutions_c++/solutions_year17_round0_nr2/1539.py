#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)n; i++)
#define vec vector
#define ll long long

int main(void)
{
	int T;
	cin >> T;
	rep(t, T) {
		string s;
		cin >> s;
		int i = 1;
		while(i < (int)s.length() && (int)s[i - 1] <= (int)s[i]) {
			i++;
		}
		cout << "Case #" << t + 1 << ": ";
		if (i == (int)s.length()) {
			cout << s << endl;
			continue;
		}

		string e = "";
		rep(i, s.length() - 1) e += '9';
		for (int j = (int)s.length() - 1; j >= i; j--) s[j] = '9';
		for (int j = i - 1; j >= 0; j--) {
			s[j]--;
			s[j + 1] = '9';
			if (j == 0 && s[j] == '0') {
				s = e;
				break;
			}
			if (j == 0 || s[j] >= s[j - 1]) break;
		}
		cout << s << endl;

	}
	return 0;
}
