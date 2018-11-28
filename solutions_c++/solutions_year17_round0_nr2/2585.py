#include <bits/stdc++.h>
using namespace std;

void modifyTidyNumber(string& s) {
	for (int i = 0; i < (int)s.size(); i++)
		s[i] = '9';
}

void removeLeadingZeros(string& s) {
	int i = 0;
	for (; i < (int)s.size(); i++)
		if (s[i] != '0')
			break;
	s = s.substr(i);
}

int main() {

	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);

	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) { //test cases
		string n;
		cin >> n;

		int len = (int)n.size();
		string tidy = "";
		tidy += n[len-1];

		for (int i = len - 2; i >= 0; i--) {
			if (tidy[0] < n[i]) {
				modifyTidyNumber(tidy);
				n[i] = n[i] - 1;
			}

			tidy = n[i] + tidy;
		}

		removeLeadingZeros(tidy);
		cout << "Case #" << t << ": " << tidy << '\n';
	}

	return 0;
}
