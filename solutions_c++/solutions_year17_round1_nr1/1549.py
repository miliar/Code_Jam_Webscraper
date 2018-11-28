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

typedef pair<int, int> pii;
typedef long long i64;
typedef unsigned long long ui64;
typedef vector<i64> vi64;
typedef pair<i64, i64> pi64;
typedef vector<int> vi;
typedef vector<char> vc;
typedef vector<vc> vvc;
typedef vector<pii> vpi;
typedef vector<pi64> vpi64;
typedef vector<vi> vvi;
typedef vector<vi64> vvi64;
typedef double ld;

int main() {
	//ifstream fin("File.txt");
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
		char line[101];
		fin.getline(line, (int)101);
		int t = stoi(line);
		for (int T = 0; T < t; T++) {
			fin.getline(line, (int)101,' ');
			int R = stoi(line);
			vc Row;
			Row.assign(R, '?');
			fin.getline(line, (int)101);
			int C = stoi(line);
			vvc Col;
			Col.assign(C, Row);
			for (int i = 0; i < R; i++) {
				fin.getline(line, (int)101);
				for (int j = 0; j < C; j++) {
					if (line[j] != '?') {
						Col[j][i] = line[j];
					}
				}
			}
				for (int i = 0; i < R; i++) {
					for (int j = 0; j < C; j++) {
						if (Col[j][i] != '?') {
							for (int k = j+1; k < C; k++) {
								if (Col[k][i] == '?') {
									Col[k][i] = Col[j][i];
								}
								else {
									break;
								}
							}
							for (int k = j-1; k > -1; k--) {
								if (Col[k][i] == '?') {
									Col[k][i] = Col[j][i];
								}
								else {
									break;
								}
							}
						}
					}
				}
				for (int i = 0; i < R; i++) {
					for (int j = 0; j < C; j++) {
						if (Col[j][i] != '?') {
							for (int k = i+1; k < R; k++) {
								if (Col[j][k] == '?') {
									Col[j][k] = Col[j][i];
								}
								else {
									break;
								}
							}
							for (int k = i-1; k > -1; k--) {
								if (Col[j][k] == '?') {
									Col[j][k] = Col[j][i];
								}
								else {
									break;
								}
							}
						}
					}
				}

			fout << "Case #" << T+1 << ":" << endl;
			for (int i = 0; i < R; i++) {
				for (int j = 0; j < C; j++) {
					fout << Col[j][i];
				}
				fout << endl;
			}
		}
	}

	fin.close();
	fout.close();

	return 0;
}