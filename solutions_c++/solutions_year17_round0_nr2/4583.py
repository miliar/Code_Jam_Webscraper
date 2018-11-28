#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	ifstream fin("B-large.in");
	ofstream fout("output.txt");

	int T;
	fin >> T;

	for (int t = 1; t <= T; t++) {
		string number;
		fin >> number;

		int last = 0;
		int lasti = -1;
		for (int i = 0; i < number.length(); i++) {
			int v = number[i] - '0';
			if (v < last) {
				if (number[lasti] == '1') {
					number = string(number.length() - 1, '9');
					break;
				}
				else {
					number[lasti] = last - 1 + '0';
					for (int j = lasti + 1; j < number.length(); j++){
						number[j] = '9';
					}
					break;
				}
			}
			if (v != last) {
				last = v;
				lasti = i;
			}
		}
	
		fout << "Case #" << to_string(t) << ": " << number << endl;
	}
}