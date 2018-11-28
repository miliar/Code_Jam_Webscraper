#include <bits/stdc++.h>
#include <cmath>
#include <climits>
#include <queue>
#include <vector>
#include <map>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>  // istringstream buffer(myString);
#include <stack>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <string>
#include <stdio.h>
// Get input
#define getstr(st) getline(std::cin, st)
#define getn(num) getline(std::cin, genstr);\
						stringToInt(genstr, num)
#define scanstr(s) scanf("%s", s)
#define scanch(c) scanf("%c", c)
#define _cin(a) cin>>a
#define __cin(a,b) cin>>a>>b
#define ___cin(a,b,c) cin>>a>>b>>c

//Define useful directives for vectors
#define VECBE(vec) vec.begin(), vec.end()
#define RVECBE(vec) vec.rbegin(), vec.rend()
#define VECS(vec) vec.size()

//Define useful number operators
#define inf INT_MAX
#define miinf INT_MIN
#define sti(str, num) stringToInt(str, num)
using namespace std;

// Define Loops
#define forle(lv, size) for (int lv = 0; lv <= size; lv++)
#define forl(lv, size) for (int lv = 0; lv < size; lv++)

//Typredef variable names
typedef long long int _lli;
typedef long int _li;
typedef int _i;
typedef float _f;
typedef double _d;
typedef string _s;
typedef char _c;
// Global Variables
string genstr;
template <class T>
void stringToInt(string st, T &num) {
	istringstream stringsstream(st);
	stringsstream >> num;
}

bool idcharpresent(char ch[], char c) {
	forl(i, 25) {
		if (ch[i] == c)
			return true;
	}
	return false;
}

void addcharpresent(char ch[], char c) {
	forl(i, 25) {
		if (ch[i] == '.') {
			ch[i] = c;
			break;
		}
	}
}


void ProcessMainAlgorithm(_i z) {
	char cake[25][25];
	char pr[25];
	forl(i, 25) {
		pr[i] = '.';
	}
	int R, C;
	__cin(R, C);
	forl(i, R) {
		scanstr(&cake[i]);
	}
	forl(i, R) {
		forl(j, C) {
			if (cake[i][j] == '?') {
				for (int k = i - 1; k >= 0; k--) {
					if (cake[k][j] != '?' && !idcharpresent(pr, cake[k][j])) {
						cake[i][j] = cake[k][j];
						break;
					}
					else if (cake[k][j] == '?' && idcharpresent(pr, cake[k][j])) {
						break;
					}
				}
				for (int k = i + 1; k < R; k++) {
					if (cake[k][j] != '?' && !idcharpresent(pr, cake[k][j])) {
						cake[i][j] = cake[k][j];
						break;
					}
					else if (cake[k][j] == '?' && idcharpresent(pr, cake[k][j])) {
						break;
					}

				}
			}
			if (cake[i][j] != '?' && !idcharpresent(pr, cake[i][j])) {
				addcharpresent(pr, cake[i][j]);
				int r1 = i, r2 = i;
				// Fill above
				for (int k = i - 1; k >= 0; k--) {
					if (cake[k][j] == '?' || cake[i][j] == cake[k][j]) {
						cake[k][j] = cake[i][j];
						r1 = k;
					}
					else {
						break;
					}
				}
				// Fill below
				for (int k = i + 1; k < R; k++) {
					if (cake[k][j] == '?' || cake[i][j] == cake[k][j]) {
						cake[k][j] = cake[i][j];
						r2 = k;
					}
					else {
						break;
					}
				}
				/*
				cout << endl;
				forl(i1, R) {
					forl(j1, C) {
						cout << cake[i1][j1];
					}
					cout << endl;
				}
				forl(i1, 25) {
					cout << pr[i1] << " ";
				}
				cout << endl;
				*/
				// Fill left column
				for (int k = j - 1; k >= 0; k--) {
					bool flag = true;
					for (int l = r1; l <= r2; l++) {
						if (cake[l][k] != '?') flag = false;
					}
					if (flag) {
						for (int l = r1; l <= r2; l++) {
							cake[l][k] = cake[i][j];
						}
					}
					else {
						break;
					}
				}
				// Fill right column
				for (int k = j + 1; k < C ; k++) {
					bool flag = true;
					for (int l = r1; l <= r2; l++) {
						if (cake[l][k] != '?') flag = false;
					}
					if (flag) {
						for (int l = r1; l <= r2; l++) {
							cake[l][k] = cake[i][j];
						}
					}
					else {
						break;
					}

				}
			}
		}
	}

	cout << endl;
	forl(i, R) {
		forl(j, C) {
			cout << cake[i][j];
		}
		cout << endl;
	}
}


int main(){
	_i nooftestcases;
	_cin(nooftestcases);
	forl(i, nooftestcases) {
		cout << "Case #" << i + 1 << ": ";
		ProcessMainAlgorithm(i);
		cout<< endl;
	}
	return 0;
}