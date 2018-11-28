#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

string tidy(string & temp) {
	for (size_t i = 0; i < temp.size() - 1; ++i) {
		if (temp[i] > temp[i + 1]) {
			for (size_t j = i + 1; j < temp.size(); j++) {
				temp[j] = '9';
			}
			bool is_finished = false;
			while (!is_finished) {
				while (temp[i] == '0')
				{
					temp[i] = '9';
					i--;
				}
				temp[i] = temp[i] - 1;
				if (i == 0) {
					break;
				}
				if (temp[i] >= temp[i - 1])
					is_finished = true;
				else {
					temp[i] = '9';
					i--;
				}					
			}	
			temp.erase(0, temp.find_first_not_of('0'));
			break;
		}
	}
	return temp;
}
void main() {
	int t;
	string temp;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> temp;
		cout << "Case #" << i << ": " << tidy(temp) << endl;
		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
}