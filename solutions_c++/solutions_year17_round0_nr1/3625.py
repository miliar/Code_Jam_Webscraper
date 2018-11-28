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
#include <sstream>

using namespace std;


int flip (string cake, int k, int num_flips) {
	if (count(cake.begin(), cake.end(), '-') == 0) {
		return num_flips;
	}

	int first = cake.find('-');
	if ((first + k) > cake.length()) {
		return -1;
	}

	string new_cake = "";
	new_cake = cake.substr(0, first);
	string end_cake = cake.substr((first+k), string::npos);

	for (int i = 0; i < k; i++) {
		if (cake.substr((first+i), 1) == "+") {
			new_cake += "-";
		}
		else {
			new_cake += "+";
		}
	}

	new_cake += end_cake;

	return flip(new_cake, k, num_flips+1);

}


int solve(string cakes) {
	istringstream iss(cakes);

	string cake;
	int k;
	
	//cake contains the pancakes
	//k is the integer
	iss >> cake;
	iss >> k;

	int num_sad = count(cake.begin(), cake.end(), '-');

	if (num_sad == 0) {
		return 0;
	}
	if ((k % 2 == 0) && (num_sad % 2 == 1)) {
		return -1;
	}

	return flip(cake, k, 0);
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

			int res = solve(line);

			if (res == -1) {
				output << "Case #" + to_string(i) + ": " + "IMPOSSIBLE" << '\n';
			}
			else {
				output << "Case #" + to_string(i) + ": " + to_string(res) << '\n';
			}
		}

		myfile.close();
	}

	return 0;
}