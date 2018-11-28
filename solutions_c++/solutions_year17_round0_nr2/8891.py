#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;
string tidy = "";
bool tide(string);
int main() {
	int T = 0;
	string N = "";
	ifstream in("B-large.in");
	ofstream out("B-Large_out.txt");
	in >> T;
	for (int z = 0; z < T; z++) {
		in >> N;
		tide(N);
		if (tidy.at(0) == '0') {
			tidy = tidy.substr(1, tidy.length() - 1);
		}
		out << "Case #" << z + 1 << ": " << tidy << "\n";
		tidy = "";
	}
	return 0;
}
bool tide(string N) {
	tidy = "";
	char x = N.at(0), y = 0;
	bool isTidy = true;
	int len = N.length();
	for (int i = 0; i < len - 1; i++) {
		x = N.at(i);
		y = N.at(i + 1);
		if (y < x) {
			isTidy = false;
			x -= 1;
			y = '9';
			tidy += x;
			for (int j = i; j < len - 1; j++) {
				tidy += y;
			}
			break;
		}
		tidy += x;
	}
	if (len == 1) {
		tidy = x;
		return true;
	}
	if (isTidy) {
		tidy += y;
		return true;
	} else {
		return tide(tidy);
	}
}
