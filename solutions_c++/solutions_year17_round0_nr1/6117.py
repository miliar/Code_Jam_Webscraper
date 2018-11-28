#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int flip(string &temp, int & k) {
	int num = 0;
	for (int i = 0; i <= temp.size() - k; i++) {
		if (temp[i] == '-') {
			num++;
			for (int j = i; j < i + k; j++) {
				if (temp[j] == '+')
					temp[j] = '-';
				else
					temp[j] = '+';
			}
		}
	}
	for (int i = temp.size() - k + 1; i < temp.size(); ++i) {
		if (temp[i] == '-')
			return -1;
	}
	return num;
}
void main() {
	int t, k;
	string temp;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> temp >> k;
		int n = flip(temp, k);
		if((n== -1))
			cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << i << ": " << n << endl;
		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
}