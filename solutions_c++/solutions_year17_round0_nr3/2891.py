// OI.cpp : Defines the entry point for the console application.
//

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
using namespace std;

int T;
long long n, k;

int main() {	
	ifstream fin("C-large.in");
	ofstream fout("C-large.out");
	fin >> T;
	for (int cse = 1; cse <= T; cse++) {
		fin >> n >> k;
		vector<long long> ql, qr, qp;
		
		ql.push_back(n / 2);
		qr.push_back(n / 2 - !(n % 2));
		qp.push_back(1);
		for (int i = 0; ql[i] || qr[i]; i++) {
			long long nl = ql[i] / 2;
			long long nr = ql[i] / 2 - !(ql[i] % 2);
			if (nl == ql.back() && nr == qr.back())
				qp.back() += qp[i];
			else {
				ql.push_back(nl);
				qr.push_back(nr);
				qp.push_back(qp[i]);
			}
			nl = qr[i] / 2;
			nr = qr[i] / 2 - !(qr[i] % 2);
			if (nl == ql.back() && nr == qr.back())
				qp.back() += qp[i];
			else {
				ql.push_back(nl);
				qr.push_back(nr);
				qp.push_back(qp[i]);
			}
		}
		int index = -1;
		for (int i = 0; i < qp.size(); i++) {
			k -= qp[i];
			if (k <= 0) {
				index = i;
				break;
			}
		}

		long long ans1 = ql[index];
		long long ans2 = qr[index];
		fout << "Case #" << cse << ": " << ans1 << ' ' << ans2 << endl;
	}
	return 0;
}

