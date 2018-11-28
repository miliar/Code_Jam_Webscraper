
#include <iostream>
using namespace std;

int get_number_of_intents(string &s, int k) {
	int n = 0;
	unsigned int i;

	for (i = 0; i < s.length() - k; i++) {
		if ('-' == s[i]) {
			for (int j = 0; j < k; j++)
				s[j+i] = s[j+i] == '-' ? '+' : '-';
			n++;
		}
	}

	//cout << "i final = " << i << endl;

	if ('-' == s[i]) {
		for (int j = 1; j < k; j++) if ('-' != s[j+i]) return -1;
		n++;
	} else {
		for (int j = 1; j < k; j++) if ('+' != s[j+i]) return -1;
	}

	return n;
}

int main() {

	unsigned int T, K;
	int n;
	std::string s;

	cin >> T;

	for (unsigned int i = 0; i < T; i++) {
		cin >> s;
		cin >> K;

		n = get_number_of_intents(s, K);

		if (-1 == n)
			cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << i + 1 << ": " << n << endl;
	}
}
