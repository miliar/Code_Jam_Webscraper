#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	ifstream in;
	ofstream out;

	in.open("C:\\works\\in.txt");
	out.open("C:\\works\\out.txt");

	int n;

	in >> n;

	for (int i = 0; i < n; i++) {
		int num;
		string s;
		in >> s;
		if (s.size() > 1) {
			char prev = s[s.size() - 1];
			for (int j = s.size() - 2; j >= 0; j--) {
				if (prev < s[j]) {
					s[j + 1] = '9';
					s[j] = s[j] - 1;
					for (int k = j + 1; k < s.size(); k++) {
						s[k] = '9';
					}
				}
				prev = s[j];
			}
		}
		out << "Case #" << i + 1 << ": ";
		for (int j = 0; j < s.size(); j++) {
			if (s[j] != '0') out << s[j];
		}
		out << endl;
	}
}