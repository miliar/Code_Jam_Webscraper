#include<iostream>
#include<algorithm>
#include<math.h>
#include<string>
#include<string.h>
#include<cstdio>
using namespace std;
int stringtoint(const char ca[]) {
	int num = 0;
	int stlen = strlen(ca);
	for (int i = 0; i < stlen; i++) {
		num *= 10;
		num += ca[i] - '0';
	}
	return num;
}
bool violatesplus(char input[][101], int N, int ri, int ci) {
	int count = 0;
	for (int i = 1; i <= N; i++) {
		if (input[ri][i] == 'o' || input[ri][i] == 'x') count += 1;
		if (input[i][ci] == 'o' || input[i][ci] == 'x') count += 1;
	}
	if (input[ri][ci] == 'o' || input[ri][ci] == 'x') count -= 1;
	if (count > 1) return true;
	return false;
}
bool violatesstar(char input[][101], int N, int ri, int ci) {
	int count = 0;
	for (int i = 1; i <= N; i++)
		if (ri + i <= N && ci + i <= N)
			if (input[ri+i][ci+i] == 'o' || input[ri + i][ci + i] == '+') count += 1;
	for (int i = 1; i <= N; i++)
		if (ri - i > 0 && ci - i > 0)
			if (input[ri - i][ci - i] == 'o' || input[ri - i][ci - i] == '+') count += 1;
	for (int i = 1; i <= N; i++)
		if (ri + i <= N && ci - i > 0)
			if (input[ri + i][ci - i] == 'o' || input[ri + i][ci - i] == '+') count += 1;
	for (int i = 1; i <= N; i++)
		if (ri - i > 0 && ci + i <= N)
			if (input[ri - i][ci + i] == 'o' || input[ri - i][ci + i] == '+') count += 1;
//	if (input[ri][ci] == 'o' || input[ri][ci] == 'x') count -= 3;
	if (count >= 1) return true;
	return false;
}

int main() {
	int NoOfTestCases;
	//cin.clear();
//	cin.ignore();
	string st;
	getline(std::cin, st);
	NoOfTestCases = stringtoint(st.c_str());
	for (int j = 0; j < NoOfTestCases; j++) {
		getline(std::cin, st);
		int delim = st.find(' ');
		int N = stringtoint(st.substr(0, delim).c_str());
		int M = stringtoint(st.substr(delim + 1, strlen(st.c_str())).c_str());
		char input[101][101];
		int inputno[101][101], models = 0;
		for (int i = 0; i < N + 1; i++) {
			for (int k = 0; k < N + 1; k++) { input[i][k] = '.'; inputno[i][k] = 0;
			}
		}
		// Read the input
		for (int i = 0; i < M; i++) {
			getline(std::cin, st);
			int delim = st.find(' ');
			char charact = st[0];
			st = st.substr(delim + 1, strlen(st.c_str()));
			delim = st.find(' ');
			int ri = stringtoint(st.substr(0, delim).c_str());
			int ci = stringtoint(st.substr(delim + 1, strlen(st.c_str())).c_str());
			input[ri][ci] = charact;
		}

		// Start processing the algorithm
		// Fill the boundaries only
		for (int i = 1; i <= N; i++) {
			if (input[i][1] == '.') {
				bool flag = true;
				if (flag) {
					input[i][1] = '+';
					if (!violatesstar(input, N, i, 1)) flag = false;
				}
				if (flag) {
					input[i][1] = '.';
				}
				else {
					inputno[i][1] = 1;
				}
			}
		}

		for (int i = 1; i <= N; i++) {
			if (input[N][i] == '.') {
				bool flag = true;
				if (flag) {
					input[N][i] = '+';
					if (!violatesstar(input, N, N, i)) flag = false;
				}
				if (flag) {
					input[N][i] = '.';
				}
				else
				{
					inputno[N][i] = 1;
				}
			}
		}

		for (int i = 1; i <= N; i++) {
			if (input[i][N] == '.') {
				bool flag = true;
				if (flag) {
					input[i][N] = '+';
					if (!violatesstar(input, N, i, N)) flag = false;
				}
				if (flag) {
					input[i][N] = '.';
				}
				else {
					inputno[i][N] = 1;
				}
			}
		}

		for (int i = 1; i <= N; i++) {
			if (input[1][i] == '.') {
				bool flag = true;
				if (flag) {
					input[1][i] = '+';
					if (!violatesstar(input, N, 1, i)) flag = false;
				}
				if (flag) {
					input[1][i] = '.';
				}
				else {
					inputno[1][i] = 1;
				}
			}
		}
		// Fill the stars
		for (int i = 1; i <= N; i++) {
			for (int k = 1; k <= N; k++) {
				if (input[i][k] == '.') {
					bool flag = true;
					if (flag) {
						input[i][k] = 'x';
						if (!violatesplus(input, N, i, k)) flag = false;
					}
					if (flag) {
						input[i][k] = '.'; continue;
					}
					inputno[i][k] = 1;
					models += 1;
				}
			}
		}
		// Fill the stars
		// Improvise
		for (int i = 1; i <= N; i++) {
			for (int k = 1; k <= N; k++) {
				if (input[i][k] == '+' || input[i][k] == 'x') {
					// Try Upgrading
					char temp = input[i][k];
					input[i][k] = 'o';
					if (violatesplus(input, N, i, k)) {
						input[i][k] = temp; continue;
					}
					if (violatesstar(input, N, i, k)) {
						input[i][k] = temp; continue;
					}
					inputno[i][k] = 1;
					models += 1;
				}
			}
		}
		// Fill the stars
		int stylepoints = 0, inserts = 0;
		for (int i = 1; i < N + 1; i++) {
			for (int k = 1; k < N + 1; k++) {
				if (input[i][k] == 'x' || input[i][k] == '+') stylepoints += 1;
				if (input[i][k] == 'o') stylepoints += 2;
				if (inputno[i][k] == 1) inserts += 1;
			}
		}
		cout << "Case #" << j + 1 << ": " << stylepoints << " " << inserts<< endl;
		for (int i = 1; i < N + 1; i++) {
			for (int k = 1; k < N + 1; k++) {
				if (inputno[i][k] == 1)
					cout << input[i][k] << " " << i << " " << k<<endl;
			}
		}
	}
	return 0;
}