#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main() {
	int t = 0;
	bool arr[1010] = { false };
	ifstream fin;
	fin.open("A-large.in", ios::in);
	ofstream fout;
	fout.open("output.out", ios::out);

	fin >> t;

	for (int i = 0; i < t; i++) {
		int k = 0;
		string str;
		fin >> str >> k;
		int len = str.length();
		for (int j = 0; j < len; j++) {
			if (str[j] == '-') {
				arr[j] = false;
			}
			else arr[j] = true;
		}
		int cnt = 0;
		for (int j = 0; j <= len-k; j++) {
			if (!arr[j]) {
				cnt++;
				for (int z = 0; z < k; z++) {
					arr[j + z] = !arr[j + z];
				}
			}
		}

		fout << "Case #" << i + 1 << ": ";
		bool valid = true;
		for (int j = len - k; j < len; j++) {
			if (!arr[j]) {
				valid = false;
				break;
			}
		}
		
		if (valid) {
			fout << cnt << endl;
		}
		else{
			fout << "IMPOSSIBLE" << endl;
		}
	}

	return 0;
}