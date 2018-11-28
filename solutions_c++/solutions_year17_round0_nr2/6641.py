#include <fstream>
#include <iostream>
#include <string>

using namespace std;

string numbers;

bool run() {
	for (int i = 0; i < numbers.length() - 1; i++) {
		if (numbers[i] > numbers[i + 1]) {
			numbers[i]--;
			i++;
			while (i < numbers.length()) {
				numbers[i] = '9';
				i++;
			}
			return true;
		}
	}
	return false;
}

void remove_leading_zeroes() {
	while (numbers[0] == '0')
		numbers.erase(0,1);
}

int main() {
	int T;
	ifstream in("B-large.in");
	ofstream out("output.txt");
	in >> T;
	bool changed;
	for (int t = 0; t < T; t++) {
		//read file
		cout << "===Starting " << t + 1 << "===" << endl;
		in >> numbers;
		cout << numbers << endl;
		//run
		do {
			changed = run();
			cout << numbers << endl;
		} while (changed);
		remove_leading_zeroes();
		//output
		out << "Case #" << t + 1 << ": " << numbers << endl;
	}
	in.close();
	out.close();
	return 0;
}