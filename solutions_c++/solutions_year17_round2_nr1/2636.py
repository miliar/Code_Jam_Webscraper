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
	int T, N, D;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cin >> D >> N;
		double maxTime = -1;
		int K, S;
		for (int j = 0; j < N; ++j) {
			cin >> K >> S;
			double t = (D - K) / (double)S;
			maxTime = max(maxTime, t);
		}
		cout.setf(ios::fixed);
		cout.precision(6);
		cout << "Case #" << i << ": " << D / maxTime << endl;
		//printf("Case #%d: %.6f\n", i, D / maxTime);
	}
	recoverIO();
	//system("pause");
	return 0;
}