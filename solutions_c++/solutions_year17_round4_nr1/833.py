// q1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>
#include <cstdint>
#include <vector>
#include <fstream>
#include <algorithm>
#include <iomanip>

using namespace std;

size_t solve(size_t N, size_t P, vector<size_t>& groups) {
	size_t res = groups[0];

	if (P == 2) {
		res += groups[1] / 2;
		groups[1] -= 2 * (groups[1] / 2);
	}
	else if (P == 3) {
		// 1+2
		size_t m = min(groups[1], groups[2]);
		res += m;
		groups[1] -= m;
		groups[2] -= m;

		// 3*1 or 3*2
		res += groups[1] / 3;
		res += groups[2] / 3;
		groups[1] -= 3 * (groups[1] / 3);
		groups[2] -= 3 * (groups[2] / 3);
	}
	else if (P == 4) {
		// 1+3
		size_t m = min(groups[1], groups[3]);
		res += m;
		groups[1] -= m;
		groups[3] -= m;

		// 2+2
		res += groups[2] / 2;
		groups[2] -= 2 * (groups[2] / 2);

		// 1+1+2 or 2+3+3
		if (groups[2] != 0) {
			if (groups[1] >= 2) {
				res += 1;
				groups[2]--;
				groups[1] -= 2;
			}
			else if (groups[3] >= 2) {
				res += 1;
				groups[2]--;
				groups[3] -= 2;
			}
		}

		// 4*1 or 4*3
		res += groups[1] / 4;
		res += groups[3] / 4;
		groups[1] -= 4 * (groups[1] / 4);
		groups[3] -= 4 * (groups[3] / 4);
	}

	for (size_t i = 1; i < P; i++) {
		if (groups[i] != 0) {
			res++;
			break;
		}
	}

	return res;
}

int main()
{
	ifstream inFile;
	inFile.open("..\\..\\A-large.in");
	//inFile.open("..\\..\\A-large.in");
	ofstream outFile;
	outFile.open("..\\..\\A-large.out");
	//outFile.open("..\\..\\A-large.out");

	size_t T;
	inFile >> T;
	for (size_t i = 0; i < T; i++) {
		size_t N;
		size_t P;
		inFile >> N;
		inFile >> P;

		vector<size_t> groups(P, 0);
		size_t g;
		for (size_t j = 0; j < N; j++) {
			inFile >> g;
			groups[g % P]++;
		}

		size_t res = solve(N, P, groups);

		outFile << "Case #" << (i + 1) << ": " << res << endl;
	}

	outFile.close();
	inFile.close();
	return 0;
}