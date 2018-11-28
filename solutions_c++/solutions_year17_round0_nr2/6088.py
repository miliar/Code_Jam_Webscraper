/// B_Tidy_Numbers

#include <cstdio>
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
	int t;	cin >> t;

	ofstream fout;
	fout.open("output.txt");

	for (int testCase = 1; testCase <= t; testCase++) {
		int k = 0;
		string line;
		cin >> line;
		for (int i = 0; i < line.length() - 1; i++) {
			if (line[i] > line[i + 1]) {
				line[i]--;
				for (int j = i + 1; j < line.length(); j++)
					line[j] = '9';
				i = -1;
			}
		}

		for (int i = 0; i < line.length(); i++) {
			if (line[i] != '0') {
				k = i;
				break;
			}
		}
		line = line.substr(k, line.length() - k);
		
		cout << "Case #" << testCase << ": " << line << endl;
		fout << "Case #" << testCase << ": " << line << endl;
	}
	fout.close();
}