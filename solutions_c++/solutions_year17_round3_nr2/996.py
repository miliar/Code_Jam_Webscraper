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
#include <cstdio>
#include <cmath>
#include <iomanip>
using namespace std;

# define M_PI           3.14159265358979323846  /* pi */

ifstream in("B-small-attempt1.in");
ofstream out("B-small-attempt1.out");
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

struct interval {
	int begin;
	int end;
	interval(int b, int e):begin(b),end(e){}
};

bool cmp(const interval &a, const interval &b) {
	return a.begin < b.begin;
}

int main() {
	redirectIO();
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		int Ac, Aj;
		cin >> Ac >> Aj;
		int Ci, Di, Ji, Ki;
		vector<interval> cvec, jvec;
		for (int j = 0; j < Ac; ++j) {
			cin >> Ci >> Di;
			cvec.push_back(interval(Ci, Di));
		}
		for (int j = 0; j < Aj; ++j) {
			cin >> Ji >> Ki;
			jvec.push_back(interval(Ji, Ki));
		}

		sort(cvec.begin(), cvec.end(), cmp);
		sort(jvec.begin(), jvec.end(), cmp);

		if (Ac == 1 && Aj == 1) {
			cout << "Case #" << i << ": 2"<< endl;
		}
		else if (Ac == 1 || Aj == 1) {
			cout << "Case #" << i << ": 2" << endl;
		}
		else if(Ac == 2){
			if (cvec[1].end - cvec[0].begin <= 720 || (cvec[0].end - 1 + 1440 - cvec[1].begin + 1) <= 720) {
				cout << "Case #" << i << ": 2" << endl;
			}
			else {
				cout << "Case #" << i << ": 4" << endl;
			}
		}
		else {
			if (jvec[1].end - jvec[0].begin <= 720 || (jvec[0].end - 1 + 1440 - jvec[1].begin + 1) <= 720) {
				cout << "Case #" << i << ": 2" << endl;
			}
			else {
				cout << "Case #" << i << ": 4" << endl;
			}
		}
		
	}
	recoverIO();
	//system("pause");
	return 0;
}