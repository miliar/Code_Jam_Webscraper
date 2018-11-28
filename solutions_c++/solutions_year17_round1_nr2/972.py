#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cassert>
#include <iomanip>
#include <algorithm>
using namespace std;

using ll = long long int;
ifstream fin("2.in");
ofstream fout("2.out");

int N, P;
int r[2];
int p[2][8];

int mymax(int amt, int recipie) {
	return floor((amt / 0.9) / recipie);
}

int mymin(int amt, int recipie) {
	return ceil((amt / 1.1) / recipie);
}

bool valid(int i, int j) {
	return (mymin(p[0][i], r[0]) <= mymax(p[1][j], r[1])) && (mymin(p[1][j], r[1]) <= mymax(p[0][i], r[0]));
}

int dfs(int cur, bool* history) {
	if (cur < 0)
		return 0;

	int best = 0;
	for (int i = 0; i < P; i++) {
		if (history[i] == false) {
			if (valid(cur, i)) {
				history[i] = true;
				best = max(best, 1 + dfs(cur - 1, history));
				history[i] = false;
			}
		}
	}
	return max(best, dfs(cur - 1, history));
}

int main() {
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		fout << "Case #" << t << ": ";
		fin >> N >> P;
		for (int j = 0; j < N; j++)
			fin >> r[j];
		for (int i = 0; i < N; i++)
			for (int j = 0; j < P; j++)
				fin >> p[i][j];

		int ans = 0;
		if (N == 1) {
			for (int j = 0; j < P; j++)
				ans += mymin(p[0][j], r[0]) <= mymax(p[0][j], r[0]);
			fout << ans << endl;
		}
		else {
			bool history[8] = {};
			fout << dfs(P-1, history) << endl;
		}
	}

}
