#include <iostream>
#include <vector>
#include <string>

typedef long long ll;
//typedef pair<int, int> PII;

#define first fi
#define second se

using namespace std;

bool blankRow(string s, int C) {
	string blankRow_;
	char question_mark = '?';
	for (int c = 0; c < C; c ++) blankRow_.push_back(question_mark);
	return (s == blankRow_);
}

void set(vector<string> & cake, int r, int c, char tmp) {
	cake[r][c] = tmp;
	return;
}

string divide(vector<string> & cake, int r, int C) {
	//divide the r-th row according to the initials on the r-th row
	string result;
	int c = 0;
	while(cake[r][c] == '?')
		c ++;
	//this is the first non-blank column
	char tmp = cake[r][c];
	for (int cc =0; cc <= c; cc ++)
		result.push_back(tmp);
	for (c = c + 1; c < C; c ++) {
		if (cake[r][c] != '?')
			tmp = cake[r][c];
		result.push_back(tmp);
	}
	cake[r] = result;
	return result;
}

void solve(vector<string> & cake, int R, int C) {
	int r = 0;
	while(blankRow(cake[r], C)) {
		r++;
	}
	//this is the first non-blank row
	string rowR = divide(cake, r, C);
	for (int rr = 0; rr < r; rr ++)
		cake[rr] = rowR;
	//solve r+1...R-1 rows
	for (; r < R; r++) {
		if (blankRow(cake[r], C))
			cake[r] = rowR;
		else
			rowR = divide(cake, r, C);
	}
	return;
}

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int R, C;
		vector<string> cake;
		string s;

		cin >> R >> C;
		for (int r = 0; r < R; r++) {
			cin >> s;
			cake.push_back(s);
		}

		solve(cake, R, C);

		cout << "Case #" << t + 1 << ":" << endl;
		for (int r = 0; r < R; r++)
			cout << cake[r] << endl;
		}
	return 0;
}
