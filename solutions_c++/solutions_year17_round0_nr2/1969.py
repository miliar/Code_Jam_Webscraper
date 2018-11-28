#include<iostream>
#include<fstream>

using namespace std;

int main() {
	ofstream fout("tidy.out");
	ifstream fin("tidy.in");
	int T;
	fin >> T;
	for (int t = 0; t < T; t++) {
		char number[20];
		for (int i = 0; i < 20; i++) {
			number[i] = 0;
		}
		fin >> number;
		int i = 19;
		int end=i;
		while (!(number[i] > 47 && number[i] < 58)) {
			end = i;
			i--;
		}
		for (int i = 0; i < end-1; i++) {
			if (number[i+1] < number[i]) {
				number[i]--;
				for (int j = i + 1; j < end; j++) {
					if (number[j] > 47 && number[j] < 58) {
						number[j] = '9';
					}
				}
				i = -1;
			}
		}
		fout << "Case #" << t + 1 << ": ";
		bool leading = false;
		for (int i = 0; i < 20; i++) {
			if (number[i] > 48 && number[i] < 58) {
				leading = true;
				fout << number[i];
			}
			else if (leading&&number[i]==48) {
				fout << number[i];
			}
		}
		fout << endl;
	}
	system("pause");
}