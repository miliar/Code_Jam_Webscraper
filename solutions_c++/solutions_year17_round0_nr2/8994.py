#include <iostream>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

string tidyNumbers(string s) {

	for(int i = s.size() - 1; i > 0; i--) {
		if(!(s[i] >= s[i-1])) {
			int b = (int)s[i-1];
			b--;
			s[i-1] = b;
			
			for(int j = i; j < s.size(); j++)
				s[j] = '9';
		}
	}

	int newBeg;

	for(int i = 0; i < s.size(); i++) {
		if(s[i] != '0') {
			newBeg = i;
			break;
		}
	}

	s = s.substr(newBeg);

	return s;
}

int main() {
	int t; 
	string n; 
	string tidy;


	cin >> t;

	for(int i = 0; i < t; i++) {
		cin >> n;
		tidy = tidyNumbers(n);

		cout << "Case #" << (i+1) << ": " << tidy << endl;
	}

}