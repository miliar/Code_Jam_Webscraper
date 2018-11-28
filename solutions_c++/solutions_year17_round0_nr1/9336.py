#include <iostream>
#include <string>

using namespace std;

int flip(int k, int start, string& s) {
	int next = start + 1;
	for (int i = k - 1; i >= 0; i--) {
		s[start + i] = (s[start + i] == '-') ? '+' : '-';
		if (s[start + i] == '-') next = start + i;
	}

	return next;
}

bool checkUp(string& s) {
	for (int i = 0; i < s.length(); i++) {
		if (s[i] == '-') {
			return false;
		}
	}
	return true;
}

int main()
{
    int n;
	cin >> n;

	for (int cases = 0; cases < n; cases++) {
		string s;
		cin >> s;
		int k;
		cin >> k;

		 // if all pancakes are all happy
		if (checkUp(s)) cout << "Case #" << cases + 1 << ": 0" << endl;
		else {
			int j = 0;
			int count = 0;
			while (j <= s.length() - k) {
				if (s[j] == '-') {
					j = flip(k, j, s);
					count += 1;
				}
				else j += 1;
			}
			if (checkUp(s)) cout << "Case #" << cases + 1 << ": " << count << endl;
			else cout << "Case #" << cases + 1 << ": IMPOSSIBLE" << endl;
		}
	}
    return 0;
}
