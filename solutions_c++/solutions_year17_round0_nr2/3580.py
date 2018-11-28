#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>
#include <cstddef>
#include <cstdint>
#include <cinttypes>
#include <cctype>
#include <vector>
#include <string>

using namespace std;

//Generate string of n 9s
string generate(int n) {
	string res = "";
	for (int i = 0; i < n; i++) {
		res += "9";
	}
	return res;
}

string find(string number) {

	bool found = false;
	string res = "";
	int len = number.length();
	if (len == 1) {
		return number;
	}

	for (int i = 0; i < len-1; i++) {
		int first = stoi(number.substr(i, 1));
		int second = stoi(number.substr(i+1, 1));

		if (first > second) {
			if (i == 0 && first == 1) {
				res = generate(len-1);
			}
			else {
				res += to_string(first-1);
				res += generate(len - i - 1);
			}
			found = true;
			break;
		}

		res += to_string(first);
		if (i == len-2) {
			res += to_string(second);
		}
	}

	if (found) {
		return find(res);
	}
	else {
		return res;
	}

}

int main() {

	int num;
	string line;
	ifstream myfile ("large.in");
	ofstream output ("output_large.txt");

	if (myfile.is_open()) {

		myfile >> num;
		getline(myfile, line);

		for (int i = 1; i <= num; i++) {
			getline(myfile, line);

			string res = find(line);
			output << "Case #" + to_string(i) + ": " + res << '\n';
		}

		myfile.close();
	}

	return 0;
}