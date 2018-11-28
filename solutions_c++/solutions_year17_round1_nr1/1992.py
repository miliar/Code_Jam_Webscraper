// OJ.cpp : 定义控制台应用程序的入口点。
//
#include "stdafx.h"

#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>
#include <climits>
#include <cmath>
#include <sstream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

ifstream in("A-large.in");
ofstream out("A-large.out");
streambuf *cinbuf = cin.rdbuf();
streambuf *coutbuf = cout.rdbuf();

void redirectIO() {
	cin.rdbuf(in.rdbuf());
	cout.rdbuf(out.rdbuf());
}

void recoverIO() {
	cin.rdbuf(cinbuf);
	cout.rdbuf(coutbuf);
}

int main() {
	redirectIO();
	int T, R, C;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cin >> R >> C;
		vector<vector<char>> cake(R, vector<char>(C));
		bool headPending = true;
		for (int j = 0; j < R; ++j) {
			for (int k = 0; k < C; ++k) {
				cin >> cake[j][k];
			}
		}
		for (int j = 0; j < R; ++j) {
			bool first = false;
			char last = '\0';
			for (int k = 0; k < C; ++k) {
				if (!first && cake[j][k] != '?') {
					for (int l = 0; l < k; ++l) {
						cake[j][l] = cake[j][k];
					}
					first = true;
					last = cake[j][k];
					continue;
				}
				if (cake[j][k] == '?') {
					cake[j][k] = last;
				}
				else {
					last = cake[j][k];
				}
			}
			if (!first) {
				if (!headPending) {
					for (int k = 0; k < C; ++k) {
						cake[j][k] = cake[j - 1][k];
					}
				}
			}
			else {
				if (headPending) {
					for (int r = j-1; r >= 0; --r) {
						for (int c = 0; c < C; ++c) {
							cake[r][c] = cake[r + 1][c];
						}
					}
					headPending = false;
				}
			}
		}

		cout << "Case #" << i << ":" << endl;
		for (int j = 0; j < R; ++j) {
			for (int k = 0; k < C; ++k) {
				cout << cake[j][k];
			}
			cout << endl;
		}
	}
	recoverIO();
	//system("pause");
	return 0;
}