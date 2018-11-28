// q2.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>
#include <cstdint>
#include <vector>
#include <fstream>
#include <algorithm>
#include <iomanip>

using namespace std;

string solve(size_t N, size_t R, size_t Y, size_t B) {

	string res = "";
	char c;
	if (R >= Y && R >= B) {
		c = 'R';
		R--;
	}
	else if (Y >= R && Y >= B) {
		c = 'Y';
		Y--;
	}
	else {
		c = 'B';
		B--;
	}
	res += c;

	for (size_t i = 0; i < N - 1; i++) {
		if (c == 'R') {
			if (Y == B && Y != 0) {
				if (res[0] == 'Y') {
					c = 'Y';
					Y--;
				}
				else {
					c = 'B';
					B--;
				}
			}
			else if (Y >= B && Y != 0) {
				c = 'Y';
				Y--;
			}
			else if (B >= Y && B != 0) {
				c = 'B';
				B--;
			}
			else {
				return "";
			}
		}

		else if (c == 'Y') {
			if (R == B && R != 0) {
				if (res[0] == 'R') {
					c = 'R';
					R--;
				}
				else {
					c = 'B';
					B--;
				}
			}
			else if (R >= B && R != 0) {
				c = 'R';
				R--;
			}
			else if (B >= R && B != 0) {
				c = 'B';
				B--;
			}
			else {
				return "";
			}
		}

		else if (c == 'B') {
			if (Y == R && Y != 0) {
				if (res[0] == 'Y') {
					c = 'Y';
					Y--;
				}
				else {
					c = 'R';
					R--;
				}
			}
			else if (R >= Y && R != 0) {
				c = 'R';
				R--;
			}
			else if (Y >= R && Y != 0) {
				c = 'Y';
				Y--;
			}
			else {
				return "";
			}
		}
		res += c;
	}

	if (res[N - 1] != res[0]) {
		return res;
	}
	else {
		return "";
	}
}

int main()
{
	ifstream inFile;
	inFile.open("..\\..\\B-small-attempt1.in");
	ofstream outFile;
	outFile.open("..\\..\\B-small-attempt1.out");

	size_t T;
	inFile >> T;
	for (size_t i = 0; i < T; i++) {
		size_t N;
		size_t R;
		size_t O;
		size_t Y;
		size_t G;
		size_t B;
		size_t V;
		inFile >> N;
		inFile >> R;
		inFile >> O;
		inFile >> Y;
		inFile >> G;
		inFile >> B;
		inFile >> V;

		string res = solve(N, R, Y, B);

		if (res != "") {
			outFile << "Case #" << (i + 1) << ": " << res << endl;
		}
		else {
			outFile << "Case #" << (i + 1) << ": IMPOSSIBLE" << endl;
		}
	}

	outFile.close();
	inFile.close();
	return 0;
}