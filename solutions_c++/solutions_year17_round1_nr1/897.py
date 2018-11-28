// OI.cpp : Defines the entry point for the console application.

#include "stdafx.h"

#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <map>
#include <set>
using namespace std;

int T, r, c;
vector<vector<char>> a;

int main() {
	//ifstream fin("A-small-attempt0.in");
	//ofstream fout("A-small-attempt0.out");
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> T;
	for (int cse = 1; cse <= T; cse++) {
		cin >> r >> c;
		a = vector<vector<char>>(r + 1, vector<char>(c + 1, '?'));
		for (int i = 1; i <= r; i++) {
			string tmp;
			cin >> tmp;
			for (int j = 1; j <= c; j++) {
				a[i][j] = tmp[j - 1];
			}
		}
		for (int i = 1; i <= r; i++) {
			a[i][0] = '?';
			for (int j = 1; j <= c; j++) {
				if (a[i][j] != '?') {
					a[i][0] = a[i][j];
					break;
				}
			}
		}

		for (int i = 1; i <= r; i++) {
			for (int j = 1; j <= c; j++) {
				if (a[i][j] == '?')
					a[i][j] = a[i][j - 1];
			}
		}

		for (int j = 1; j <= c; j++) {
			a[0][j] = '?';
			for (int i = 1; i <= r; i++) {
				if (a[i][j] != '?') {
					a[0][j] = a[i][j];
					break;
				}
			}
		}

		for (int i = 1; i <= r; i++) {
			for (int j = 1; j <= c; j++) {
				if (a[i][j] == '?')
					a[i][j] = a[i - 1][j];
			}
		}

		//for (auto x : a) {
		//	cout << "                ";
		//	for (auto y : x)
		//		cout << y;
		//	cout << endl;
		//}
		cout << "Case #" << cse << ":" << endl;
		for (int i = 1; i <= r; i++) {
			for (int j = 1; j <= c; j++) {
				cout << a[i][j];
			}
			cout << endl;
		}

	}
	return 0;
}
