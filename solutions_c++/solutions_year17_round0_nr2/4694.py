#include <iostream>  
#include <string>
#include <fstream>


char basic_pred(char c) {
	switch (c) {
	case '1': return '0';
	case '2': return '1';
	case '3': return '2';
	case '4': return '3';
	case '5': return '4';
	case '6': return '5';
	case '7': return '6';
	case '8': return '7';
	case '9': return '8';
	case '0': return '9';
	default: break;
	}
}

void solve(std::string &l) {
	for (int i = l.length() -1; i > 0 ; --i) {
		if (l[i - 1] > l[i]) {
			for (int j = i; j < l.length(); ++j) {
				l[j] = '9';
			}
			l[i - 1] = basic_pred(l[i - 1]);
		}
	}
	if (l.length() > 1 && l[0] == '0') {
		l = l.substr(1, l.length() - 1);
	}
}

void main() {
	int t;
	std::ofstream out;
	std::ifstream in;
	in.open("B-large.in");
	out.open("out.txt");
	in >> t;
	for (int i = 0; i < t; ++i) {
		std::string l;
		in >> l;
		solve(l);
		out << "Case #" << i + 1 << ": " << l << std::endl;
	}
	out.close();
	in.close();
}
