#include <iostream> 
#include <string>
#include <fstream>

using namespace std;

void main() {
	ifstream fin("in.txt");
	ofstream fout("out.txt");

	int T;
	fin >> T;
	for (int caseNo = 1; caseNo <= T; caseNo++) {
		string s;
		int k;
		fin >> s >> k; 

		int i;
		int flips = 0;
		for (i = 0; i < s.length()-(k-1); i++) {
			if (s[i] == '-') {
				//flip k
				flips++;
				for (int j = 0; j < k; j++)
					s[i + j] = (s[i + j] == '-' ? '+' : '-');
			}
		}
		for (; i < s.length(); i++) {
			if (s[i] == '-') {
				flips = -1;
				break;
			}
		}
		string t = flips == -1 ? "IMPOSSIBLE" : to_string(flips);
		fout << "Case #" << caseNo << ": " << t << endl;
		cout << "Case #" << caseNo << ": " << t << endl;
	}
}