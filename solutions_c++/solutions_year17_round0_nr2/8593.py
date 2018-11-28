#include <fstream>
#include <iostream>
#include <unordered_set>
#include <queue>
#include <string>

using namespace std;

string tidy(string n);

int main() {
	ifstream in("B-large.in");
	ofstream out("out.txt");
	int T;
	in >> T;
	for (int i = 1; i <= T; ++i) {
		string n;
		in >> n;
		out << "Case #" << i << ": ";
		string r = tidy(n);
		string s = tidy(r);
		while (r != s) {
			r = tidy(s);
			s = tidy(r);
		}
		out <<  r << endl;
		out.flush();
	}

	return 0;
}

string tidy(string n) {
	int i = 1;
	for (; i < n.length(); ++i) {
		if (n[i] < n[i - 1])break;
	}
	if (i == n.length()) return n;
	while (i > 0 && n[i - 1] == '0') --i;
	n[i - 1]--;
	for (; i < n.length(); ++i) {
		n[i] = '9';
	}
	if (n[0] == '0') return n.substr(1);
	return n;
}