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

struct pan {
	int r;
	int h;
	double lateralArea;
	double floorArea;
	pan(int r, int h) :r(r), h(h) {
		floorArea = M_PI * r * r;
		lateralArea = 2 * M_PI * r * h;
	}
};

bool cmpr(const pan &a, const pan &b) {
	if (a.r < b.r) {
		return true;
	}
	else if (a.r > b.r) {
		return false;
	}
	else {
		return a.lateralArea < b.lateralArea;
	}
}

bool cmpl(const pan &a, const pan &b) {
	return a.lateralArea > b.lateralArea;
}


int main() {
	redirectIO();
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		int N, K;
		cin >> N >> K;
		vector<pan> pans, pansR;
		int r, h;
		for (int j = 0; j < N; ++j) {
			cin >> r >> h;
			//pans.push_back(pan(r, h));
			pansR.push_back(pan(r, h));
		}
		
		double res = 0;
		cout << fixed << setprecision(9);

		sort(pansR.begin(), pansR.end(), cmpr);

		for (int j = K - 1; j < N; ++j) {
			double area = pansR[j].floorArea + pansR[j].lateralArea;
			sort(pansR.begin(), pansR.begin() + j, cmpl);
			for (int k = 0; k < K-1; ++k) {
				area += pansR[k].lateralArea;
			}
			if (area > res) {
				res = area;
			}
		}
		cout << "Case #" << i << ": " << res << endl;
	}
	recoverIO();
	//system("pause");
	return 0;
}