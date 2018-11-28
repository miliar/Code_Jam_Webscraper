#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const *argv[])
{
	int n, cas, k, i, ans;
	string s;

	cin >> n;
	cas = 1;
	while (n) {
		cin >> s;
		i = 0;
		if (s.length() > 1)
		{
			i++;
			while (i < s.length()) {
				while (i < s.length() && s[i] >= s[i-1]) i++;
				if (i == s.length()) continue;
				else {
					i--;
					while (i > 0 && s[i-1] == s[i]) i--;
					if (s[i] == 0) i++;
					s[i]--;
					i++;
					while (i < s.length()) {
						s[i] = '9';
						i++;
					}
				}
			}
		}
		cout << "Case #" << cas++ << ": ";
		i = 0;
		while (s[i] == '0') i++;
		for (; i < s.length(); i++) cout << s[i];
		cout << endl;
		n--;
	}

	return 0;
}