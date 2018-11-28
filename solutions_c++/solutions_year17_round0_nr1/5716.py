#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int k = 4;
int dp[1025][1025];
int happy(int state, int flipped, int n) {
	if (state == pow(2, n) - 1) return 0;
	if (!(dp[state][flipped] == 0)) return dp[state][flipped];

	int min = -1;
	for (int i = 0; i <= n - k; i++) {
		int newState = state, newFlipped = flipped;
		bool used = ((flipped >> i) & 1);
		if (used) continue;

		newFlipped += (1 << i);
		for (int j = i; j - i < k; j++) {
			newState = newState - (((newState >> j) & 1) << j) + ((1 - ((newState >> j) & 1)) << j);
		}
		int x = happy(newState, newFlipped, n);
		if (x > -1 && (min == -1 || x + 1 < min)) min = x + 1;
	}

	return dp[state][flipped] = min;
}

int main() {
	ifstream infile("in31.in");
	ofstream out("out31.txt");
	int T;
	infile >> T;

	
	for (int t = 0; t < T; t++) {
		string str;
		infile >> str >> k;
		memset(dp, 0, sizeof dp[0][0] * 1025 * 1025);

		int initState = 0, c = 0;
		for (int i = str.length() - 1; i >= 0; i--) {
			if (str[i] == '+') initState += pow(2, c);
			c++;
		}

		int res = happy(initState, 0, str.length());
		if (res > -1) {
			out << "Case #" << t + 1 << ": " << res << endl;
		}
		else {
			out << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;
		}
	}

	system("pause");
	return 0;
}