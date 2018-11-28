#include <iostream>
#include <tuple>
#include <sstream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>

using namespace std;

int main() {
	ifstream fin("A-large.in");
	ofstream fout("Results.txt");

	if (!fin) {
		cout << "Error reading input file." << endl;
		return -1;
	}
	else if (!fout) {
		cout << "Error reading output file." << endl;
		return -1;
	}
	else {
		char line[1001];
		char states[1001];
		fin.getline(line, (int)101);
		int t = stoi(line);
		for (int i = 0; i < t; i++) {
			fin.getline(states, (int)1001, ' ');
			fin.getline(line, (int)10);
			int k = stoi(line);
			int count = 0;
			for (int j = 0; j < strlen(states) - k+1; j++) {
				if (states[j] == '-') {
					count++;
					states[j] = '+';
					for (int m = j+1; m < j + k; m++) {
						if (states[m] == '-') {
							states[m] = '+';
						}
						else
						{
							states[m] = '-';
						}
					}
				}
			}
			bool success = true;
			for (int j = strlen(states) - k; j < strlen(states) + 1; j++) {
				if (states[j] == '-') {
					success = false;
				}
			}
			if (success) {
				fout << "Case #" << i + 1 << ": " << count << endl;
			}
			else {
				fout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
			}
			
		}

		cout << endl;
	}

	fin.close();
	fout.close();

	return 0;
}