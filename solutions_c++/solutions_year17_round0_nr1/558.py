#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

using ll = long long int;
ifstream fin("1.in");
ofstream fout("1.out");

int main() {
	int T,k;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		string s;
		fin >> s >> k;
		int count = 0;
		for (int i = 0; i <= s.length() - k; i++) {
			if (s[i] == '-') {
				count++;
				for (int j = 0; j < k; j++) {
					if (s[i + j] == '+')
						s[i + j] = '-';
					else
						s[i + j] = '+';
				}
			}
		}

		bool impossible = false;
		for (int i = s.length() - k; i < s.length(); i++)
			if (s[i] == '-')
				impossible = true;

		if (!impossible)
			fout << "Case #" << t << ": " << count << endl;
		else
			fout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
	}
}
