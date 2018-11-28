#include <iostream>  
#include <string>
#include <fstream>


int solve(std::string l, int k) {
	int c = 0;
	int len = l.length();
	for (int i = 0; i <= len - k; ++i) {
		if (l[i] == '-') {
			for (int j = 0; j < k; ++j) {
				l[i + j] = l[i + j] == '-' ? '+' : '-';
			}
			c++;
		}
	}
	for (int i = len - k + 1; i < len && i >= 0; ++i) {
		if (l[i] == '-') return -1;
	}

	return c;
}

void main() {
	int t;
	std::ofstream out;
	std::ifstream in;
	in.open("A-large.in");
	out.open("out.txt");
	in >> t;
	for (int i = 0; i < t; ++i) {
		std::string l;
		int k;
		in >> l >> k;

		int x = solve(l, k);
		if (x == -1) { out << "Case #" << i+1 << ": " << "IMPOSSIBLE"  << std::endl; }
		else { out << "Case #" << i+1 << ": " << x << std::endl; }
	}
	out.close();
	in.close();
}
