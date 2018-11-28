#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
typedef struct input {
	string in;
	int len;
	string space;
}Input;
vector<Input> read_file() {
	vector <Input> input(1);
	ifstream myfile;
	myfile.open("A-large.in");
	if (myfile.is_open()) {
		for (int i = 0;; i++) {
			if (myfile.eof()) { break; }
			input.resize(i + 1);
			myfile >> input[i].in >> input[i].len;
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
vector<char> reverse(vector<char>input_for_rev, int start,int len) {
	for (int i = start; i<start+len; i++) {
		if (input_for_rev[i] == '-') { input_for_rev[i] = '+'; }
		else if (input_for_rev[i] == '+') { input_for_rev[i] = '-'; }
	}
	return input_for_rev;
}
vector<char> fill(int size) {
	vector<char> ret(size);
	for (int i = 0; i < size; i++) {
		ret[i] = '+';
	}
	return ret;
}
int check2(vector<char> in1, vector<char> in2) {
	int counter = 0;
	for (int i = 0; i < in1.size(); i++) {
		if (in1[i] == in2[i]) { counter++; }
	}
	if (counter == in2.size()) { return 1; }
	else { return -2; }
}
int execute(string proc,int len) {
	int counter = 0;
	vector<char>examination = takeapart(proc);
	vector<char> check = fill(examination.size());
	int s;
	for (int i = 0; i <examination.size(); i++) {
		if (examination[i] == '+') { continue; }
		else if (examination[i] == '-') {
			s = i;
			if (s + len <= examination.size()) { examination = reverse(examination, s, len); counter++; }
			else { s = 0; examination = reverse(examination, s, len); counter++;
			}
		}
	}
	int d = check2(examination, check);
	if (d == 1) {
		return counter;
	}
	else if (d == -2) {
		return d;
	}
}
int main() {
	ofstream output;
	vector<Input> input = read_file();
	output.open("output.out");
	for (int i = 0; i <input.size(); i++) {
		int d = execute(input[i].in, input[i].len);
		if (d != -2) {
			output << "Case #" << i + 1 << ": " << d << endl;
		}
		else {
			output << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
		}
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