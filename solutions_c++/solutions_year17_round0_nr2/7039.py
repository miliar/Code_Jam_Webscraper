#include <sstream>
#include <iostream>
#include <string>

using namespace std;

int solve(char s[], int casee) {
	int reset = -1; //Bepaal reset punt.
	int i = 0;

	while (s[i + 1] != 0 && reset == -1) {
		if (s[i] > s[i+1]) {
			//reset
			reset = i;
			while (reset != 0 && s[reset -1] == s[reset]) {
				reset--;
			}
		} else {
			i++;
		}
	}

	cout << "Case #" << casee << ": ";

	if (s[1] == 0) {
		char x = s[0];
		cout << x;
	}
	else if (reset == -1) {
		cout << s;
	}
	else {
		i = 0;

		while (s[i] != 0) {
			if (i < reset) {
				cout << s[i];
			}
			else if (reset == i) {
				if (reset != 0 || s[0] != '1') {
					char x = s[reset];
					x--;
					cout << x;
				}
			}
			else {
				cout << '9';
			}

			i++;
		}
	}

	cout << endl;
};

int main() {
	int casee;
	int cases;

	cin>>cases;
	char s[3100];

	//cout << "Number of cases: " << cases << endl;
	
	for (casee = 1; casee <= cases; casee++ ) {
		for (int i = 0; i < 3100; i++)
			s[i] = 0;
		cin >> s;
		solve(s, casee);
	}
};