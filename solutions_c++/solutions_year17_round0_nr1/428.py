#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <queue>
#include <cmath>

using namespace std;

string str;
int N;
int C[3000];
int K;

int NUM;

void FLIP(int m) {
	for (int i = m; i < m + K; i++) { if (C[i] == 1) { C[i] = 0; } else { C[i] = 1; } }
}

int CHECK() {
	for (int i = 0; i < N; i++) { if (C[i] == 0) { return -1; } }
	return 1;
}

int main()
{
	ifstream ifs("A-large.in");
	ofstream ofs("answer_A_large");
	int T;
	ifs >> T; cout << "T= " << T << endl;

	for (int t = 0; t<T; t++) {  // test cases

		ifs >> str; // cout << str << endl;

		N = str.size();

		for (int i = 0; i < N; i++) {
			if (str.substr(i, 1) == "+") { C[i] = 1; }
		else { C[i] = 0; }
		//cout << C[i];
		}
	//	cout << endl;
		ifs >> K; //cout << "K= " << K << endl;

		NUM = 0;
		for (int i = 0; i + K <= N;i++) {
			if (C[i] == 0) { FLIP(i); NUM++; }
		}
		

		cout << "Case #" << t + 1 << ": ";
		if (CHECK() == 1) { cout << NUM << endl; }
		else { cout << "IMPOSSIBLE" << endl; }
		ofs << "Case #" <<t+1<<": ";
		if (CHECK() == 1) { ofs << NUM << endl; }
		else { ofs << "IMPOSSIBLE" << endl; }

	} // end of test cases

	system("pause");
	return 0;
}