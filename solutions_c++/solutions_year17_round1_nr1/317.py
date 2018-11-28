#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <assert.h>
#include <unordered_map>
#include <limits.h>
#include <assert.h>
#include <string.h>
#include <Util.h>

using namespace std;

bool debug = false;

enum { MAX = 100 };

char matrix[MAX][MAX];

int R, C;

bool emptyRow(int r) {
	for (int c = 0; c < C; c++)
		if (matrix[r][c] != '?') return false;
	return true;
}

void solve(int CASE) {
	for (int r = 0; r < R; r++) {
		if (debug) cout << "row: ";
		for (int c = 0; c < C; c++) {
			if (debug) cout << matrix[r][c];
		}
		if (debug) cout << endl;
	}

	for (int r = 0; r < R; r++) {
		if (emptyRow(r)) continue;
		for (int c = 1; c < C; c++) {
			if (matrix[r][c - 1] != '?' && matrix[r][c] == '?')
				matrix[r][c] = matrix[r][c - 1];
		}
		for (int c = C - 2; c >= 0; c--) {
			if (matrix[r][c + 1] != '?' && matrix[r][c] == '?')
				matrix[r][c] = matrix[r][c + 1];
		}
	}
	for (int r = 1; r < R; r++) {
		if (!emptyRow(r - 1) && emptyRow(r)) {
			for (int c = 0; c < C; c++)
				matrix[r][c] = matrix[r - 1][c];
		}
	}
	for (int r = R - 2; r >= 0; r--) {
		if (!emptyRow(r + 1) && emptyRow(r)) {
			for (int c = 0; c < C; c++)
				matrix[r][c] = matrix[r + 1][c];
		}
	}
	cout << "Case #" << CASE << ":" << endl;
	for (int r = 0; r < R; r++) {
		for (int c = 0; c < C; c++)
			cout << matrix[r][c];
		cout << endl;
	}
}

int main(int argc, const char * argv[]) {

	istream &fin = cin;
	// fstream fin("tiny.in");

	int T;
	fin >> T;
	for (int CASE = 1; CASE <= T; CASE++) {
		fin >> R >> C;
		for (int r = 0; r < R; r++) {
			string s;
			fin >> s;
			for (int c = 0; c < C; c++) {
				matrix[r][c] = s[c];
			}
		}
		solve(CASE);
	}
    return 0;
}
