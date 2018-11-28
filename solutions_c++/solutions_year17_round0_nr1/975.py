#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main () {
	ifstream fin ("A-large.in");
	ofstream fout ("A-sol.txt");
	if (fin.is_open()) {
		string pattern;
		int k;
		int numCases;
		fin >> numCases;
		for (int cases = 1; cases <= numCases; cases++) {
			fin >> pattern >> k;
			int length = pattern.size();
			int sol[length] = {0};
			int ans = 0;
			for (int i = 0; i < length; i++) {
				if (pattern[i] == '-') {
					sol[i]++;
				}
			}
			for (int i = 0; i < length-k+1; i++) {
				if (sol[i] % 2 == 1) {
					ans++;
					for (int j = 0; j < k; j++) {
						sol[i+j]++;
					}
				}
			}
			bool noSol = false;
			for (int i = 0; i < length; i++) {
				if (sol[i] % 2 == 1) {
					noSol = true;
					break;
				}
			}
			if (noSol) {
				fout << "Case #" << cases << ": IMPOSSIBLE\n";
				cout << "Case #" << cases << ": IMPOSSIBLE\n";
			} else {
				fout << "Case #" << cases << ": " << ans << '\n';
				cout << "Case #" << cases << ": " << ans << '\n';
			}
		}
	}
	fin.close();
	fout.close();
	return 0;
}
