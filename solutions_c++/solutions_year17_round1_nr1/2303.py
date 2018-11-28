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

int R, C;

vector<string> B;

int CHECK(int i, int j1, int j2) {

	for (int j = j1; j <= j2; j++) {
		if (B[i].substr(j, 1) != "?") { return 0; }
	}
	return 1;
}

int CHANGE(int i, int j) {
   
//======= ‰¡
	int p;
	for (p = j - 1; p >= 0; p--) {
		if (B[i].substr(p, 1) == "?") { continue; }
		else { break; }
	}

	int q;
	for ( q = j + 1; q < C; q++) {
		if (B[i].substr(q, 1) == "?") { continue; }
		else { break; }
	}
	//cout << "p= " << p << " q= " << q << endl;
	string temp;

	string STR;
	STR = B[i].substr(j, 1); 

	for (int k = 0; k < C; k++) {
		if (p + 1 <= k && k <= q - 1) { temp += STR; }
		else { temp += B[i].substr(k, 1); }
	}

	B[i] = temp;
//=======================================//
	
	//==== c
	int m,n;

	for (m = i+1; m < R; m++) {
		if (CHECK(m, p+1, q-1) == 1) { continue; }
		else { break; }
	}

	for (n = i - 1; n >= 0; n--) {
		if (CHECK(n,p + 1, q - 1) == 1) { continue; }
		else { break; }
	}

	for (int h = n + 1; h < m; h++) {
		temp = "";
		for (int k = 0; k < C; k++) {
			if (p + 1 <= k && k <= q - 1) { temp += STR; }
			else { temp += B[h].substr(k, 1); }
		}
		B[h] = temp;
	}
	
	return 0;
}

void REP_B(void) {
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			cout << B[i].substr(j,1);
		}
		cout << endl;
	}
}

int main()
{
	ifstream ifs("A-large.in");
	ofstream ofs("answer_A_large");
	int T;
	ifs >> T; cout << "T= " << T << endl;

	set<string> S;

	string moji;

	for (int t = 0; t < T; t++) {  // test cases

		ifs >> R; cout << "R= " << R << endl;
		ifs >> C; cout << "C= " << C << endl;

		B.clear(); S.clear();

		string temp;
		for (int i = 0; i < R; i++) {
			ifs >> temp;
			B.push_back(temp);
		}

		
		for (int i = 0; i < R; i++) {  //‡‚É‚Ý‚Ä‚¢‚­
			for (int j = 0; j < C; j++) {
				moji = B[i].substr(j, 1);
				if ((moji != "?") && (S.find(moji) == S.end())) { CHANGE(i, j); S.insert(moji); }
				//REP_B();
			}
		}

		

		cout << "Case #" << t + 1 << ": " << endl;
		//REP_B();
		ofs << "Case #" << t + 1 << ": " << endl;
		for (int i = 0; i < R; i++) {
				ofs << B[i] << endl;
		}

	} // end of test cases

	system("pause");

	return 0;
}