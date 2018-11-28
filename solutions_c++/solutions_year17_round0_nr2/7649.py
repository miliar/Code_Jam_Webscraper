#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main() {
	int t = 0;
	int arr[20] = { 0 };
	int res[20] = { 0 };

	ifstream fin;
	fin.open("B-large.in", ios::in);
	ofstream fout;
	fout.open("output.out", ios::out);

	fin >> t;

	for (int i = 0; i < t; i++) {
		string str;
		fin >> str;
		int len = str.length();
		for (int j = 0; j < len; j++) {
			arr[j] = str[j] - '0';
			res[j] = str[j] - '0';
		}
		int index = 0;
		bool invalid = false;
		for (int j = len-1; j > 0; j--) {
			if (res[j] < res[j - 1]) {
				int temp = res[j];
				res[j] = 9;
				res[j - 1]--;
				index = j - 1;
				invalid = true;
			}
		}

		if (invalid) {
			
			for (int j = index + 1; j < len; j++) {
				res[j] = 9;
			}
		}
		fout << "Case #" << i + 1 << ": ";
		int start = 0;
		if (!res[0])
			start = 1;
		for (int j = start; j < len;j++) {
			char c = res[j] + '0';
			fout << c;
		}
		fout << endl;
	}

	return 0;
}