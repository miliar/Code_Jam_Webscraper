#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool isTidy(string s) {
	for (int i = 1; i < s.size(); ++i) {
		if (s[i - 1] > s[i]) {
			return false;
		}
	}
	return true;
}

string minus_one(string s) {
	int l = s.size();
	if (s[l - 1] == '0') {
		return minus_one(s.substr(0, l - 1)) + "9";
	}
	s[l - 1] = s[l - 1] - 1;
	if (s[0] == '0') {
		s = s.substr(1);
	}
	return s;
}

string search(string s) {
	if (isTidy(s)) {
		return s;
	}
	string sub_s = minus_one(s.substr(0, s.size() - 1));
	return search(sub_s) + "9";
}

void run(istream &in, ostream &out) {
	int T;
	in >> T;
	for (int i = 0; i < T; ++i) {
		string s;
		in >> s;
		string result = search(s);
		out << "Case #" << (i + 1) << ": " << result << endl;
		// out << result << endl;
	}
}

int main() {
	// ifstream fin("B-large.in");
	// ofstream fout("B-large.out");
	// run(fin, fout);
	run(cin, cout);
	return 0;
}