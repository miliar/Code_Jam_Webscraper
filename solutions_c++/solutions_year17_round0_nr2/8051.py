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
	ifstream fin("B-small-attempt1.in");
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
		char line[101];
		fin.getline(line, (int)101);
		int t = stoi(line);
		for (int T = 0; T < t; T++) {

			fin.getline(line, (int)101);
			long long N = stoll(line);
			int count = 0;
			long long solution;
			for (long long i = N; i > 0; i--) {

				int p = i % 10;
				int c = 0;
				long long copy = i;
				long long power = 1;
				bool tidy = true;
				int cycles = 1;
				while (copy) {

					copy /= 10;
					if (!copy) {
						break;
					}
					c = copy % 10;
					if (c > p) {

						tidy = false;
						break;
					}

					else if (c == p){
						cycles++;
					}
					else {
						for (int s = 1; s < (cycles + 1); s++) {
							power *= 10;
						}
						p = c;
					}

				}

				if (tidy) {
					solution = i;
					break;

				}
				else {
					i -= i % power;
				}

			}

			fout << "Case #" << T+1 << ": " << solution << endl;

		}

	}

	fin.close();
	fout.close();

	return 0;
}