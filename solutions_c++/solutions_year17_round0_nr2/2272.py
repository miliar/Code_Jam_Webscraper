#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <cmath>

using namespace std;

int toint(char a) {
	return a - '0';
}

string solve(string s){
	for(int i = 0; i < s.size() - 1; i++) {
		if(toint(s[i]) > toint(s[i + 1])) {

			for(int j = i + 1; j < s.size(); j++) {
				s[j] = '9';
			}


			s[i] -= 1;
			return solve(s);
		}
	}

	if(s[0] == '0')
		s.erase(0, 1);

	return s;
}

int main() {
	int t;
	string s;

	cin >> t;

	for(int i = 0; i < t; i++){
		cin >> s;

		cout << "Case #" << (i + 1) << ": " << solve(s) << endl;

	}

	return EXIT_SUCCESS;
}
