
#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

void flip(vector<char> &s, int idx, int k) {

	for (int i = idx, limit = idx + k; i < limit; i++) {
		if (i > (int)s.size() - 1) break;
		if (s[i] == '+') {
			s[i] = '-';
		}
		else {
			s[i] = '+';
		}
	}
}

int main()
{
	const string IMPOSSIBLE = "IMPOSSIBLE";
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	int T;
	string tStr;
	getline(fin, tStr);
	istringstream is(tStr);
	is >> T;

	string sStr, tempStr;
	int K;

	for (int i = 1; i <= T; i++) {
		getline(fin, sStr);
		istringstream is(sStr);
		is >> tempStr >> K;

		vector<char> S(tempStr.begin(), tempStr.end());
		int flipCnt = 0;
		for (int j = 0, leng = S.size(); j < leng; j++) {
			if (leng - j < K)	break;
			if (S[j] == '-') {
				flip(S, j, K);
				flipCnt++;
			}
		}

		bool canBeHappy = true;
		string comStr = string(S.begin(), S.end());

		if (comStr.find("-") != string::npos) {
			canBeHappy = false;
		}
		
		if (canBeHappy) {
			fout << flipCnt << endl;
		}
		else {
			fout << IMPOSSIBLE << endl;
		}
	}

	fin.close();
	fout.close();
	return 0;
}
