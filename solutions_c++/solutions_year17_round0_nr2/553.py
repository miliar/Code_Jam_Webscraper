#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

using ll = long long int;
ifstream fin("2.in");
ofstream fout("2.out");

int main() {
	int T,k;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		string s;
		fin >> s;
		bool found = true;

		while (found) {
			found = false;
			for (int i = 0; i < s.length() - 1; i++) {
				if (s[i] > s[i + 1]) {
					s[i]--;
					for (int j = i + 1; j < s.length(); j++)
						s[j] = '9';
					found = true;
					break;
				}
			}
		}

		fout << "Case #" << t << ": ";
		int ind = 0;
		while (s[ind] == '0')
			ind++;
		for (; ind < s.length(); ind++)
			fout << s[ind];
		fout << endl;
	}
}
