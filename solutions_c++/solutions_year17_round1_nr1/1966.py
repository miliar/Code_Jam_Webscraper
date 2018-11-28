// Codejam_Sample.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <limits.h>
#include <algorithm>
#include <numeric>
#include <functional>
#include <fstream>
#include <iomanip> //cout << setprecision(10) << fixed << solve(n, m) << endl;

using namespace std;

//#define CONSOLE

#define IN		cin
#define OUT		cout

bool fillChar(vector<string>& table, int row, int col) {
	char c = '?';
	int l = col;
	while (l >= 0 && c == '?') {
		c = table[row][l];
		l--;
	}

	int r = col;
	while (r < table[row].size() && c == '?') {
		c = table[row][r];
		r++;;
	}

	if (c == '?')
		return false;


	for (int i = col; i > l; i--) 
		table[row][i] = c;
	for (int i = col; i < r; i++) 
		table[row][i] = c;

	return true;
}

void fillRow(vector<string>& table, unordered_set<int>& rowUpdate, int row) {	
	for (int i = row; i >= 0; i--) {
		if (rowUpdate.count(i))
			continue;

		for (int j = 0; j < table[i].size(); j++) 
			table[row][j] = table[i][j];

		return;
	}

	for (int i = row; i < table.size(); i++) {
		if (rowUpdate.count(i))
			continue;

		for (int j = 0; j < table[i].size(); j++)
			table[row][j] = table[i][j];

		return;
	}	
}

int main() {
#ifndef CONSOLE
	fstream IN, OUT;
	IN.open("in_large.txt", ios::in);
	OUT.open("out_large.txt", ios::out);
#endif

	/*
	*
	*	START CODE HERE
	*
	*/

	int T; IN >> T;

	for (int t = 0; t < T; t++) {
		int R, C;
		IN >> R >> C;

		vector<string> table(R, (1, string(C, '?')));
		char c = '?';
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				IN >> table[i][j];
				if (table[i][j] != '?')
					c = table[i][j];
			}
		}

		/*if (t + 1 == 25) {
			for (int i = 0; i < R; i++) {
				cout << table[i] << endl;
			}
		}*/

		if (c == '?') {
			OUT << "Case #" << t + 1 << ": " << endl;
			for (int i = 0; i < R; i++) 
				OUT << table[i] << endl;
			continue;
		}

		unordered_set<int> rowUpdate;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (table[i][j] == '?') {
					if (fillChar(table, i, j) == false) {
						rowUpdate.insert(i);
					}
				}
			}
		}

		for (auto iter = rowUpdate.begin(); iter != rowUpdate.end(); ++iter) 
			fillRow(table, rowUpdate, *iter);

		OUT << "Case #" << t + 1 << ": " << endl;
		for (int i = 0; i < R; i++)
			OUT << table[i] << endl;
	}


#ifndef CONSOLE
	IN.close();
	OUT.close();
#endif

	return 0;
}

