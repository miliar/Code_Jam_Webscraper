#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#include <stdlib.h>

using namespace std;

typedef unsigned long int uli;  // 18^18

void Flip(vector<bool>* B, int s, int K) {
	for (int i = s; i < s+K; i++) {
		(*B)[i] = !((*B)[i]);
	}
}

void main() {
	string file = "A-large";
	ifstream ifile(file + ".in");
	ofstream ofile(file + ".out");
	//
	int T;
	ifile >> T;
	string dummy;
	getline(ifile, dummy);
	for (int t = 1; t <= T; t++) {
		cout << "t: " << t << endl;
		string S;
		getline(ifile, S);
		vector<bool> B;
		int K;
		for (int i = 0; i < S.size(); i++) {
			char s = S[i];
			if (' ' == s) {
				string ss = S.substr(i+1);
				K = atoi(ss.c_str());
				break;
			}
			bool b = '+' == s ? true : false;
			B.push_back(b);
		}
		int flip_count = 0;
		for (int i = 0; i < B.size() - K + 1; i++) {
			if (B[i]) continue;
			Flip(&B, i, K);
			flip_count++;
		}
		bool is_good = true;
		for (const auto& b : B) {
			if (!b) is_good = false;
		}
		ofile << "Case #" << t << ": ";
		if (is_good)
			ofile << flip_count << endl;
		else
			ofile << "IMPOSSIBLE" << endl;

	}
	//
	ifile.close();
	ofile.close();
}