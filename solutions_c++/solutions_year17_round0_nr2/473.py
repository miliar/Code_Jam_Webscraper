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
		string N;
		fin >> N;

		while (true) {
			int i = 0;
			while (i + 1 < N.length() && N[i] <= N[i + 1])
				i++;
			if (i + 1 == N.length()) {
				break;
			}
			N[i]--;
			while (++i < N.length())
				N[i] = '9';
		}		
		int j = 0;
		while (N[j] == '0')
			j++;
		N = N.substr(j);

		fout << "Case #" << caseNo << ": " << N << endl;
		cout << "Case #" << caseNo << ": " << N << endl;
	}
}