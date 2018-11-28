#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;
int t, nsize, nn[20];
char n[20];
int main() {
	ifstream fin;
	ofstream fout;
	fin.open("B-small-attempt3.in");
	fout.open("out.in");
	fin >> t;
	fin.getline(n, 20);
	for (int j = 1; j <= t; j++) {
		fin.getline(n, 20);
		nsize = strlen(n);
		int flag = 0;
		for (int i = nsize - 1; i >= 0; i--) {
			int curr = n[i] - '0';
			if (flag == 1) {
				curr--;
				for (int j = i + 1; j < nsize; j++) nn[j] = 9;
				flag = 0;
			}
			if (i != 0 && (curr <= 0 || (n[i - 1] - '0' > curr))) {
				flag = 1;
				if (i == nsize - 1) nn[i] = 9;
				else nn[i] = nn[i + 1];
			}
			else nn[i] = curr;
		}
		fout << "Case #" << j << ": ";
		for (int i = 0; i < nsize; i++) {
			if (i == 0 && nn[i] == 0) continue;
			fout << nn[i];
		}
		fout << endl;
	}
	fin.close();
	fout.close();
	return 0;
}