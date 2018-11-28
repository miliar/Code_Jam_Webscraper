#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

vector<string> read_file() {
	vector <string> input(1);
	ifstream myfile;
	myfile.open("B-small-attempt0.in");
	if (myfile.is_open()) {
		for (int i = 0;; i++) {
			if (myfile.eof()) { break; }
			input.resize(i + 1);
			myfile >> input[i];
		}
		myfile.close();
		input.resize(input.size() - 1);
		return input;
	}
	else { exit; }
}
vector<char> takeapart(string input) {
	std::vector<char> writable(input.begin(), input.end());
	writable.push_back('\0');
	writable.resize(writable.size() - 1);
	return writable;
}


int test(string proc) {
	int counter = 0;
	vector<char>examination = takeapart(proc);

	char s;
	for (int i = 0; i <examination.size(); i++) {
		s = examination[i];
		for (int j = i; j < examination.size(); j++) {
			if (examination[j] - '0' < s - '0') { return 0; }
		}
	}
	return 1;
}

int execute(string input) {
	int ret = 0;
	for (int i = atoi(input.c_str()); i > 0; i--) {
		{
			
			ret=test( to_string(i));
			
			if (ret == 1) { return i; }
			else { continue; }
		}

	}
}
int main() {
	ofstream output;
	vector<string> input = read_file();
	output.open("output.out");
	for (int i = 0; i < input.size(); i++) {
		int d = execute(input[i]);
			output << "Case #" << i + 1 << ": " << d << endl;
	}
/*	int d = execute("+---+++---", 6);
	if (d != -2) {
		cout << "Case #" << 1 << ": " << d << endl;
	}
	else {
		cout << "Case #" << 1 << ": " << "IMPOSSIBLE" << endl;
	}*/
	output.close(); cout << "process is completed...\n";
}